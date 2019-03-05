.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i F

.method public static testCallStmt(IFF)V
.var 0 is a I from Label0 to Label1
.var 1 is b F from Label0 to Label1
.var 2 is c F from Label0 to Label1
Label0:
	iload_0
	i2f
	fload_1
	fadd
	fload_2
	fadd
	putstatic MPClass.i F
	getstatic MPClass.i F
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 10
	iconst_1
	ldc 1.5
	invokestatic MPClass/testCallStmt(IFF)V
Label1:
	return
.limit stack 3
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
