.source MPClass.java
.class public MPClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b Z from Label0 to Label1
.var 2 is a I from Label0 to Label1
.var 3 is c F from Label0 to Label1
.var 4 is d Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 2.0
	iconst_1
	i2f
	fcmpl
	iflt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label8
	iconst_1
	iconst_1
	iconst_2
	if_icmplt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iand
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label12
	iconst_0
	ldc 2.0
	ldc 2.0
	fcmpl
	ifne Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ior
	goto Label13
Label12:
	iconst_1
Label13:
	ifle Label2
	ldc "enter 1"
	astore 4
	iconst_1
	ifgt Label16
	iconst_0
	iconst_0
	ior
	goto Label17
Label16:
	iconst_1
Label17:
	ifle Label20
	iconst_1
	iconst_2
	iconst_1
	if_icmpeq Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	iand
	goto Label21
Label20:
	iconst_0
Label21:
	ifle Label14
	ldc "enter 2"
	astore 4
	goto Label15
Label14:
Label15:
	goto Label3
Label2:
	ldc "This is false"
	astore 4
Label3:
	aload 4
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 15
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
