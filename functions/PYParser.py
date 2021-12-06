def ParserToPY(TokenLines):
    Output = ''
    SingleCommentMode = False
    MultiCommentMode = False
    Parenthesis = False
    WritingString = False
    NestLevel = 0
    Buffer = None
    BufferSkip = 0
    DoingForEach = False

    for i, token in enumerate(TokenLines):

        PrevToken = TokenLines[i - 1]
        NextToken = TokenLines[i + 1] if i + 1 != len(TokenLines) else ""
        NextIsColon = False if len(TokenLines) == i + 1 else NextToken == "'" or NextToken == '"'

        # CommentMode toggle
        if SingleCommentMode and "\n" in token:
            SingleCommentMode = False
        elif MultiCommentMode and token == "##":
            MultiCommentMode = False

        # String Handler
        elif WritingString and token != "'" and token != '"':
            if NextIsColon:
                Output += token
            elif NextToken == "{":
                Output += ""
            else:
                Output += f"{token}"

        # Other token handler
        elif not SingleCommentMode and not MultiCommentMode:

            match token:
                # Functions
                case "main":
                    Output += "if __name__ == '__main__'"
                case "print":
                    Output += "print("
                    if NextIsColon:
                        Output += "f"
                    Parenthesis = True

                # Symbols
                case "{":
                    Output += ":"
                    NestLevel += 1
                case "}":
                    Output += "\n"
                    NestLevel -= 1
                    Buffer = ("    " * NestLevel)

                case "'":
                    WritingString = not WritingString
                    Output += "'"
                case '"':
                    WritingString = not WritingString
                    Output += '"'
                case "=":
                    Output += '=' if NextToken == "=" else "= "

                # Logic
                case "true":
                    Output += "True"
                case "false":
                    Output += "False"
                case "is" | "equals":
                    Output += "=="
                case "in":
                    if NextToken.isdigit():
                        Output += "in range("
                        Buffer = ")"
                        BufferSkip = 1
                    elif DoingForEach:
                        Output += "in enumerate("
                        Buffer = ")"
                        BufferSkip = 1
                        DoingForEach = False
                    else:
                        Output += "in "

                # Conditional Statements
                case "switch":
                    Output += "match "
                case "case":
                    Output += "case "
                case "default":
                    Output += "case other"

                case "forEach":
                    Output += "for "
                    DoingForEach = True
                case "if":
                    if PrevToken != "else":
                        Output += "if "
                case "else":
                    if NextToken == "if":
                        Output += "elif "
                    else:
                        Output += "else "

                # Comments
                case "##":
                    MultiCommentMode = True
                case "//":
                    SingleCommentMode = True

                case "\n" | "\n\n":
                    if Parenthesis:
                        Output += ")"
                        Parenthesis = False
                    Output += "\n" + ("    " * NestLevel)

                case other:
                    Output += f"{other} "

            if BufferSkip == 0:
                if Buffer is not None:
                    Output += f"{Buffer}"
                    Buffer = None
            else:
                BufferSkip -= 1

    return Output
