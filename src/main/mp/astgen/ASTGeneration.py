from MPVisitor import MPVisitor
from MPParser import MPParser
from AST import *

class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        #return Program([self.visit(x) for x in ctx.one_Dec()])
        return Program([decl for decls in ctx.one_Dec() for decl in self.visit(decls)])

    def visitFun_dec(self, ctx: MPParser.Fun_decContext):
        return [FuncDecl(Id(ctx.ID().getText()),
                        self.visit(ctx.paramList()),                            # param
                        self.visit(ctx.var_dec()) if ctx.var_dec() else [],     #local
                        self.visit(ctx.compound()),                             #compoundstmt
                        self.visit(ctx.type_D()) if ctx.type_D() else self.visit(ctx.array()))]  #return type

    def visitProce_dec(self, ctx: MPParser.Proce_decContext):
        return [FuncDecl(Id(ctx.ID().getText()),
                        self.visit(ctx.paramList()),  # param
                        self.visit(ctx.var_dec()) if ctx.var_dec() else [],  # local
                        self.visit(ctx.compound()))]  # compoundstmt

    def visitParamList(self, ctx: MPParser.ParamListContext):
        return [param for paramdecl in ctx.param() for param in self.visit(paramdecl)]

    def visitParam(self, ctx: MPParser.ParamContext):
        return [VarDecl(Id(x.getText()), self.visit(ctx.type_D()) if ctx.type_D() else self.visit(ctx.array())) for x in ctx.ID()]

    def visitArray(self, ctx: MPParser.ArrayContext):
        return ArrayType(int(('-' if ctx.subop1() else '') + ctx.INTLIT(0).getText()),  # lower
                         int(('-' if ctx.subop2() else '') + ctx.INTLIT(1).getText()),  # upper
                         self.visit(ctx.type_D()))                                      # eleType

    def visitType_D(self, ctx: MPParser.Type_DContext):
        if ctx.BOOLEAN():
            return BoolType()
        elif ctx.INTTYPE():
            return IntType()
        elif ctx.REALTYPE():
            return FloatType()
        else:
            return StringType()

    def visitVar_dec(self, ctx: MPParser.Var_decContext):
        return [vardecl for varlist in ctx.variable() for vardecl in self.visit(varlist)]

    def visitVariable(self, ctx: MPParser.VariableContext):
        return [VarDecl(Id(x.getText()), self.visit(ctx.type_D()) if ctx.type_D() else self.visit(ctx.array())) for x in ctx.ID()]

    def visitAssignment(self, ctx: MPParser.AssignmentContext):
        return reversed([Assign(self.visit(x), self.visit(y)) for x, y in zip(ctx.lhs(), ctx.lhs()[1:] + [ctx.exp()])])

    def visitLhs(self, ctx: MPParser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.exp_id())

    def visitIf_stmt(self, ctx: MPParser.If_stmtContext):
        return [If(self.visit(ctx.exp()), self.visit(ctx.statement(0)), self.visit(ctx.statement(1)) if ctx.statement(1) else [])]

    def visitWhile_stmt(self, ctx: MPParser.While_stmtContext):
        return [While(self.visit(ctx.exp()), self.visit(ctx.statement()))]

    def visitFor_stmt(self, ctx: MPParser.For_stmtContext):
        return [For(Id(ctx.ID().getText()), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)), True if ctx.TO() else False,
                    self.visit(ctx.statement()))]

    def visitBr_stmt(self, ctx: MPParser.Br_stmtContext):
        return [Break()]

    def visitContinue_stmt(self, ctx: MPParser.Continue_stmtContext):
        return [Continue()]

    def visitReturn_stmt(self, ctx: MPParser.Return_stmtContext):
        return [Return(self.visit(ctx.exp()) if ctx.exp() else None)]

    def visitCompound(self, ctx: MPParser.CompoundContext):
        return [stmt_ for stmt in ctx.statement() for stmt_ in self.visit(stmt)]

    def visitWith_stmt(self, ctx: MPParser.With_stmtContext):
        return [With([vardecl for varlist in ctx.variable() for vardecl in self.visit(varlist)], self.visit(ctx.statement()))]

    def visitCall(self, ctx: MPParser.CallContext):
        return CallExpr(Id(ctx.ID().getText()), [self.visit(x) for x in ctx.manyexp().exp()] if ctx.manyexp() else [])

    def visitFuncall(self, ctx: MPParser.FuncallContext):
        return [CallStmt(Id(ctx.call().ID().getText()),
                         [self.visit(x) for x in ctx.call().manyexp().exp()] if ctx.call().manyexp() else [])]

    def visitExp(self, ctx: MPParser.ExpContext):
        if ctx.andthenop():
            return BinaryOp('andthen', self.visit(ctx.exp()), self.visit(ctx.exp1()))
        elif ctx.orelseop():
            return BinaryOp('orelse', self.visit(ctx.exp()), self.visit(ctx.exp1()))
        else:
            return self.visit(ctx.exp1())

    def visitExp1(self, ctx: MPParser.Exp1Context):
        if ctx.EQUOP():
            return BinaryOp('=', self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.NEOP():
            return BinaryOp('<>', self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.LTOP():
            return BinaryOp('<', self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.LTEOP():
            return BinaryOp('<=', self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.MTOP():
            return BinaryOp('>', self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        elif ctx.MTEOP():
            return BinaryOp('>=', self.visit(ctx.exp2(0)), self.visit(ctx.exp2(1)))
        else:
            return self.visit(ctx.exp2(0))

    def visitExp2(self, ctx: MPParser.Exp2Context):
        if ctx.ADDOP():
            return BinaryOp('+', self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        elif ctx.SUBOP():
            return BinaryOp('-', self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        elif ctx.OROP():
            return BinaryOp(ctx.OROP().getText(), self.visit(ctx.exp2()), self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())

    def visitExp3(self, ctx: MPParser.Exp3Context):
        if ctx.DIVOP():
            return BinaryOp('/', self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.MULOP():
            return BinaryOp('*', self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.DIV():
            return BinaryOp(ctx.DIV().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.MODOP():
            return BinaryOp(ctx.MODOP().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        elif ctx.ANDOP():
            return BinaryOp(ctx.ANDOP().getText(), self.visit(ctx.exp3()), self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())

    def visitExp4(self, ctx: MPParser.Exp4Context):
        if ctx.SUBOP():
            return UnaryOp('-', self.visit(ctx.exp4()))
        elif ctx.NOTOP():
            return UnaryOp(ctx.NOTOP().getText(), self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.operand())

    def visitOperand(self, ctx: MPParser.OperandContext):
        if ctx.operand2():
            return self.visit(ctx.operand2())
        else:
            return self.visit(ctx.exp_id())

    def visitOperand2(self, ctx: MPParser.Operand2Context):
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(True if str.lower(ctx.BOOLLIT().getText()) == 'true' else False)
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.call():
            return self.visit(ctx.call())
        else:
            return self.visit(ctx.exp())

    def visitExp_id(self, ctx: MPParser.Exp_idContext):
        if ctx.operand2():
            return ArrayCell(self.visit(ctx.operand2()), self.visit(ctx.exp()))
        else:
            return ArrayCell(self.visit(ctx.exp_id()), self.visit(ctx.exp()))