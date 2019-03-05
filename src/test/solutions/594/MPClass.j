.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static i I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	putstatic MPClass.i I
Label4:
	getstatic MPClass.i I
	bipush 10
	if_icmpgt Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
	getstatic MPClass.i I
	iconst_5
	if_icmple Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label7
	goto Label3
	goto Label8
Label7:
Label8:
Label2:
	getstatic MPClass.i I
	iconst_1
	iadd
	putstatic MPClass.i I
	goto Label4
Label3:
	getstatic MPClass.i I
	invokestatic io/putIntLn(I)V
	iconst_0
	putstatic MPClass.i I
Label13:
	getstatic MPClass.i I
	bipush 100
	if_icmpgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label12
	getstatic MPClass.i I
	bipush 10
	if_icmplt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label16
	goto Label11
	goto Label17
Label16:
	getstatic MPClass.i I
	invokestatic io/putInt(I)V
Label17:
Label11:
	getstatic MPClass.i I
	iconst_1
	iadd
	putstatic MPClass.i I
	goto Label13
Label12:
Label1:
	return
.limit stack 4
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
