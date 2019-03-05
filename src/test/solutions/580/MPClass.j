.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c F from Label0 to Label1
Label0:
	iconst_5
	istore_1
	iload_1
	invokestatic MPClass/foo(I)I
	i2f
	fstore_2
	fload_2
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 1
.limit locals 3
.end method

.method public static foo(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iload_0
	imul
	goto Label1
Label1:
	ireturn
.limit stack 2
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
