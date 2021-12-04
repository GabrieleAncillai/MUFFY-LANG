from functions.PYParser import ParserToPY
from functions.CPPParser import ParserToCPP
from functions.Lexer import LexAnalizer
import time
import os

if __name__ == '__main__':
    StartTimer = time.time()
    MuffyFile = open("muffy_lang_example.muffy", "r")
    Lines = MuffyFile.readlines()
    TokenizedLines = LexAnalizer(Lines)

    '''
        for token in TokenizedLines:
        print("token: {}".format(token.replace("\n", "TAB")))
    '''

    ParsedLangCPP = ParserToCPP(TokenizedLines)
    ParsedLangPY = ParserToPY(TokenizedLines)

    try:
        os.remove("dist/muffy_out.cpp")
    except:
        print("Error eliminating output files")

    try:
        os.remove("dist/muffy_out.py")
    except:
        print("Error eliminating output files")

    OutFileCPP = open("dist/muffy_out.cpp", "x")
    OutFileCPP.write(ParsedLangCPP)
    OutFilePY = open("dist/muffy_out.py", "x")
    OutFilePY.write(ParsedLangPY)
    print("--- %s seconds ---" % (time.time() - StartTimer))
