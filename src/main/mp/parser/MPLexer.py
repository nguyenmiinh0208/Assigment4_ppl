# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u0251\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\39\39\39")
        buf.write("\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3<\3<\3<\3")
        buf.write("<\3<\3<\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3>\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3")
        buf.write("B\3B\3B\3C\3C\3C\3C\3C\3D\3D\3D\3D\7D\u01a5\nD\fD\16D")
        buf.write("\u01a8\13D\3D\3D\3D\3D\3D\3E\3E\7E\u01b1\nE\fE\16E\u01b4")
        buf.write("\13E\3E\3E\3E\3E\3F\3F\3F\3F\7F\u01be\nF\fF\16F\u01c1")
        buf.write("\13F\3F\7F\u01c4\nF\fF\16F\u01c7\13F\3F\3F\3G\3G\3G\3")
        buf.write("G\3G\3G\3G\3G\3G\3G\3G\5G\u01d6\nG\3H\3H\7H\u01da\nH\f")
        buf.write("H\16H\u01dd\13H\3I\3I\3J\3J\3J\3K\3K\3L\3L\3M\3M\3N\3")
        buf.write("N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\6S\u01f5\nS\rS\16S\u01f6")
        buf.write("\3T\6T\u01fa\nT\rT\16T\u01fb\3T\3T\5T\u0200\nT\3T\6T\u0203")
        buf.write("\nT\rT\16T\u0204\3U\3U\6U\u0209\nU\rU\16U\u020a\3U\3U")
        buf.write("\3U\6U\u0210\nU\rU\16U\u0211\5U\u0214\nU\3U\3U\3U\3U\6")
        buf.write("U\u021a\nU\rU\16U\u021b\5U\u021e\nU\3V\6V\u0221\nV\rV")
        buf.write("\16V\u0222\3V\3V\3W\3W\7W\u0229\nW\fW\16W\u022c\13W\3")
        buf.write("W\7W\u022f\nW\fW\16W\u0232\13W\3W\3W\3W\3X\3X\3X\3X\7")
        buf.write("X\u023b\nX\fX\16X\u023e\13X\3X\3X\3Y\3Y\3Y\3Y\7Y\u0246")
        buf.write("\nY\fY\16Y\u0249\13Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\6\u01a6\u01b2")
        buf.write("\u01bf\u022a\2[\3\2\5\2\7\2\t\2\13\2\r\2\17\2\21\2\23")
        buf.write("\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2")
        buf.write("/\2\61\2\63\2\65\2\67\39\4;\5=\6?\7A\bC\tE\nG\13I\fK\r")
        buf.write("M\16O\17Q\20S\21U\22W\23Y\24[\25]\26_\27a\30c\31e\32g")
        buf.write("\33i\34k\35m\36o\37q s!u\"w#y${%}&\177\'\u0081(\u0083")
        buf.write(")\u0085*\u0087+\u0089,\u008b-\u008d.\u008f/\u0091\60\u0093")
        buf.write("\61\u0095\62\u0097\63\u0099\64\u009b\65\u009d\66\u009f")
        buf.write("\67\u00a18\u00a39\u00a5:\u00a7\2\u00a9;\u00ab<\u00ad=")
        buf.write("\u00af>\u00b1?\u00b3@\3\2#\4\2CCcc\4\2DDdd\4\2EEee\4\2")
        buf.write("FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4")
        buf.write("\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSs")
        buf.write("s\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2")
        buf.write("ZZzz\4\2[[{{\4\2\\\\||\4\2\f\f\17\17\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\7\2\n\f\16\17$$))")
        buf.write("^^\n\2$$))^^ddhhppttvv\2\u024e\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a9\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1")
        buf.write("\3\2\2\2\2\u00b3\3\2\2\2\3\u00b5\3\2\2\2\5\u00b7\3\2\2")
        buf.write("\2\7\u00b9\3\2\2\2\t\u00bb\3\2\2\2\13\u00bd\3\2\2\2\r")
        buf.write("\u00bf\3\2\2\2\17\u00c1\3\2\2\2\21\u00c3\3\2\2\2\23\u00c5")
        buf.write("\3\2\2\2\25\u00c7\3\2\2\2\27\u00c9\3\2\2\2\31\u00cb\3")
        buf.write("\2\2\2\33\u00cd\3\2\2\2\35\u00cf\3\2\2\2\37\u00d1\3\2")
        buf.write("\2\2!\u00d3\3\2\2\2#\u00d5\3\2\2\2%\u00d7\3\2\2\2\'\u00d9")
        buf.write("\3\2\2\2)\u00db\3\2\2\2+\u00dd\3\2\2\2-\u00df\3\2\2\2")
        buf.write("/\u00e1\3\2\2\2\61\u00e3\3\2\2\2\63\u00e5\3\2\2\2\65\u00e7")
        buf.write("\3\2\2\2\67\u00e9\3\2\2\29\u00ec\3\2\2\2;\u00ee\3\2\2")
        buf.write("\2=\u00f0\3\2\2\2?\u00f2\3\2\2\2A\u00f4\3\2\2\2C\u00f8")
        buf.write("\3\2\2\2E\u00fa\3\2\2\2G\u00fc\3\2\2\2I\u00ff\3\2\2\2")
        buf.write("K\u0101\3\2\2\2M\u0104\3\2\2\2O\u0108\3\2\2\2Q\u010b\3")
        buf.write("\2\2\2S\u010e\3\2\2\2U\u0112\3\2\2\2W\u0116\3\2\2\2Y\u011a")
        buf.write("\3\2\2\2[\u011d\3\2\2\2]\u0124\3\2\2\2_\u012c\3\2\2\2")
        buf.write("a\u0131\3\2\2\2c\u0136\3\2\2\2e\u013d\3\2\2\2g\u0145\3")
        buf.write("\2\2\2i\u014b\3\2\2\2k\u0154\3\2\2\2m\u0157\3\2\2\2o\u015d")
        buf.write("\3\2\2\2q\u0160\3\2\2\2s\u0165\3\2\2\2u\u016c\3\2\2\2")
        buf.write("w\u0171\3\2\2\2y\u0177\3\2\2\2{\u017b\3\2\2\2}\u0184\3")
        buf.write("\2\2\2\177\u018e\3\2\2\2\u0081\u0192\3\2\2\2\u0083\u0198")
        buf.write("\3\2\2\2\u0085\u019b\3\2\2\2\u0087\u01a0\3\2\2\2\u0089")
        buf.write("\u01ae\3\2\2\2\u008b\u01b9\3\2\2\2\u008d\u01d5\3\2\2\2")
        buf.write("\u008f\u01d7\3\2\2\2\u0091\u01de\3\2\2\2\u0093\u01e0\3")
        buf.write("\2\2\2\u0095\u01e3\3\2\2\2\u0097\u01e5\3\2\2\2\u0099\u01e7")
        buf.write("\3\2\2\2\u009b\u01e9\3\2\2\2\u009d\u01eb\3\2\2\2\u009f")
        buf.write("\u01ed\3\2\2\2\u00a1\u01ef\3\2\2\2\u00a3\u01f1\3\2\2\2")
        buf.write("\u00a5\u01f4\3\2\2\2\u00a7\u01f9\3\2\2\2\u00a9\u021d\3")
        buf.write("\2\2\2\u00ab\u0220\3\2\2\2\u00ad\u0226\3\2\2\2\u00af\u0236")
        buf.write("\3\2\2\2\u00b1\u0241\3\2\2\2\u00b3\u024e\3\2\2\2\u00b5")
        buf.write("\u00b6\t\2\2\2\u00b6\4\3\2\2\2\u00b7\u00b8\t\3\2\2\u00b8")
        buf.write("\6\3\2\2\2\u00b9\u00ba\t\4\2\2\u00ba\b\3\2\2\2\u00bb\u00bc")
        buf.write("\t\5\2\2\u00bc\n\3\2\2\2\u00bd\u00be\t\6\2\2\u00be\f\3")
        buf.write("\2\2\2\u00bf\u00c0\t\7\2\2\u00c0\16\3\2\2\2\u00c1\u00c2")
        buf.write("\t\b\2\2\u00c2\20\3\2\2\2\u00c3\u00c4\t\t\2\2\u00c4\22")
        buf.write("\3\2\2\2\u00c5\u00c6\t\n\2\2\u00c6\24\3\2\2\2\u00c7\u00c8")
        buf.write("\t\13\2\2\u00c8\26\3\2\2\2\u00c9\u00ca\t\f\2\2\u00ca\30")
        buf.write("\3\2\2\2\u00cb\u00cc\t\r\2\2\u00cc\32\3\2\2\2\u00cd\u00ce")
        buf.write("\t\16\2\2\u00ce\34\3\2\2\2\u00cf\u00d0\t\17\2\2\u00d0")
        buf.write("\36\3\2\2\2\u00d1\u00d2\t\20\2\2\u00d2 \3\2\2\2\u00d3")
        buf.write("\u00d4\t\21\2\2\u00d4\"\3\2\2\2\u00d5\u00d6\t\22\2\2\u00d6")
        buf.write("$\3\2\2\2\u00d7\u00d8\t\23\2\2\u00d8&\3\2\2\2\u00d9\u00da")
        buf.write("\t\24\2\2\u00da(\3\2\2\2\u00db\u00dc\t\25\2\2\u00dc*\3")
        buf.write("\2\2\2\u00dd\u00de\t\26\2\2\u00de,\3\2\2\2\u00df\u00e0")
        buf.write("\t\27\2\2\u00e0.\3\2\2\2\u00e1\u00e2\t\30\2\2\u00e2\60")
        buf.write("\3\2\2\2\u00e3\u00e4\t\31\2\2\u00e4\62\3\2\2\2\u00e5\u00e6")
        buf.write("\t\32\2\2\u00e6\64\3\2\2\2\u00e7\u00e8\t\33\2\2\u00e8")
        buf.write("\66\3\2\2\2\u00e9\u00ea\7<\2\2\u00ea\u00eb\7?\2\2\u00eb")
        buf.write("8\3\2\2\2\u00ec\u00ed\7-\2\2\u00ed:\3\2\2\2\u00ee\u00ef")
        buf.write("\7/\2\2\u00ef<\3\2\2\2\u00f0\u00f1\7,\2\2\u00f1>\3\2\2")
        buf.write("\2\u00f2\u00f3\7\61\2\2\u00f3@\3\2\2\2\u00f4\u00f5\5\33")
        buf.write("\16\2\u00f5\u00f6\5\37\20\2\u00f6\u00f7\5\t\5\2\u00f7")
        buf.write("B\3\2\2\2\u00f8\u00f9\7?\2\2\u00f9D\3\2\2\2\u00fa\u00fb")
        buf.write("\7@\2\2\u00fbF\3\2\2\2\u00fc\u00fd\7@\2\2\u00fd\u00fe")
        buf.write("\7?\2\2\u00feH\3\2\2\2\u00ff\u0100\7>\2\2\u0100J\3\2\2")
        buf.write("\2\u0101\u0102\7>\2\2\u0102\u0103\7?\2\2\u0103L\3\2\2")
        buf.write("\2\u0104\u0105\5\3\2\2\u0105\u0106\5\35\17\2\u0106\u0107")
        buf.write("\5\t\5\2\u0107N\3\2\2\2\u0108\u0109\5\37\20\2\u0109\u010a")
        buf.write("\5%\23\2\u010aP\3\2\2\2\u010b\u010c\7>\2\2\u010c\u010d")
        buf.write("\7@\2\2\u010dR\3\2\2\2\u010e\u010f\5\35\17\2\u010f\u0110")
        buf.write("\5\37\20\2\u0110\u0111\5)\25\2\u0111T\3\2\2\2\u0112\u0113")
        buf.write("\5\t\5\2\u0113\u0114\5\23\n\2\u0114\u0115\5-\27\2\u0115")
        buf.write("V\3\2\2\2\u0116\u0117\5\r\7\2\u0117\u0118\5\37\20\2\u0118")
        buf.write("\u0119\5%\23\2\u0119X\3\2\2\2\u011a\u011b\5)\25\2\u011b")
        buf.write("\u011c\5\37\20\2\u011cZ\3\2\2\2\u011d\u011e\5\t\5\2\u011e")
        buf.write("\u011f\5\37\20\2\u011f\u0120\5/\30\2\u0120\u0121\5\35")
        buf.write("\17\2\u0121\u0122\5)\25\2\u0122\u0123\5\37\20\2\u0123")
        buf.write("\\\3\2\2\2\u0124\u0125\5\23\n\2\u0125\u0126\5\35\17\2")
        buf.write("\u0126\u0127\5)\25\2\u0127\u0128\5\13\6\2\u0128\u0129")
        buf.write("\5\17\b\2\u0129\u012a\5\13\6\2\u012a\u012b\5%\23\2\u012b")
        buf.write("^\3\2\2\2\u012c\u012d\5-\27\2\u012d\u012e\5\37\20\2\u012e")
        buf.write("\u012f\5\23\n\2\u012f\u0130\5\t\5\2\u0130`\3\2\2\2\u0131")
        buf.write("\u0132\5%\23\2\u0132\u0133\5\13\6\2\u0133\u0134\5\3\2")
        buf.write("\2\u0134\u0135\5\31\r\2\u0135b\3\2\2\2\u0136\u0137\5\'")
        buf.write("\24\2\u0137\u0138\5)\25\2\u0138\u0139\5%\23\2\u0139\u013a")
        buf.write("\5\23\n\2\u013a\u013b\5\35\17\2\u013b\u013c\5\17\b\2\u013c")
        buf.write("d\3\2\2\2\u013d\u013e\5\5\3\2\u013e\u013f\5\37\20\2\u013f")
        buf.write("\u0140\5\37\20\2\u0140\u0141\5\31\r\2\u0141\u0142\5\13")
        buf.write("\6\2\u0142\u0143\5\3\2\2\u0143\u0144\5\35\17\2\u0144f")
        buf.write("\3\2\2\2\u0145\u0146\5\5\3\2\u0146\u0147\5%\23\2\u0147")
        buf.write("\u0148\5\13\6\2\u0148\u0149\5\3\2\2\u0149\u014a\5\27\f")
        buf.write("\2\u014ah\3\2\2\2\u014b\u014c\5\7\4\2\u014c\u014d\5\37")
        buf.write("\20\2\u014d\u014e\5\35\17\2\u014e\u014f\5)\25\2\u014f")
        buf.write("\u0150\5\23\n\2\u0150\u0151\5\35\17\2\u0151\u0152\5+\26")
        buf.write("\2\u0152\u0153\5\13\6\2\u0153j\3\2\2\2\u0154\u0155\5\t")
        buf.write("\5\2\u0155\u0156\5\37\20\2\u0156l\3\2\2\2\u0157\u0158")
        buf.write("\5/\30\2\u0158\u0159\5\21\t\2\u0159\u015a\5\23\n\2\u015a")
        buf.write("\u015b\5\31\r\2\u015b\u015c\5\13\6\2\u015cn\3\2\2\2\u015d")
        buf.write("\u015e\5\23\n\2\u015e\u015f\5\r\7\2\u015fp\3\2\2\2\u0160")
        buf.write("\u0161\5\13\6\2\u0161\u0162\5\31\r\2\u0162\u0163\5\'\24")
        buf.write("\2\u0163\u0164\5\13\6\2\u0164r\3\2\2\2\u0165\u0166\5%")
        buf.write("\23\2\u0166\u0167\5\13\6\2\u0167\u0168\5)\25\2\u0168\u0169")
        buf.write("\5+\26\2\u0169\u016a\5%\23\2\u016a\u016b\5\35\17\2\u016b")
        buf.write("t\3\2\2\2\u016c\u016d\5)\25\2\u016d\u016e\5\21\t\2\u016e")
        buf.write("\u016f\5\13\6\2\u016f\u0170\5\35\17\2\u0170v\3\2\2\2\u0171")
        buf.write("\u0172\5\5\3\2\u0172\u0173\5\13\6\2\u0173\u0174\5\17\b")
        buf.write("\2\u0174\u0175\5\23\n\2\u0175\u0176\5\35\17\2\u0176x\3")
        buf.write("\2\2\2\u0177\u0178\5\13\6\2\u0178\u0179\5\35\17\2\u0179")
        buf.write("\u017a\5\t\5\2\u017az\3\2\2\2\u017b\u017c\5\r\7\2\u017c")
        buf.write("\u017d\5+\26\2\u017d\u017e\5\35\17\2\u017e\u017f\5\7\4")
        buf.write("\2\u017f\u0180\5)\25\2\u0180\u0181\5\23\n\2\u0181\u0182")
        buf.write("\5\37\20\2\u0182\u0183\5\35\17\2\u0183|\3\2\2\2\u0184")
        buf.write("\u0185\5!\21\2\u0185\u0186\5%\23\2\u0186\u0187\5\37\20")
        buf.write("\2\u0187\u0188\5\7\4\2\u0188\u0189\5\13\6\2\u0189\u018a")
        buf.write("\5\t\5\2\u018a\u018b\5+\26\2\u018b\u018c\5%\23\2\u018c")
        buf.write("\u018d\5\13\6\2\u018d~\3\2\2\2\u018e\u018f\5-\27\2\u018f")
        buf.write("\u0190\5\3\2\2\u0190\u0191\5%\23\2\u0191\u0080\3\2\2\2")
        buf.write("\u0192\u0193\5\3\2\2\u0193\u0194\5%\23\2\u0194\u0195\5")
        buf.write("%\23\2\u0195\u0196\5\3\2\2\u0196\u0197\5\63\32\2\u0197")
        buf.write("\u0082\3\2\2\2\u0198\u0199\5\37\20\2\u0199\u019a\5\r\7")
        buf.write("\2\u019a\u0084\3\2\2\2\u019b\u019c\5/\30\2\u019c\u019d")
        buf.write("\5\23\n\2\u019d\u019e\5)\25\2\u019e\u019f\5\21\t\2\u019f")
        buf.write("\u0086\3\2\2\2\u01a0\u01a1\7*\2\2\u01a1\u01a2\7,\2\2\u01a2")
        buf.write("\u01a6\3\2\2\2\u01a3\u01a5\13\2\2\2\u01a4\u01a3\3\2\2")
        buf.write("\2\u01a5\u01a8\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a9")
        buf.write("\u01aa\7,\2\2\u01aa\u01ab\7+\2\2\u01ab\u01ac\3\2\2\2\u01ac")
        buf.write("\u01ad\bD\2\2\u01ad\u0088\3\2\2\2\u01ae\u01b2\7}\2\2\u01af")
        buf.write("\u01b1\13\2\2\2\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2")
        buf.write("\2\u01b2\u01b3\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b3\u01b5")
        buf.write("\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\7\177\2\2\u01b6")
        buf.write("\u01b7\3\2\2\2\u01b7\u01b8\bE\2\2\u01b8\u008a\3\2\2\2")
        buf.write("\u01b9\u01ba\7\61\2\2\u01ba\u01bb\7\61\2\2\u01bb\u01bf")
        buf.write("\3\2\2\2\u01bc\u01be\13\2\2\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("\u01c1\3\2\2\2\u01bf\u01c0\3\2\2\2\u01bf\u01bd\3\2\2\2")
        buf.write("\u01c0\u01c5\3\2\2\2\u01c1\u01bf\3\2\2\2\u01c2\u01c4\n")
        buf.write("\34\2\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c8\3\2\2\2")
        buf.write("\u01c7\u01c5\3\2\2\2\u01c8\u01c9\bF\2\2\u01c9\u008c\3")
        buf.write("\2\2\2\u01ca\u01cb\5)\25\2\u01cb\u01cc\5%\23\2\u01cc\u01cd")
        buf.write("\5+\26\2\u01cd\u01ce\5\13\6\2\u01ce\u01d6\3\2\2\2\u01cf")
        buf.write("\u01d0\5\r\7\2\u01d0\u01d1\5\3\2\2\u01d1\u01d2\5\31\r")
        buf.write("\2\u01d2\u01d3\5\'\24\2\u01d3\u01d4\5\13\6\2\u01d4\u01d6")
        buf.write("\3\2\2\2\u01d5\u01ca\3\2\2\2\u01d5\u01cf\3\2\2\2\u01d6")
        buf.write("\u008e\3\2\2\2\u01d7\u01db\t\35\2\2\u01d8\u01da\t\36\2")
        buf.write("\2\u01d9\u01d8\3\2\2\2\u01da\u01dd\3\2\2\2\u01db\u01d9")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u0090\3\2\2\2\u01dd")
        buf.write("\u01db\3\2\2\2\u01de\u01df\7.\2\2\u01df\u0092\3\2\2\2")
        buf.write("\u01e0\u01e1\7\60\2\2\u01e1\u01e2\7\60\2\2\u01e2\u0094")
        buf.write("\3\2\2\2\u01e3\u01e4\7<\2\2\u01e4\u0096\3\2\2\2\u01e5")
        buf.write("\u01e6\7=\2\2\u01e6\u0098\3\2\2\2\u01e7\u01e8\7]\2\2\u01e8")
        buf.write("\u009a\3\2\2\2\u01e9\u01ea\7_\2\2\u01ea\u009c\3\2\2\2")
        buf.write("\u01eb\u01ec\7*\2\2\u01ec\u009e\3\2\2\2\u01ed\u01ee\7")
        buf.write("+\2\2\u01ee\u00a0\3\2\2\2\u01ef\u01f0\7}\2\2\u01f0\u00a2")
        buf.write("\3\2\2\2\u01f1\u01f2\7\177\2\2\u01f2\u00a4\3\2\2\2\u01f3")
        buf.write("\u01f5\t\37\2\2\u01f4\u01f3\3\2\2\2\u01f5\u01f6\3\2\2")
        buf.write("\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u00a6")
        buf.write("\3\2\2\2\u01f8\u01fa\t\37\2\2\u01f9\u01f8\3\2\2\2\u01fa")
        buf.write("\u01fb\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2")
        buf.write("\u01fc\u01fd\3\2\2\2\u01fd\u01ff\t\6\2\2\u01fe\u0200\7")
        buf.write("/\2\2\u01ff\u01fe\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0202")
        buf.write("\3\2\2\2\u0201\u0203\t\37\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("\u0204\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u00a8\3\2\2\2\u0206\u021e\5\u00a7T\2\u0207\u0209")
        buf.write("\t\37\2\2\u0208\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a")
        buf.write("\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020c\3\2\2\2")
        buf.write("\u020c\u0213\7\60\2\2\u020d\u0214\5\u00a7T\2\u020e\u0210")
        buf.write("\t\37\2\2\u020f\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u020f\3\2\2\2\u0211\u0212\3\2\2\2\u0212\u0214\3\2\2\2")
        buf.write("\u0213\u020d\3\2\2\2\u0213\u020f\3\2\2\2\u0213\u0214\3")
        buf.write("\2\2\2\u0214\u021e\3\2\2\2\u0215\u0216\7\60\2\2\u0216")
        buf.write("\u021e\5\u00a7T\2\u0217\u0219\7\60\2\2\u0218\u021a\t\37")
        buf.write("\2\2\u0219\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u0219")
        buf.write("\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u021e\3\2\2\2\u021d")
        buf.write("\u0206\3\2\2\2\u021d\u0208\3\2\2\2\u021d\u0215\3\2\2\2")
        buf.write("\u021d\u0217\3\2\2\2\u021e\u00aa\3\2\2\2\u021f\u0221\t")
        buf.write(" \2\2\u0220\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0220")
        buf.write("\3\2\2\2\u0222\u0223\3\2\2\2\u0223\u0224\3\2\2\2\u0224")
        buf.write("\u0225\bV\2\2\u0225\u00ac\3\2\2\2\u0226\u022a\7$\2\2\u0227")
        buf.write("\u0229\13\2\2\2\u0228\u0227\3\2\2\2\u0229\u022c\3\2\2")
        buf.write("\2\u022a\u022b\3\2\2\2\u022a\u0228\3\2\2\2\u022b\u0230")
        buf.write("\3\2\2\2\u022c\u022a\3\2\2\2\u022d\u022f\n!\2\2\u022e")
        buf.write("\u022d\3\2\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2")
        buf.write("\u0230\u0231\3\2\2\2\u0231\u0233\3\2\2\2\u0232\u0230\3")
        buf.write("\2\2\2\u0233\u0234\7$\2\2\u0234\u0235\bW\3\2\u0235\u00ae")
        buf.write("\3\2\2\2\u0236\u023c\7$\2\2\u0237\u023b\n!\2\2\u0238\u0239")
        buf.write("\7^\2\2\u0239\u023b\t\"\2\2\u023a\u0237\3\2\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023c\u023d\3\2\2\2\u023d\u023f\3\2\2\2\u023e\u023c\3")
        buf.write("\2\2\2\u023f\u0240\bX\4\2\u0240\u00b0\3\2\2\2\u0241\u0247")
        buf.write("\7$\2\2\u0242\u0246\n!\2\2\u0243\u0244\7^\2\2\u0244\u0246")
        buf.write("\t\"\2\2\u0245\u0242\3\2\2\2\u0245\u0243\3\2\2\2\u0246")
        buf.write("\u0249\3\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2")
        buf.write("\u0248\u024a\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b\7")
        buf.write("^\2\2\u024b\u024c\n\"\2\2\u024c\u024d\bY\5\2\u024d\u00b2")
        buf.write("\3\2\2\2\u024e\u024f\13\2\2\2\u024f\u0250\bZ\6\2\u0250")
        buf.write("\u00b4\3\2\2\2\31\2\u01a6\u01b2\u01bf\u01c5\u01d5\u01db")
        buf.write("\u01f6\u01fb\u01ff\u0204\u020a\u0211\u0213\u021b\u021d")
        buf.write("\u0222\u022a\u0230\u023a\u023c\u0245\u0247\7\b\2\2\3W")
        buf.write("\2\3X\3\3Y\4\3Z\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CEOP = 1
    ADDOP = 2
    SUBOP = 3
    MULOP = 4
    DIVOP = 5
    MODOP = 6
    EQUOP = 7
    MTOP = 8
    MTEOP = 9
    LTOP = 10
    LTEOP = 11
    ANDOP = 12
    OROP = 13
    NEOP = 14
    NOTOP = 15
    DIV = 16
    FOR = 17
    TO = 18
    DOWNTO = 19
    INTTYPE = 20
    VOIDTYPE = 21
    REALTYPE = 22
    STRINGTYPE = 23
    BOOLEAN = 24
    BREAK = 25
    CONTINUE = 26
    DO = 27
    WHILE = 28
    IF = 29
    ELSE = 30
    RETURN = 31
    THEN = 32
    BEGIN = 33
    END = 34
    FUNCTION = 35
    PROCEDURE = 36
    VAR = 37
    ARRAY = 38
    OF = 39
    WITH = 40
    TRADITIONAL_BLOCK = 41
    BLOCK_COMMENT = 42
    LINE_COMMENT = 43
    BOOLLIT = 44
    ID = 45
    COMMA = 46
    DOUDOT = 47
    COLON = 48
    SEMI = 49
    LSB = 50
    RSB = 51
    LB = 52
    RB = 53
    LP = 54
    RP = 55
    INTLIT = 56
    FLOATLIT = 57
    WS = 58
    STRINGLIT = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    ERROR_CHAR = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'+'", "'-'", "'*'", "'/'", "'='", "'>'", "'>='", "'<'", 
            "'<='", "'<>'", "','", "'..'", "':'", "';'", "'['", "']'", "'('", 
            "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "CEOP", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "EQUOP", 
            "MTOP", "MTEOP", "LTOP", "LTEOP", "ANDOP", "OROP", "NEOP", "NOTOP", 
            "DIV", "FOR", "TO", "DOWNTO", "INTTYPE", "VOIDTYPE", "REALTYPE", 
            "STRINGTYPE", "BOOLEAN", "BREAK", "CONTINUE", "DO", "WHILE", 
            "IF", "ELSE", "RETURN", "THEN", "BEGIN", "END", "FUNCTION", 
            "PROCEDURE", "VAR", "ARRAY", "OF", "WITH", "TRADITIONAL_BLOCK", 
            "BLOCK_COMMENT", "LINE_COMMENT", "BOOLLIT", "ID", "COMMA", "DOUDOT", 
            "COLON", "SEMI", "LSB", "RSB", "LB", "RB", "LP", "RP", "INTLIT", 
            "FLOATLIT", "WS", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "CEOP", "ADDOP", "SUBOP", "MULOP", 
                  "DIVOP", "MODOP", "EQUOP", "MTOP", "MTEOP", "LTOP", "LTEOP", 
                  "ANDOP", "OROP", "NEOP", "NOTOP", "DIV", "FOR", "TO", 
                  "DOWNTO", "INTTYPE", "VOIDTYPE", "REALTYPE", "STRINGTYPE", 
                  "BOOLEAN", "BREAK", "CONTINUE", "DO", "WHILE", "IF", "ELSE", 
                  "RETURN", "THEN", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
                  "VAR", "ARRAY", "OF", "WITH", "TRADITIONAL_BLOCK", "BLOCK_COMMENT", 
                  "LINE_COMMENT", "BOOLLIT", "ID", "COMMA", "DOUDOT", "COLON", 
                  "SEMI", "LSB", "RSB", "LB", "RB", "LP", "RP", "INTLIT", 
                  "Real1", "FLOATLIT", "WS", "STRINGLIT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[85] = self.STRINGLIT_action 
            actions[86] = self.UNCLOSE_STRING_action 
            actions[87] = self.ILLEGAL_ESCAPE_action 
            actions[88] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             
            s = self.text[1:-1]
            self.text = s

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             raise UncloseString(self.text[1:]) 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
             raise IllegalEscape(self.text[1:]) 
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise ErrorToken(self.text[0:]) 
     


