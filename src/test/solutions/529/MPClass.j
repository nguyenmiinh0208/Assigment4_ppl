.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static testCallExpr(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 9
	invokestatic MPClass/testCallExpr(I)I
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public <init>()V
.var 0 is this LMPClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
