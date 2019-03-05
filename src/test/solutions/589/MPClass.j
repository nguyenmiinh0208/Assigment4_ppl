.source MPClass.java
.class public MPClass
.super java.lang.Object
.field static a I
.field static b I
.field static c I
.field static out Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic MPClass.a I
.var 1 is a I from Label2 to Label3
.var 2 is b I from Label2 to Label3
.var 3 is c I from Label2 to Label3
Label2:
	iconst_2
	istore_1
.var 4 is a I from Label4 to Label5
.var 5 is b I from Label4 to Label5
.var 6 is c I from Label4 to Label5
Label4:
	iconst_3
	istore 4
	iload 4
	invokestatic io/putInt(I)V
Label5:
Label3:
Label1:
	return
.limit stack 1
.limit locals 7
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
