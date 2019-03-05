.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static k Ljava/lang/String;

.method public static testReturnString(IZ)Ljava/lang/String;
.var 0 is a I from Label0 to Label1
.var 1 is b Z from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	iload_1
	iconst_1
	if_icmpne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	ldc "Thanh cong"
	putstatic MPClass.k Ljava/lang/String;
	goto Label7
Label6:
	ldc "That bai"
	putstatic MPClass.k Ljava/lang/String;
Label7:
	goto Label3
Label2:
	ldc "ERROR"
	putstatic MPClass.k Ljava/lang/String;
Label3:
	getstatic MPClass.k Ljava/lang/String;
	goto Label1
Label1:
	areturn
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	iconst_1
	invokestatic MPClass/testReturnString(IZ)Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 3
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
