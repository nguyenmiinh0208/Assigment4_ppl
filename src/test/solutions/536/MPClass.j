.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static k Ljava/lang/String;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b F from Label0 to Label1
Label0:
	bipush 10
	istore_1
	ldc 10.5
	fstore_2
	iload_1
	i2f
	fload_2
	fcmpl
	ifge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	ldc "a nho hon b"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	goto Label3
Label2:
	ldc "a lon hon b"
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
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
