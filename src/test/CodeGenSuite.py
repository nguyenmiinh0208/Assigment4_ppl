import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_int(self):
    #     """Simple program: int main() {} """
    #     input = """procedure main(); begin putInt(100); end"""
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,500))
    # def test_int_ast(self):
    # 	input = Program([
    # 		FuncDecl(Id("main"),[],[],[
    # 			CallStmt(Id("putInt"),[IntLiteral(5)])])])
    # 	expect = "5"
    # 	self.assertTrue(TestCodeGen.test(input,expect,501))

    # def test_assgin(self):
    #     input = """var a:integer;
    #         procedure main();
    #         //var b: integer;
    #         begin
    #             a:=5;
    #             //b:=6;
    #             putInt(a);
    #             //putInt(b);
    #         end
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))

    # def test_assgin_local_variable(self):
    #     input = """
    #         procedure main();
    #         var b: integer;
    #         begin
    #             b:=6;
    #             putInt(b);
    #         end
    #     """
    #     expect = "6"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))
    
    # def test_assgin_local_variable1(self):
    #     input = """
    #         procedure foo();
    #         var a, b: integer;
    #         begin
    #             a := 5;
    #             b := 7;
    #             putIntLn(a);
    #             putInt(b); 
    #         end
    #         procedure main();
    #         begin
    #             foo();
    #         end
    #     """
    #     expect = "5\n7"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))

    # def test_parameter(self):
    #     input = """
    #         procedure foo(a, b: integer);
    #         begin
    #             putIntLn(a);
    #             putInt(b); 
    #         end
    #         procedure main();
    #         begin
    #             foo(5, 7);
    #         end
    #     """
    #     expect = "5\n7"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))

    # def test_float(self):
    #     input = """
    #         procedure main();
    #         begin
    #             putFloat(1.99);
    #         end
    #     """
    #     expect = "1.99"
    #     self.assertTrue(TestCodeGen.test(input,expect,506))      

    # def test_parameter_float(self):
    #     input = """
    #         procedure foo();
    #         var a,b: real;
    #         begin
    #             a := 0.5;
    #             b := 9.75;
    #             putFloatLn(a);
    #             putFloat(b); 
    #         end
    #         procedure main();
    #         begin
    #             foo();
    #         end
    #     """
    #     expect = "0.5\n9.75"
    #     self.assertTrue(TestCodeGen.test(input,expect,507))

    # def test_assign_int2float(self):
    #     input = """
    #         procedure foo();
    #         var a: real;
    #         begin
    #             a := 1;
    #             putFloat(a); 
    #         end
    #         procedure main();
    #         begin
    #             foo();
    #         end
    #     """
    #     expect = "1.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,508))

    # def test_binary_IntVsInt(self):
    #     input = """
    #         procedure main();
    #         begin
    #             putBool(3 > 2);
    #         end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,509))

    # def test_binary_floatVsfloat(self):
    #     input = """
    #         procedure main();
    #         begin
    #             putBool(3.5 > 2.0);
    #         end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,510))

    # def test_binary_floatVsInt(self):
    #     input = """
    #         procedure main();
    #         begin
    #             putBool(3.5 > 2);
    #         end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,511))

    # def test_binary_IntVsFloat(self):
    #     input = """
    #         procedure main();
    #         begin
    #             putBool(2 > 3.5);
    #         end
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,512))

    # def test_Binary_Add_F2F(self):
    #     input = """
    #         procedure main();
    #         begin
    #             putFloat(1.5 + 8.5);
    #         end
    #     """
    #     expect = "10.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,513))

    # def test_Binary_Add_I2I(self):
    #     input = """
    #         procedure main();
    #         begin
    #             putIntLn(2 + 8);
    #         end
    #     """
    #     expect = "10\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,514))

    # def test_Binary_Add_I2F(self):
    #     input = """
    #         procedure main();
    #         var a: integer;
    #             b: real;
    #         begin
    #             a := 5;
    #             b := 4.5;
    #             putFloat(a - b);
    #         end
    #     """
    #     expect = "0.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,515))

    # def test_Binary_Mul(self):
    #     input = """
    #         procedure main();
    #         var a: integer;
    #         begin
    #             a := 2;
    #             a := a*a*a*a*a;
    #             putInt(a);
    #         end
    #     """
    #     expect = "32"
    #     self.assertTrue(TestCodeGen.test(input,expect,516))

    # def test_Binary_div(self):
    #     input = """
    #         procedure main();
    #         var a: integer;
    #             b: integer;
    #         begin
    #             a := 3;
    #             b := 2;
    #             putFloat(a / b);
    #         end
    #     """
    #     expect = "1.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,517))

    # def test_Binary_MUL_IvsF(self):
    #     input = """
    #         procedure main();
    #         var a: integer;
    #             b: real;
    #         begin
    #             a := 4;
    #             b := 1.5;
    #             putFloat(a*b);
    #         end
    #     """
    #     expect = "6.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,518))

    # def test_Binary_Div(self):
    #     input = """
    #         procedure main();
    #         begin
    #             putFloat(3/2);
    #         end
    #     """
    #     expect = "1.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,519))      

    # def test_if(self):
    #     input = """
    #         procedure main();
    #         begin
    #             if (1 < 2) then putInt(0);
    #         end
    #     """
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input,expect,520))        

    # def test_if1(self):
    #     input = """
    #         procedure main();
    #         begin
    #             if (1 > 2) then putInt(0);
    #             else putInt(1);
    #         end
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,521))

    # def test_if2(self):
    #     input = """
    #         procedure main();
    #         var a: integer;
    #             b: real;
    #         begin
    #             a := 2;
    #             b := 1.5;
    #             if (a < b) then putIntLn(a);
    #             else putFloat(b);
    #         end
    #     """
    #     expect = "1.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,522))

    # def test_withStmt(self):
    #     input = """
    #         procedure main();
    #         var a: integer;
    #             b: real;
    #         begin
    #             a := 2;
    #             b := 1.5;
    #             with i,j: integer; do begin
    #                 i := 10;
    #                 j := 3;
    #                 if (i <> j) then i := i + a;
    #                 else j := j + a*2;
    #                 putInt(i-j);
    #             end
    #         end
    #     """
    #     expect = "9"
    #     self.assertTrue(TestCodeGen.test(input,expect,523))

    # def test_withStmt1(self):
    #     input = """
    #         procedure main();
    #         begin
    #             with i,j: integer; do begin
    #                 i := 10;
    #                 j := 3;
    #                 putInt(i - j);
    #             end
    #         end
    #     """
    #     expect = "7"
    #     self.assertTrue(TestCodeGen.test(input,expect,524))

    # def test_withStmt2(self):
    #     input = """
    #         procedure main();
    #         begin
    #             with i,j: integer; do begin
    #                 i := 10;
    #                 j := 3;
    #                 putIntLn(i - j);
    #             end
    #             With i: real; do begin
    #                 with j: real; do begin
    #                     i := 1.5;
    #                     j := 2.5;
    #                     putFloat(i - j);
    #                 end
    #             end
    #         end
    #     """
    #     expect = "7\n-1.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,525))

    # def test_IfStmt(self):
    #     input = """
    #         var a: integer;
    #             b: real;
    #         procedure testIf();
    #         begin
    #             a := 10;
    #             b := 9.98;
    #             if (a > b) then begin
    #                 if a >= 10 then a := a*a;
    #                 else b:= a - b;
    #                 putIntLn(a);
    #                 putFloat(b);
    #             end
    #         end
    #         procedure main();
    #         begin
    #             testIf();
    #         end
    #     """
    #     expect = "100\n9.98"
    #     self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_whileStmt(self):
        input = """
            var a, b: integer;
            procedure testWhile();
            begin
                a := 0;
                b := 5;
                while a < b do begin
                    putIntLn(a);
                    a := a + 1;
                end
            end
            procedure main();
            begin
                testWhile();
            end
        """
        expect = "0\n1\n2\n3\n4\n"
        self.assertTrue(TestCodeGen.test(input,expect,527))

    # def test_CallExpr(self):
    #     input = """
    #         function testCallExpr(a,b:real): real;
    #         begin
    #             return a+b+1.5;
    #         end
    #         procedure main();
    #         begin
    #             putFloat(testCallExpr(8,0.5));
    #         end
    #     """
    #     expect = "10.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,528))

    # def test_CallExpr1(self):
    #     input = """
    #         function testCallExpr(a: INTEGER): integer;
    #         begin
    #             return a + 1;
    #         end
    #         procedure main();
    #         begin
    #             putIntLn(testCallExpr(9));
    #         end
    #     """
    #     expect = "10\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,529))

    # def test_CallStmt1(self):
    #     input = """
    #         procedure testCallStmt(a: INTEGER; b, c:real);
    #         begin
    #             i := a + b + c;
    #             putFloat(i);
    #         end
    #         procedure main();
    #         begin
    #             testCallStmt(10, 1, 1.5);
    #         end
    #         var i: Real;
    #     """
    #     expect = "12.5"
    #     self.assertTrue(TestCodeGen.test(input,expect,530))

    # def test_CallExpr2(self):
    #     input = """
    #         function testCallExpr(a,b:real): real;
    #         begin
    #             return a+b+1.5;
    #         end
    #         procedure main();
    #         begin
    #             putFloat(testCallExpr(8,0.5));
    #         end
    #     """
    #     expect = "10.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,531))

    # def test_Bool(self):
    #     input = """
    #         procedure main();
    #         var a: boolean;
    #         begin
    #             a := true;
    #             putBool(a);
    #         end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,532))

    # def test_Bool1(self):
    #     input = """
    #         procedure main();
    #         begin
    #             putBool(false);
    #         end
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,533))

    # def test_Bool2(self):
    #     input = """
    #         procedure main();
    #         var isTrue: Boolean;
    #         begin
    #             isTrue := 2 > 3;
    #             putBool(isTrue);
    #         end
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,534))

    # def test_String(self):
    #     input = """
    #         procedure main();
    #         begin
    #             putString("Minhh");
    #         end
    #     """
    #     expect = "Minhh"
    #     self.assertTrue(TestCodeGen.test(input,expect,535))

    # def test_String1(self):
    #     input = """
    #         procedure main();
    #         var a: integer;
    #             b: real;
    #         begin
    #             a := 10;
    #             b := 10.5;
    #             if (a < b) then putStringLn("a nho hon b");
    #             else putStringLn("a lon hon b");
    #         end
    #         var k: String;
    #     """
    #     expect = "a nho hon b\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,536))

    # def test_String2(self):
    #     input = """
    #         procedure main();
    #         var a: String;
    #         begin
    #             a := "Nguyen Huu Minh";
    #             putStringLn(a);
    #         end
    #     """
    #     expect = "Nguyen Huu Minh\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,537))

    # def test_for_stmt(self):
    #     input = """
    #         procedure main();
    #         var i: integer;
    #         begin
    #             for i:=0 to 5 do begin
    #                 putInt(i);
    #                 //break;
    #             end
    #         end
    #     """
    #     expect = "012345"
    #     self.assertTrue(TestCodeGen.test(input,expect,538))

    # def test_CallExpr3(self):
    #     input = """
    #         procedure main();
    #         var i: integer;
    #         begin
    #            i := foo(5);
    #            putInt(i);
                
    #         end
    #         function foo(a:integer):integer;
    #         begin
    #             return a;
    #         end
    #     """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,539))

    # def test_for_stmt1(self):
    #     input = """
    #         procedure main();
    #         var i: integer;
    #         begin
    #             for i:=5 downto 0 do begin
    #                 putInt(i);
    #                 //break;
    #             end
    #         end
    #     """
    #     expect = "543210"
    #     self.assertTrue(TestCodeGen.test(input,expect,540))

    # def test_for_stmt2(self):
    #     input = """
    #         procedure main();
    #         var i, j: integer;
    #         begin
    #             for i:=0 to 2 do begin
    #                 for j:= i + 1 to 3 do begin
    #                     putInt(j);
    #                 end
    #                 putInt(i);
    #             end
    #         end
    #     """
    #     expect = "123023132"
    #     self.assertTrue(TestCodeGen.test(input,expect,541))

    # def test_CallExpr_returnString(self):
    #     input = """
    #         function testReturnString(a: integer; b:Boolean): String;
    #         begin
    #             if (a > 0) then 
    #                 if b = true then
    #                     k := "Thanh cong";
    #                 else k := "That bai";
    #             else k := "ERROR";
    #             return k;
    #         end
    #         procedure main();
    #         begin
    #             putString(testReturnString(1,true));
    #         end
    #         var k: String;
    #     """
    #     expect = "Thanh cong"
    #     self.assertTrue(TestCodeGen.test(input,expect,542))

    # def test_CallExpr_returnString1(self):
    #     input = """
    #         function testReturnString(): String;
    #         begin
    #             return "Minh";
    #         end
    #         procedure main();
    #         begin
    #             putString(testReturnString());
    #         end
    #     """
    #     expect = "Minh"
    #     self.assertTrue(TestCodeGen.test(input,expect,543))

    # def test_CallExpr_returnBool(self):
    #     input = """
    #         function testReturnBool(): Boolean;
    #         begin
    #             g := False;
    #             return g;
    #         end
    #         procedure main();
    #         begin
    #             putBool(testReturnBool());
    #         end
    #         var g: Boolean;
    #     """
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input,expect,544))

    # def test_CallExpr_returnBool1(self):
    #     input = """
    #         function testReturnBool(): Boolean;
    #         begin
    #             return true;
    #         end
    #         procedure main();
    #         begin
    #             putBool(testReturnBool());
    #         end
    #         var g: Boolean;
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,545))

    # def test_Unary(self):
    #     input = """
    #         procedure main();
    #         var a, b, c: integer;
    #         begin
    #             a := -2;
    #             b := -1;
    #             c := 3;
    #             putInt(a + b + c);
    #         end
    #     """
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input,expect,546))

    # def test_Unary1(self):
    #     input = """
    #         procedure main();
    #         var a, b, c: integer;
    #         begin
    #             a := -2;
    #             b := -1;
    #             c := 3;
    #             if -(a*b) < 0 then putString("Pass!");
    #             else putString("Failed :(");
    #         end
    #     """
    #     expect = "Pass!"
    #     self.assertTrue(TestCodeGen.test(input,expect,547))

    # def test_for_stmt3(self):
    #     input = """
    #     procedure main();
    #     var a, b, iSum:integer;
    #     begin
    #         iSum := 0;
    #         for a := 0 to 9 do
    #         begin
    #             if iSum > 27 then break;
    #             iSum := iSum + a;
    #         end
    #         putInt(iSum);
    #     end
    #     """
    #     expect = "28"
    #     self.assertTrue(TestCodeGen.test(input,expect,548))

    # def test_assign1(self):
    #     input = """
    #     procedure main();
    #     var a, b, iSum:integer;
    #     begin
    #         iSum := a := b := 0;
    #         putIntLn(iSum);
    #         putIntLn(a);
    #         putInt(b);
    #     end
    #     """
    #     expect = "0\n0\n0"
    #     self.assertTrue(TestCodeGen.test(input,expect,549))
    
    # def test_callStmt(self):
    #     input = """
    #     procedure main();
    #     begin
    #         putFloat(14.12);
    #         putLn();
    #         putFloat(15.05);
    #         return;
    #     end
    #     """
    #     expect = "14.12\n15.05"
    #     self.assertTrue(TestCodeGen.test(input,expect,550))

    # def test_forStmt(self):
    #     input = """
    #         procedure main();
    #         var i1, i2: integer;
    #         begin
    #             for i1:= 1 to 10 do begin
    #                 for i2:=1 to 10 do begin
    #                     putInt(i2);
    #                     if i2= i1 - 1 then continue;
    #                     end
    #                 If i1 = 3 then continue;
    #                 if i1 = 5 then break;
    #             end
    #             return;
    #         end
    #     """
    #     expect = "1234567891012345678910123456789101234567891012345678910"
    #     self.assertTrue(TestCodeGen.test(input,expect,551))

    # def test_forStmt2(self):
    #     input = """
    #         procedure main();
    #         var i1, i2: integer;
    #         begin
    #             i2:= 0;
    #             for i1 := 0 to 5 do begin
    #                 if i1 = 1 then continue;
    #                 i2 := i2 + i1;
    #             end
    #             putInt(i2);
    #         end
    #     """
    #     expect = "14"
    #     self.assertTrue(TestCodeGen.test(input,expect,552))

    # def test_float1(self):
    #     input = """
    #         procedure main(); 
    #         begin
    #             putFloat(1.4315E7);
    #         end
    #     """
    #     expect = "1.4315E7"
    #     self.assertTrue(TestCodeGen.test(input,expect,553))

    # def test_float2(self):
    #     input = """
    #         procedure main(); 
    #         begin
    #             putFloat(1.4315E7);
    #         end
    #     """
    #     expect = "1.4315E7"
    #     self.assertTrue(TestCodeGen.test(input,expect,554))

    # def test_if_bool(self):
    #     input = """
    #     procedure main();
    #     begin
    #         if (true)
    #             then putInt(1);
    #             else putInt(2);
    #     end
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,555))

    # def test_callStmt4(self):
    #     input = """ 
    #     procedure main();
    #     var a:integer;
    #     begin
    #         a := 4;
    #         putFloatLn(foo(a));
    #     end
    #     function foo(a:integer):real;
    #     var foo:integer;
    #     begin
    #         foo := 5;
    #         return foo + a;
    #     end 
    #     """
    #     expect = "9.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,556))

    # def test_Bool3(self):
    #     input = """
    #     var fNum:real;
    #     procedure main();
    #     var isT, isTrue:boolean;
    #     begin
    #         isT := false;
    #         isTrue := true;
    #         isT := isTrue;
    #         putBool(isT);
    #     end
    #     """
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input,expect,557))

    # def test_putBool(self):
    #     input = """
    #     procedure main();
    #     var a:real;
    #         b:integer;
    #         isTrue:boolean;
    #     begin
    #         a := 11.0;
    #         b := 11;
    #         isTrue := a <= b ;
    #         putBoolLn(isTrue);
    #     end"""
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,558))

    # def test_operator(self):
    #     input = """
    #     var a,b,c:integer;
    #         fa,fb,fc:real;
    #     procedure main();
    #     var isTrue:boolean;
    #     begin
    #         a := 1;
    #         b := a + 1;
    #         c := b mod 1;
    #         fa := (a + b) div (c + a);
    #         fb := (fa + a) / (c + b);
    #         fc := fa * fb / c;
    #         isTrue := fa <= fb;
    #         putBoolLn(isTrue);
    #     end
    #     """
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,559))
    
    # def test_operator1(self):
    #     input = """
    #     var a,b, c:integer;
    #         fa,fb:real;
    #     procedure main();
    #     var isTrue:boolean;
    #     begin
    #         a := 1;
    #         b := a + 1;
    #         c := b mod 1;
    #         fa := (a + b) div (c + a);
    #         fb := (fa + a) / (c + b);
    #         isTrue := fa <= fb;
    #         putBoolLn(isTrue);
    #     end
    #     """
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,560))

    # def test_compine_operator(self):
    #     input = """
    #     var a,b,c:integer;
    #         fa,fb,fc:real;
    #     procedure main();
    #     var isTrue, isT, isF:boolean;
    #     begin
    #         a := 10;
    #         b := a * 2;
    #         c := b div 7;
    #         fa := (a * b) - (c div a);
    #         fb := a * (fa + a) * (c - b);
    #         fc := fa * fb / c;
    #         isT := fa < fc;
    #         isF := fb >= fa;
    #         isTrue := isT=isF;
    #         putBoolLn(isTrue);
    #     end
    #     """
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,561))


    # def test_andthen4(self):
    #     input = """ procedure main(); 
    #                 begin 
    #                     a:=8;
    #                     b:=a/2 + 5;
    #                     if (false and then nhat(1)) 
    #                     then
    #                         a:=7;
    #                     else putInt(5);
    #                 end
    #                 function nhat(v:integer):boolean;                                       
    #                 begin                        
    #                     putInt(v);
    #                     return true;                        
    #                 end                    
    #                 var a:integer; b: real;
    #                 var x:boolean;                                   
    #             """
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input,expect,562))

    # def test_returnBool(self):
    #     input = """ function isprime(n:integer):boolean;
    #                 var flag:boolean;
    #                  id,i:integer;
    #                 begin
    #                    if (n=1) or (n=0)  then return False;
    #                    if ( n=2) or (n= 3) then return True;
    #                    flag:=True;
    #                    for i:=2 to n div 2 do
    #                         if  n-(n div i)*i =0 then
    #                         begin
    #                             id:=False;
    #                             break;
    #                         end
    #                     return flag;
    #                 end
    #                 procedure main();
    #                 begin
    #                     putBoolLn(isprime(1));
    #                 	putBoolLn(isprime(2));
    #                 end                           
    #             """
    #     expect = "false\ntrue\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,563))

    # def test_compine_operator1(self):
    #     input = """
    #             var a,b,c: integer;
    #             function foo(i: integer): boolean;
    #             begin
    #                 a := a + i;
    #                 return i >= 5;
    #             end
    #             procedure main();
    #             var x: boolean;
    #             begin
    #                 a := 0;
    #                 putBoolLn(((foo(1) or foo(2)) or foo(3)) or foo(7));
    #             end                      
    #             """
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,564))

    # def test_compine_operator2(self):
    #     input = """
    #             var a,b,c: integer;
    #             function foo(i: integer): boolean;
    #             begin
    #                 a := a + i;
    #                 return i >= 5;
    #             end
    #             procedure main();
    #             var x: boolean;
    #             begin
    #                 a := 0;
    #                 putBoolLn(((foo(1) or else foo(2)) or else foo(3)) or else foo(4));
    #             end                      
    #             """
    #     expect = "false\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,565))

    # def test_compine_operator3(self):
    #     input = """
    #             var a,b,c: boolean;
    #             procedure main();
    #             var x: boolean;
    #             begin
    #                 x := True;
    #                 a := False;
    #                 b := False;
    #                 c := True;
    #                 putBoolLn(((a or else x) or else b) or else c);
    #             end                      
    #             """
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,566))

    # def test_compine_operator4(self):
    #     input = """
    #             function foo(i: integer): boolean;
    #             begin
    #                 return i >= 5;
    #             end
    #             procedure main();
    #             begin
    #                 putBoolLn(foo(1) or else foo(5));
    #             end                      
    #             """
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,567))

    # def test_callStmt5(self):
    #     input = """
    #     procedure main();
    #     var a:integer;
    #     begin
    #         a := 1;
    #         test(a);
    #     end
    #     procedure test(a:integer);
    #     begin
    #         putInt(a);
    #     end
    #     """
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input,expect,568))

    # def test_ifElse_stmt(self):
    #     input = """
    #     procedure main();
    #     var a:integer;
    #     begin
    #         a := 2;
    #         if a > 5
    #             then a := 10;
    #             else a := 11;
    #         putInt(a);
    #     end
    #     """
    #     expect = "11"
    #     self.assertTrue(TestCodeGen.test(input,expect,569))

    # def test_isElse_stmt1(self):
    #     input = """
    #     procedure main();
    #     var a:integer;
    #     begin
    #         a := 2;
    #         if a > 5 
    #         then
    #             if a mod 2=0
    #             then 
    #                 a := a * 2;
    #             else
    #                 begin
    #                 end
    #         else 
    #         begin
    #             a := 11;
    #             if a mod 3 <> 0 then a := a * 3;
    #         end
    #         putInt(a);
    #     end
    #     """
    #     expect = "33"
    #     self.assertTrue(TestCodeGen.test(input,expect,570))

    # def test_ifelse_stmt3(self):
    #     input = """
    #     procedure main();
    #     var a:integer;
    #     begin
    #         a := 2;
    #         if a > 5 then
    #             if a mod 2=0 then
    #                 a := a * 2;
    #             else
    #             begin
    #             end
    #         else begin
    #             a := 11;
    #             if a mod 3 <> 0 then
    #                 a := a * 3 div 2;
    #         end
    #         putInt(a);
    #     end
    #     """
    #     expect = "16"
    #     self.assertTrue(TestCodeGen.test(input,expect,571))

    # def test_whileStmt1(self):
    #     input = """
    #     procedure main();
    #     var a, iSum:integer;
    #     begin
    #         a := 0;
    #         iSum := 0;
    #         while a < 20 do
    #         begin
    #             a := a + 1;
    #             if a mod 2=0 then continue;
    #             iSum := iSum + a;
    #         end
    #         putInt(iSum);
    #     end
    #     """
    #     expect = "100"
    #     self.assertTrue(TestCodeGen.test(input,expect,572))

    # def test_whileStmt3(self):
    #     input = """
    #     procedure main();
    #     var a, iSum:integer;
    #     begin
    #         a := 0;
    #         iSum := 0;
    #         while a < 20 do
    #         begin
    #             a := a + 1;
    #             if a > 17 then break;
    #             iSum := iSum + a;
    #         end
    #         putInt(iSum);
    #     end
    #     """
    #     expect = "153"
    #     self.assertTrue(TestCodeGen.test(input,expect,573))

    # def test_whileStmt4(self):
    #     input = """
    #     procedure main();
    #     var a, b, iSum:integer;
    #     begin
    #         a := b := iSum := 0;
    #         while a < 20 do
    #         begin
    #             b := 0;
    #             a := a + 1;
    #             while b < a do
    #             begin
    #                 b := b + 1;
    #                 iSum := iSum + b;
    #             end
    #             iSum := iSum + a;
    #         end
    #         putInt(iSum);
    #     end
    #     """
    #     expect = "1750"
    #     self.assertTrue(TestCodeGen.test(input,expect,574))

    # def test_whileStmt5(self):
    #     input = """
    #     procedure main();
    #     var a, b, iSum:integer;
    #     begin
    #         a := b := iSum := 0;
    #         while a < 20 do
    #         begin
    #             b := 0;
    #             a := a + 1;
    #             while b < a do
    #             begin
    #                 b := b + 1;
    #                 if b > 10 then break;
    #                 if b mod 2=1 then continue;
    #                 iSum := iSum + b;
    #             end
    #             if a mod b=0 then continue;
    #             if a + b > 40 then break;
    #             iSum := iSum + a;
    #         end
    #         putInt(iSum);
    #     end
    #     """
    #     expect = "554"
    #     self.assertTrue(TestCodeGen.test(input,expect,575))

    # def test_forStmt4(self):
    #     input = """
    #     procedure main();
    #     var a, b, iSum:integer;
    #     begin
    #         iSum := 0;
    #         for a := 0 to 9 do
    #         begin
    #             if a mod 2=0 then continue;
    #             iSum := iSum + a;
    #         end
    #         putInt(iSum);
    #     end
    #     """
    #     expect = "25"
    #     self.assertTrue(TestCodeGen.test(input,expect,576))

    # def test_forStmt5(self):
    #     input = """
    #     procedure main();
    #     var a, b, iSum:integer;
    #     begin
    #         iSum := 0;
    #         for a := 0 to 9 do
    #         begin
    #             if iSum > 27 then break;
    #             iSum := iSum + a;
    #         end
    #         putInt(iSum);
    #     end
    #     """
    #     expect = "28"
    #     self.assertTrue(TestCodeGen.test(input,expect,577))

    # def test_withDoStmt(self):
    #     input = """
    #     var i, j:integer;
    #     procedure main();
    #     var a, b, iSum:integer;
    #     begin
    #         i := 10;
    #         with i:real; do
    #         begin
    #             i := 11.8;
    #             putFloat(i);
    #         end
    #         i := 11;
    #         putIntLn(i);
    #     end
    #     """
    #     expect = "11.811\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,578))

    # def test_withDostmt1(self):
    #     input = """
    #     var i, j:integer;
    #     procedure main();
    #     var a, b, iSum:integer;
    #     begin
    #         i := 10;
    #         with i:real; do
    #         begin
    #             i := 14.3;
    #             with i:integer; do
    #             begin
    #                 i := 19;
    #                 putInt(i);
    #             end
    #             putFloat(i);
    #         end
    #         putInt(i);
    #     end
    #     """
    #     expect = "1914.310" 
    #     self.assertTrue(TestCodeGen.test(input,expect,579))

    # def test_callStmt2(self):
    #     input = """
    #     var a:integer;
    #     procedure main();
    #     var b:integer;
    #         c:real;
    #     begin
    #         b := 5;
    #         c := foo(b);
    #         putFloat(c);
    #     end
        
    #     function foo(a:integer):integer;
    #     begin
    #         return a * a;
    #     end
    #     """
    #     expect = "25.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,580))

    # def test_compine_operator5(self):
    #     input = """
    #     var a,b,c:integer;
    #         fa,fb,fc:real;
    #     procedure main();
    #     var isTrue, isT, isF:boolean;
    #     begin
    #         a := 10;
    #         b := a * 2;
    #         c := b div 7;
    #         fa := (a * b) - (c div a);
    #         fb := a * (fa + a) * (c - b);
    #         fc := fa * fb / c;
    #         isT := fa < fc;
    #         isF := fb >= fa;
    #         isTrue := isT=isF;
    #         putBoolLn(isTrue);
    #     end
    #     """
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,581))

    # def test_ifElse_stmt2(self):
    #     input = """
    #     procedure main();
    #     var a:integer;
    #     begin
    #         a := 1;
    #         if a > 1
    #             then a := 10;
    #         putIntLn(a);
    #     end
    #     """
    #     expect = "1\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,582))

    # def test_callExpr_return(self):
    #     input = """
    #     var a:integer;
    #     procedure main();
    #     var b:integer;
    #         c:real;
    #     begin
    #         b := 5;
    #         c := foo(b);
    #         putFloat(c);
    #     end
        
    #     function foo(a:integer):integer;
    #     begin
    #         return a * a;
    #     end
    #     """
    #     expect = "25.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,583))

    # def test_andthen_orlse(self):
    #     input = """
	# 			procedure main();
	# 			var b: boolean; a:integer; c:real; d:string;
	# 			begin
	# 				if 2.0 >= 1 and then 1 >= 2 or else 2.0 = 2.0 then
	# 				begin
	# 					d := "enter 1";
	# 					if true or else false and then 2 <> 1 then 
	# 					begin
	# 						d := "enter 2";
	# 					end
	# 				end
	# 				else
	# 					d := "This is false";
	# 				putString(d);
	# 			end
	# 		"""
    #     expect = "enter 2"
    #     self.assertTrue(TestCodeGen.test(input,expect,584))

    # def test_return(self):
    #     input = """
    #     var a ,b,c: real; out:boolean;
    #     procedure main();
	# 	begin  
    #            if true then
    #                  return;
    #     end   
	
	# 	"""
    #     expect = """"""
    #     self.assertTrue(TestCodeGen.test(input,expect,585)) 

    # def test_ifelse(self):
    #     input = """
    #     var a ,b,c: real; out:boolean;
    #     procedure main();
	# 	begin  
    #     c:=400;
    #             if c=400/1 then putString("chia het cho 4");
    #             else if c = 200 then return;
    #     end   
	# 	"""
    #     expect = """chia het cho 4"""
    #     self.assertTrue(TestCodeGen.test(input,expect,586))

    # def test_callStmt6(self):
    #     input = """
    #     var a ,b,c: real; out:boolean;	
    #     procedure main();
	# 	begin  
    #              main1();
    #              main2();
    #                  return;
    #     end   
	# 	procedure main1();
	# 	begin  
    #              putInt(123);
    #                  return;
    #     end
    #     procedure main2();
	# 	begin  
    #              putInt(1234);
    #                  return;
    #     end
	# 	"""
    #     expect = "1231234"
    #     self.assertTrue(TestCodeGen.test(input,expect,587))

    # def test_forStmt6(self):
    #     input = """
	# 	procedure main();
	# 	var a ,b: integer;
	# 	begin
	# 		for a:=10 downto 1 do
	# 			putInt(a);
    #     end
	# 	"""
    #     expect = "10987654321"
    #     self.assertTrue(TestCodeGen.test(input,expect,588))

    # def test_withDoStmt2(self):
    #     input = """
    #     var a ,b,c: integer; out:boolean;
	# 	procedure main();
	# 	begin
    #     a:=1;
	# 		  with a ,b,c: integer; do 
    #           begin a:=2; with a,b,c: integer; do begin a:=3; putInt(a);end end
    #     end
	# 	"""
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input,expect,589))

    # def test_withDoStmt4(self):
    #     input = """
    #     var a ,b,c: integer; out:boolean;
	# 	procedure main();
	# 	 var a ,b,c: integer; out:boolean;
	# 	begin
    #     a:=1;
    #           for b:=1 to 3 do
	# 		  with a ,b,c: integer; do 
    #           begin 
    #             a:=2; 
    #             b:=3; 
    #             putInt(a+b); 
    #           end
    #     end
		
	# 	"""
    #     expect = """555"""
    #     self.assertTrue(TestCodeGen.test(input,expect,590))

    # def test_CallExpr5(self):
    #     input = """
    #     var a ,b,c: real; out:boolean;
	# 	function foo(c:real): real;
    #     begin return 1.2;return 1.3; end
    #     procedure main();
	# 	begin
    #             c:=a:=foo(1)+foo(foo(foo(foo(foo(1)))));
    #             putFloatLn(c/2);
    #             putFloatLn(a/2);
    #     end
	# 	"""
    #     expect = "1.2\n1.2\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,591))

    # def test_callStmt7(self):
    #     input = """
    #     var a : real;
	# 	function foo(b:integer): real;
    #     begin return b; end
    #     procedure main();
	# 	begin
    #         a := foo(5);
    #         putFloat(a);
    #     end
	# 	"""
    #     expect = "5.0"
    #     self.assertTrue(TestCodeGen.test(input,expect,592))

    # def test_assign(self):
    #     input = """
    #     var globalInt:integer;
    #     globalFloat:real;
    #     globalBool:boolean;
    #     procedure main();
    #     var localInt:integer;
    #     localFloat:real;
    #     localBool:boolean;
    #     begin
    #         globalInt := localInt := 0;
    #         globalFloat := localFloat := 1;
    #         localBool := globalBool := not not not true;
    #         putIntLn(globalInt);
    #         putIntLn(localInt);
    #         putFloatLn(globalFloat);
    #         putFloatLn(localFloat);
    #         putBoolLn(localBool);
    #         putBoolLn(globalBool);
    #     end
    #     """
    #     expect = "0\n0\n1.0\n1.0\nfalse\nfalse\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 593))

    # def test_break_continue(self):
    #     input = """
    #     var i:integer;
    #     procedure main();
    #     begin
    #         for i:= 0 to 10 do
    #             if i > 5 then break;
    #         putIntLn(i);
    #         for i:= 0 to 100 do
    #         begin
    #             if i >= 10 then continue;
    #             else putInt(i);
    #         end
    #     end
    #     """
    #     expect = "6\n0123456789"
    #     self.assertTrue(TestCodeGen.test(input, expect, 594))

    # def test_For_Continue(self):
    #     input = """
    #         procedure main();
    #         var i : integer;
    #             S : integer;
    #         begin
    #             S :=0;
    #             for i := 1 to 10 do
    #                 begin
    #                     if (S =10) then continue;
    #                     S := S + i;
    #                 end
    #             putInt(S);
    #         end
    #     """
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input,expect,595))

    # def test_For_If_Else(self):
    #     input = """
    #         procedure main();
    #         var i : integer;
    #             S1,S2 : integer;
    #         begin
    #             S1 :=0;
    #             S2 :=0;
    #             for i := 1 to 10 do
    #                 if (i mod 2 = 0) then S1 := S1 + i;
    #                 else S2 := S2 + i;
    #             putIntLn(S1);
    #             putInt(S2);
    #         end
    #     """
    #     expect = "30\n25"
    #     self.assertTrue(TestCodeGen.test(input,expect,596))

    # def test_For_DownTo(self):
    #     input = """
    #         procedure main();
    #         var i : integer;
    #             S : integer;
    #         begin
    #             S :=0;
    #             for i := 10 downto 1 do
    #                 S := S + i;
    #             putIntLn(S);
    #             putInt(i);
    #         end
    #     """
    #     expect = "55\n0"
    #     self.assertTrue(TestCodeGen.test(input,expect,597))

    # def test_comnbine_exp(self):
    #     input = """
    #     procedure main();
    #     begin
    #         putBool(1-1 = 0);
    #         putBool(not (1 > 2));
    #         putBoolLn(1.*1 <> 1/1);
    #         putBoolLn(1 div 1 <> 1*1);
    #         putFloatLn(1.*1);
    #         putFloatLn(1/1);
    #     end
	# 	"""
    #     expect = "truetruefalse\nfalse\n1.0\n1.0\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 598))

    # def test_combine_exp1(self):
    #     input = """
    #     procedure main();
    #     begin
    #         putBoolLn(T());
    #         putBoolLn(F());
    #         putBoolLn(T() and then foo());
    #         putBoolLn(F() and then foo());
    #     end
    #     function T():boolean;
    #     begin
    #         return TRUE;
    #     end
    #     function F():boolean;
    #     begin
    #         return FALSE;
    #     end
    #     function foo():boolean;
    #     begin
    #         putString("FOO!");
    #         return false;
    #     end
    #     """
    #     expect = "true\nfalse\nFOO!false\nfalse\n"
    #     self.assertTrue(TestCodeGen.test(input, expect, 599))