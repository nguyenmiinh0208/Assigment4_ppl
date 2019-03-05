.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static fa F
.field static fb F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is isTrue Z from Label0 to Label1
Label0:
	iconst_1
	putstatic MPClass.a I
	getstatic MPClass.a I
	iconst_1
	iadd
	putstatic MPClass.b I
	getstatic MPClass.b I
	iconst_1
	rem
	putstatic MPClass.c I
	getstatic MPClass.a I
	getstatic MPClass.b I
	iadd
	getstatic MPClass.c I
	getstatic MPClass.a I
	iadd
	idiv
	i2f
	putstatic MPClass.fa F
	getstatic MPClass.fa F
	getstatic MPClass.a I
	i2f
	fadd
	getstatic MPClass.c I
	getstatic MPClass.b I
	iadd
	i2f
	fdiv
	putstatic MPClass.fb F
	getstatic MPClass.fa F
	getstatic MPClass.fb F
	fcmpl
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	istore_1
	iload_1
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 3
.limit locals 2
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
