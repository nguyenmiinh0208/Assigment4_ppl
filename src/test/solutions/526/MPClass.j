.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b F

.method public static testIf()V
Label0:
	bipush 10
	putstatic MPClass.a I
	ldc 9.98
	putstatic MPClass.b F
	getstatic MPClass.a I
	i2f
	getstatic MPClass.b F
	fcmpl
	ifle Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	getstatic MPClass.a I
	bipush 10
	if_icmplt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	getstatic MPClass.a I
	getstatic MPClass.a I
	imul
	putstatic MPClass.a I
	goto Label7
Label6:
	getstatic MPClass.a I
	i2f
	getstatic MPClass.b F
	fsub
	putstatic MPClass.b F
Label7:
	getstatic MPClass.a I
	invokestatic io/putIntLn(I)V
	getstatic MPClass.b F
	invokestatic io/putFloat(F)V
	goto Label3
Label2:
Label3:
Label1:
	return
.limit stack 2
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/testIf()V
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
