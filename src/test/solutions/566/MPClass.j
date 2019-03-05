.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a Z
.field static b Z
.field static c Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_0
	putstatic MPClass.a Z
	iconst_0
	putstatic MPClass.b Z
	iconst_1
	putstatic MPClass.c Z
	getstatic MPClass.a Z
	ifgt Label2
	iconst_0
	iload_1
	ior
	goto Label3
Label2:
	iconst_1
Label3:
	ifgt Label4
	iconst_0
	getstatic MPClass.b Z
	ior
	goto Label5
Label4:
	iconst_1
Label5:
	ifgt Label6
	iconst_0
	getstatic MPClass.c Z
	ior
	goto Label7
Label6:
	iconst_1
Label7:
	invokestatic io/putBoolLn(Z)V
Label1:
	return
.limit stack 14
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
