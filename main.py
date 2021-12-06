from functions.PYParser import ParserToPY
from functions.Lexer import LexAnalizer
import os
import sys
import time

if __name__ == '__main__':

    # Temporizador de compilación
    StartTimer = time.time()

    # Recibe como parámetro de sistema (comando), el archivo a ejecutar
    FILE_TO_COMPILE = sys.argv[1] if len(sys.argv) > 1 else "main.muffy"

    MuffyFile = None

    # Carpeta residuo con los datos del parser
    OutputFolder = "dist"
    OutputFile = f"{OutputFolder}/data.py"

    # Manejo de errores para archivos inexistentes
    try:
        MuffyFile = open(FILE_TO_COMPILE, "r")
    except:
        print("File not found")
        exit()

    if MuffyFile is not None:

        Lines = MuffyFile.readlines()
        TokenizedLines = LexAnalizer(Lines)

        ParsedLangPY = ParserToPY(TokenizedLines)

        try:
            os.remove(OutputFile)
            print("Eliminated output file")
        except:
            print("Error eliminating output files")

        if not os.path.exists(OutputFolder):
            os.mkdir("dist")

        OutFilePY = open(OutputFile, "x")
        OutFilePY.write(ParsedLangPY)
        OutFilePY.close()

        print("- - - File Compiled in %s sec - - -" % (time.time() - StartTimer))

        time.sleep(1)

        try:
            PathFile = OutputFile
            source = open(PathFile).read()
            code = compile(source, PathFile, 'exec')
            exec(code)
        except NameError:
            print(f"Error: {NameError}")

        # EXECUTION TESTING

        # source = open(OutputFile).read()
        # code = compile(source, OutputFile, 'exec')
        # exec(code)
        # os.system(f"python {OutputFile}")
        # with open(OutputFile, "r") as file:
        #     exec(file.read())
        # runpy.run_path(OutputFile, run_name='__main__')
        # runpy.run_module("data", run_name='__main__')

        print("- - - Process finished in %s sec - - -" % (time.time() - StartTimer))

    else:
        print("File not found")
        exit()
