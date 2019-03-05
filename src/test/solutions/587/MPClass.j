.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a F
.field static b F
.field static c F
.field static out Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	invokestatic MPClass/main1()V
	invokestatic MPClass/main2()V
	goto Label1
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public static main1()V
Label0:
	bipush 123
	invokestatic io/putInt(I)V
	goto Label1
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main2()V
Label0:
	sipush 1234
	invokestatic io/putInt(I)V
	goto Label1
Label1:
	return
.limit stack 1
.limit locals 0
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
