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
	sipush 400
	i2f
	putstatic MPClass.c F
	getstatic MPClass.c F
	sipush 400
	i2f
	iconst_1
	i2f
	fdiv
	fcmpl
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label2
	ldc "chia het cho 4"
	invokestatic io/putString(Ljava/lang/String;)V
	goto Label3
Label2:
	getstatic MPClass.c F
	sipush 200
	i2f
	fcmpl
	ifne Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label6
	goto Label1
	goto Label7
Label6:
Label7:
Label3:
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
