.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static g Z

.method public static testReturnBool()Z
Label0:
	iconst_0
	putstatic MPClass.g Z
	getstatic MPClass.g Z
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/testReturnBool()Z
	invokestatic io/putBool(Z)V
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
