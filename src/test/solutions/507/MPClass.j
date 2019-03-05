.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static foo()V
.var 0 is a F from Label0 to Label1
.var 1 is b F from Label0 to Label1
Label0:
	ldc 0.5
	fstore_0
	ldc 9.75
	fstore_1
	fload_0
	invokestatic io/putFloatLn(F)V
	fload_1
	invokestatic io/putFloat(F)V
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
