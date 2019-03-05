.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b F
.field static x Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	bipush 8
	putstatic MPClass.a I
	getstatic MPClass.a I
	i2f
	iconst_2
	i2f
	fdiv
	iconst_5
	i2f
	fadd
	putstatic MPClass.b F
	iconst_0
	ifle Label4
	iconst_1
	iconst_1
	invokestatic MPClass/nhat(I)Z
	iand
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	bipush 7
	putstatic MPClass.a I
	goto Label3
Label2:
	iconst_5
	invokestatic io/putInt(I)V
Label3:
Label1:
	return
.limit stack 5
.limit locals 1
.end method

.method public static nhat(I)Z
.var 0 is v I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putInt(I)V
	iconst_1
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
