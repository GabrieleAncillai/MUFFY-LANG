def ParserToCPP(TokenLines):
    Output = ''
    CommentMode = False
    for token in TokenLines:
        if CommentMode and "\n" in token:
            CommentMode = False
        elif not CommentMode:
            match token:
                case "main":
                    Output += "int main()"
                case "##":
                    CommentMode = not CommentMode
                case "//":
                    CommentMode = True
                case other:
                    Output += other

    return Output
