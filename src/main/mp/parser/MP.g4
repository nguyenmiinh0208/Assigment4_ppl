/*
Ngo Tuan Dat
MSSV 1610644
*/
grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];

program : one_Dec+ EOF;

one_Dec : var_dec 
         | fun_dec 
         | proce_dec ;

//variable declaration

var_dec : VAR variable+ ; 

variable : ID (COMMA ID)* COLON (type_D|array) SEMI ;

type_D : INTTYPE 
       | REALTYPE 
       | STRINGTYPE 
       | BOOLEAN ;
array : ARRAY LSB subop1? INTLIT DOUDOT subop2? INTLIT RSB OF type_D;
subop1: SUBOP ;
subop2: SUBOP ;
//function declaration
fun_dec : FUNCTION ID LB paramList RB COLON (type_D|array) SEMI var_dec? compound ;

paramList : param (SEMI param)* |  ;

param : ID (COMMA ID)* COLON (type_D|array) ;

compound : BEGIN statement* END ;

statement : assignment 
          | if_stmt 
          | for_stmt 
          | while_stmt 
          | br_stmt
          |continue_stmt
          | return_stmt 
          | compound 
          | funcall
          | with_stmt;
assignment: (lhs CEOP )+ exp SEMI;
lhs: ID|exp_id;
CEOP: ':=';
ADDOP : '+' ;
SUBOP : '-' ;
MULOP : '*' ;
DIVOP : '/' ;
MODOP : M O D ;
EQUOP : '=' ;
MTOP : '>';
MTEOP : '>=' ;
LTOP : '<' ;
LTEOP : '<=' ;
ANDOP : A N D ;
OROP : O R ;
NEOP : '<>' ;
NOTOP : N O T;
DIV: D I V;

exp : exp (andthenop|orelseop)exp1 |exp1 ;

andthenop : ANDOP THEN;

orelseop : OROP ELSE ;

exp1 : exp2 (EQUOP|NEOP|MTOP|MTEOP|LTOP|LTEOP) exp2 | exp2;

exp2 : exp2 (ADDOP|SUBOP|OROP) exp3 | exp3;

exp3 : exp3 (DIVOP|MULOP|DIV|MODOP|ANDOP) exp4| exp4;

exp4 : (SUBOP|NOTOP) exp4 | operand;

operand : operand2 | exp_id;

operand2 : INTLIT|FLOATLIT|STRINGLIT|BOOLLIT|ID|call| LB exp RB;

exp_id : operand2 LSB exp RSB | exp_id LSB exp RSB;

if_stmt: IF exp THEN statement (ELSE statement)?;

for_stmt: FOR ID CEOP exp (TO|DOWNTO) exp DO statement;
FOR : F O R;
TO : T O;
DOWNTO : D O W N T O;

while_stmt: WHILE exp DO statement;

br_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

with_stmt: WITH variable+ DO statement;

return_stmt: RETURN exp? SEMI;

funcall: call SEMI;

call: ID LB manyexp RB;

manyexp: (exp (COMMA exp)*)|;

//procedure declaration

proce_dec : PROCEDURE ID LB paramList RB SEMI var_dec? compound ;





INTTYPE : I N T E G E R;

VOIDTYPE : V O I D;

REALTYPE : R E A L;

STRINGTYPE : S T R I N G;

BOOLEAN : B O O L  E A N;

BREAK : B R E A K;

CONTINUE : C O N T I N U E;

DO : D O;

WHILE : W H I L E;

IF : I F;

ELSE : E L S E;

RETURN : R E T U R N;

THEN : T H E N;

BEGIN : B E G I N;

END : E N D;

FUNCTION : F U N C T I O N;

PROCEDURE : P R O C E D U R E;

VAR : V A R;

ARRAY : A R R A Y ;

OF : O F;

WITH: W I T H;

TRADITIONAL_BLOCK : '(*' .*? '*)' -> skip ;

BLOCK_COMMENT : '{' .*? '}' -> skip;

LINE_COMMENT : '//' .*? ~[\r\n]* -> skip;

BOOLLIT : (T R U E) | (F A L S E) ;

ID : [a-zA-Z_][a-zA-Z0-9_]* ;
 
COMMA : ',' ;

DOUDOT : '..' ;

COLON : ':' ;

SEMI : ';' ;

LSB : '[' ; 

RSB : ']' ;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

INTLIT : [0-9]+ ;
//
fragment Real1 : [0-9]+[eE]'-'?[0-9]+;
FLOATLIT : (  Real1 | ([0-9]+'.'(Real1 |([0-9]+))?)  | '.'Real1 |'.'[0-9]+) ;
//

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

STRINGLIT : '"'.*?~[\b\f\r\n\t'"\\]*'"'
{ 
s = self.text[1:-1]
self.text = s
} ;
UNCLOSE_STRING : '"' (~[\b\f\r\n\t'"\\] | '\\' [bfrnt'"\\])* { raise UncloseString(self.text[1:]) }; 

ILLEGAL_ESCAPE : '"' (~[\b\f\r\n\t'"\\] | '\\' [bfrnt'"\\])* '\\' ~[bfrnt'"\\] { raise IllegalEscape(self.text[1:]) } ;

ERROR_CHAR : . { raise ErrorToken(self.text[0:]) };