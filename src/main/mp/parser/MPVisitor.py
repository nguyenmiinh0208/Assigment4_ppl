# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#one_Dec.
    def visitOne_Dec(self, ctx:MPParser.One_DecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_dec.
    def visitVar_dec(self, ctx:MPParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#variable.
    def visitVariable(self, ctx:MPParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#type_D.
    def visitType_D(self, ctx:MPParser.Type_DContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#array.
    def visitArray(self, ctx:MPParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#subop1.
    def visitSubop1(self, ctx:MPParser.Subop1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#subop2.
    def visitSubop2(self, ctx:MPParser.Subop2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#fun_dec.
    def visitFun_dec(self, ctx:MPParser.Fun_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#paramList.
    def visitParamList(self, ctx:MPParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#param.
    def visitParam(self, ctx:MPParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound.
    def visitCompound(self, ctx:MPParser.CompoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statement.
    def visitStatement(self, ctx:MPParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment.
    def visitAssignment(self, ctx:MPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lhs.
    def visitLhs(self, ctx:MPParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#andthenop.
    def visitAndthenop(self, ctx:MPParser.AndthenopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#orelseop.
    def visitOrelseop(self, ctx:MPParser.OrelseopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operand.
    def visitOperand(self, ctx:MPParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#operand2.
    def visitOperand2(self, ctx:MPParser.Operand2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp_id.
    def visitExp_id(self, ctx:MPParser.Exp_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#if_stmt.
    def visitIf_stmt(self, ctx:MPParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#for_stmt.
    def visitFor_stmt(self, ctx:MPParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#while_stmt.
    def visitWhile_stmt(self, ctx:MPParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#br_stmt.
    def visitBr_stmt(self, ctx:MPParser.Br_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continue_stmt.
    def visitContinue_stmt(self, ctx:MPParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#with_stmt.
    def visitWith_stmt(self, ctx:MPParser.With_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_stmt.
    def visitReturn_stmt(self, ctx:MPParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcall.
    def visitFuncall(self, ctx:MPParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#call.
    def visitCall(self, ctx:MPParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#manyexp.
    def visitManyexp(self, ctx:MPParser.ManyexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#proce_dec.
    def visitProce_dec(self, ctx:MPParser.Proce_decContext):
        return self.visitChildren(ctx)



del MPParser