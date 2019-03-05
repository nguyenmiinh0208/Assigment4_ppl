.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label0:
	iconst_2
	istore_1
	ldc 1.5
	fstore_2
.var 3 is i I from Label2 to Label3
.var 4 is j I from Label2 to Label3
Label2:
	bipush 10
	istore_3
	iconst_3
	istore 4
	iload_3
	iload 4
	if_icmpeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label4
	iload_3
	iload_1
	iadd
	istore_3
	goto Label5
Label4:
	iload 4
	iload_1
	iconst_2
	imul
	iadd
	istore 4
Label5:
	iload_3
	iload 4
	isub
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 3
.limit locals 5
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
