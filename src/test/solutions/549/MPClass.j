.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is iSum I from Label0 to Label1
Label0:
	iconst_0
	istore_2
	iload_2
	istore_1
	iload_1
	istore_3
	iload_3
	invokestatic io/putIntLn(I)V
	iload_1
	invokestatic io/putIntLn(I)V
	iload_2
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 4
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
