import os

if __name__ == '__main__':

    ExeName = "muffy"

    CompileProyectCommand = f"pyinstaller --onefile --name {ExeName} main.py"

    DeleteRemnantCommand = "rmdir /Q /S build"

    MoveExeToSource = f"cd dist && move {ExeName}.exe .. && cd .."

    DeleteRemFile = f"del {ExeName}.spec"

    os.system(f"{CompileProyectCommand} && {DeleteRemnantCommand} && {MoveExeToSource} && {DeleteRemFile}")
    # os.system(f"pyinstaller --name {ExeName} main.py")
