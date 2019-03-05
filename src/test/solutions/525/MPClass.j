.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is i I from Label2 to Label3
.var 2 is j I from Label2 to Label3
Label2:
	bipush 10
	istore_1
	iconst_3
	istore_2
	iload_1
	iload_2
	isub
	invokestatic io/putIntLn(I)V
Label3:
.var 1 is i F from Label4 to Label5
Label4:
.var 2 is j F from Label6 to Label7
Label6:
	ldc 1.5
	fstore_1
	ldc 2.5
	fstore_2
	fload_1
	fload_2
	fsub
	invokestatic io/putFloat(F)V
Label7:
Label5:
Label1:
	return
.limit stack 2
.limit locals 3
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
