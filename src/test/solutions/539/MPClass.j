.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
Label0:
	iconst_5
	invokestatic MPClass/foo(I)I
	istore_1
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 2
.end method

.method public static foo(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	goto Label1
Label1:
	ireturn
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
