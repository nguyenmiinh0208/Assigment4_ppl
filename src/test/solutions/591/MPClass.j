.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a F
.field static b F
.field static c F
.field static out Z

.method public static foo(F)F
.var 0 is c F from Label0 to Label1
Label0:
	ldc 1.2
	goto Label1
	ldc 1.3
	goto Label1
Label1:
	freturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	invokestatic MPClass/foo(F)F
	iconst_1
	invokestatic MPClass/foo(F)F
	invokestatic MPClass/foo(F)F
	invokestatic MPClass/foo(F)F
	invokestatic MPClass/foo(F)F
	invokestatic MPClass/foo(F)F
	fadd
	putstatic MPClass.a F
	getstatic MPClass.a F
	putstatic MPClass.c F
	getstatic MPClass.c F
	iconst_2
	i2f
	fdiv
	invokestatic io/putFloatLn(F)V
	getstatic MPClass.a F
	iconst_2
	i2f
	fdiv
	invokestatic io/putFloatLn(F)V
Label1:
	return
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
