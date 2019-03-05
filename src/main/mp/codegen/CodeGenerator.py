'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType(list(), FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType(list(), VoidType()), CName(self.libName)),
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        for x in ast.decl:
            e = self.visit(x, (e, True))    # get name global
        for x in ast.decl:
            self.visit(x, (e, False))  # generate code
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), e.sym, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None
        isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        glenv = reduce(lambda x, y: [self.visit(y, (frame, "decl"))] + x, consdecl.param, glenv)
        glenv = reduce(lambda x, y: [self.visit(y, (frame, "decl"))] + x, consdecl.local, glenv)
        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        list(map(lambda x: self.visit(x, SubBody(frame, glenv)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        
       # if type(returnType) is VoidType:
        self.emit.printout(self.emit.emitRETURN(returnType, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any
        subctxt = o[0]
        if o[1] is True:
            retType = MType([x.varType for x in ast.param], ast.returnType )
            return SubBody(None, [Symbol(ast.name.name, retType, CName(self.className))] + subctxt.sym)
        # o[1] is False
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym, frame)
        
    def visitVarDecl(self, ast, o):
        subctxt = o[0]
        if o[1] is True:
            retType = ast.varType
            self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, retType, False, None))
            return SubBody(None, [Symbol(ast.variable.name, retType, CName(self.className))] + subctxt.sym)
        elif o[1] == "decl":# o[0] is frame
            retType = ast.varType
            frame=o[0]
            index = frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, ast.variable.name, retType, frame.getStartLabel(), frame.getEndLabel(), frame))
            return Symbol(ast.variable.name, retType, Index(index))

    def visitWith(self, ast, o):
        subctxt = o
        frame= subctxt.frame
        frame.enterScope(False)

        nenv = reduce(lambda x, y: [self.visit(y, (frame, "decl"))] + x, ast.decl, subctxt.sym)

        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        # generate code for body
        for x in ast.stmt:
            self.visit(x, SubBody(frame, nenv))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

    
    def visitIf(self, ast, o):
        subctxt = o 
        frame = subctxt.frame
        sym = subctxt.sym
        elseLb = frame.getNewLabel()
        endLb = frame.getNewLabel()

        expcode, expType = self.visit(ast.expr, Access(frame, sym, False, True))

        self.emit.printout(expcode)
        # generate code for thenstmt
        self.emit.printout(self.emit.emitIFFALSE(elseLb,frame))
        list(map(lambda x: self.visit(x, subctxt), ast.thenStmt))
        self.emit.printout(self.emit.emitGOTO(endLb, frame))
         # generate code for elsestmt
        self.emit.printout(self.emit.emitLABEL(elseLb,frame))
        list(map(lambda x: self.visit(x, subctxt), ast.elseStmt))
        self.emit.printout(self.emit.emitLABEL(endLb,frame))
   
    def visitFor(self, ast, o):
        frame = o.frame
        sym = o.sym
        code_expr1, typeExpr1 = self.visit(ast.expr1,Access(frame,sym,False,True))
        idStore, _ = self.visit(ast.id,Access(frame,sym,True,False))
        self.emit.printout(code_expr1 + idStore)

        frame.enterLoop()
        strLabel = frame.getNewLabel()
        ConLabel = frame.getContinueLabel()
        BrkLabel = frame.getBreakLabel()

        self.emit.printout(self.emit.emitLABEL(strLabel,frame))
        idLoad, _ = self.visit(ast.id,Access(frame,sym,False,False))
        code_expr2, typeExpr2 = self.visit(ast.expr2,Access(frame, sym, False, True))
        if ast.up:
            self.emit.printout(idLoad + code_expr2 + self.emit.emitREOP("<=",typeExpr2,frame))
        else:
            self.emit.printout(idLoad + code_expr2 + self.emit.emitREOP(">=",typeExpr2,frame))
        self.emit.printout(self.emit.emitIFFALSE(BrkLabel, frame))
        for x in ast.loop:
            self.visit(x,Access(frame,sym,False,True))

        self.emit.printout(self.emit.emitLABEL(ConLabel,frame))
        self.emit.printout(self.emit.emitINCREASE(idStore, idLoad, ast.up, frame))
        self.emit.printout(self.emit.emitGOTO(strLabel,frame))
        self.emit.printout(self.emit.emitLABEL(BrkLabel,frame))
        frame.exitLoop()
    
    def visitWhile(self, ast, o):
        ctxt = o
        sym = o.sym
        frame = o.frame

        frame.enterLoop()
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()

        #generate code for continue label
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))

        #generate code for expr
        code,ret = self.visit(ast.exp, Access(frame, sym, False, True))
        self.emit.printout(code)

        #generate code for break label
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))

        #generate code for listStmt
        list(map(lambda x: self.visit(x, o), ast.sl))

        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        frame.exitLoop()

    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(),o.frame))
    
    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(),o.frame))
    
    def visitReturn(self, ast, o):
        frame = o.frame
        retType = frame.returnType
        expcode, expType = "",[]
        if ast.expr:
            expcode, expType = self.visit(ast.expr, Access(frame, o.sym, False, True))
            if type(retType) != type(expType):
                expcode = expcode + self.emit.emitI2F(frame)
        self.emit.printout(expcode)
        self.emit.printout(self.emit.emitGOTO(frame.getEndLabel(), frame))
        
    def visitAssign(self, ast, o):
        cRight,retRight = self.visit(ast.exp,Access(o.frame,o.sym,False,True))
        cLeft,retLeft = self.visit(ast.lhs,Access(o.frame,o.sym,True,False))
        code = cRight + cLeft
        if type(retRight) != type(retLeft):
            code = cRight + self.emit.emitI2F(o.frame) + cLeft
        self.emit.printout(code)

    def visitId(self, ast, o):
        sym = o.sym
        frame = o.frame
        sym = self.lookup(ast.name.lower(), sym, lambda x: x.name.lower())
        reType = sym.mtype
        cname = sym.value
        idx = sym.value.value
        id_code = ""
        # id is left not first
        if o.isLeft == True and o.isFirst == False:
            if type(cname) is CName:
                id_code = self.emit.emitPUTSTATIC(cname.value + "." + ast.name, reType, frame )
            else:
                id_code = self.emit.emitWRITEVAR(ast.name, reType, idx, frame)
        elif o.isLeft == False:
            if type(cname) is CName:
                id_code = self.emit.emitGETSTATIC(cname.value + "." + ast.name, reType, frame )
            else:
                id_code = self.emit.emitREADVAR(ast.name, reType, idx, frame)
        return id_code , reType

    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype

        in_ = ("", [])
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1] + [typ1] )
        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame))
        
    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype

        in_ = ("", [])
        for x in ast.param:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1] + [typ1] )
        
        return in_[0] + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame), ctype.rettype

    def visitBinaryOp(self, ast, o):
        ctxt = o
        frame = ctxt.frame

        lc, lt = self.visit(ast.left, o)
        rc, rt = self.visit(ast.right, o)
        retType = None

        if type(lt) == type(rt):
            if ast.op == '/':
                lc += self.emit.emitI2F(frame)
                rc += self.emit.emitI2F(frame) 
                retType = FloatType()
            else:
                retType = lt
        elif type(lt) is IntType:
            lc += self.emit.emitI2F(frame)
            retType = FloatType()
        else:
            rc += self.emit.emitI2F(frame)
            retType = FloatType() 
        if ast.op in ["+", "-"]:
            return lc + rc + self.emit.emitADDOP(ast.op, retType, frame), retType
        elif ast.op in ["*", "/"]:
            return lc + rc + self.emit.emitMULOP(ast.op, retType, frame), retType
        elif ast.op.lower() == "div":
            return lc + rc + self.emit.emitDIV(frame), retType
        elif ast.op.lower() == "mod":
            return lc + rc + self.emit.emitMOD(frame), retType
        elif ast.op.lower() == "and": # and
            return lc + rc + self.emit.emitANDOP(frame), retType
        elif ast.op.lower() == "or":
            return lc + rc + self.emit.emitOROP(frame), retType
        elif ast.op.lower() in ["andthen","orelse"]:
            pass
        else: #( >, <, <>, =, >=, <=)
            return lc + rc + self.emit.emitREOP(ast.op, retType, frame), BoolType()
    
    def visitUnaryOp(self, ast, o):
        frame = o.frame
        op = ast.op.lower()
        cExp,retType = self.visit(ast.body, o)
        code = ""
        if op == "not":
            code = cExp + self.emit.emitNOT(retType, frame)
            retType = BoolType()
        elif op == "-":
            code = cExp + self.emit.emitNEGOP(retType,frame)
        return code,retType
        
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        return self.emit.emitPUSHICONST(ast.value, o.frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any
        return self.emit.emitPUSHFCONST(str(float(ast.value)), o.frame), FloatType()

    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(str(ast.value).lower(), o.frame), BoolType()

    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, StringType(), o.frame), StringType()