.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo()V
.var 0 is a I from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	iconst_5
	istore_0
	bipush 7
	istore_1
	iload_0
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/foo()V
Label1:
	return
.limit stack 0
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
