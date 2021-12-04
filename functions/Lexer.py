from utils.constants import WHITE_SPACE, KEYWORDS, SYMBOLS, COMMENTS, RESERVED_WORDS


def LexAnalizer(DocLines):
    Tokens = []
    lex = ''
    for line in DocLines:

        WritingString = False
        SingleCommentMode = False
        MultiCommentMode = False

        for index, character in enumerate(line):

            if character == "'" or character == '"':
                WritingString = not WritingString

            if character != WHITE_SPACE or WritingString:
                lex += character

            if index + 1 < len(line):
                NextChar = line[index + 1]
                NextIsWS = NextChar == WHITE_SPACE
                NextInKey = NextChar in KEYWORDS
                NextInSym = NextChar in SYMBOLS
                LexInReserved = lex in RESERVED_WORDS
                LexInComment = lex in COMMENTS
                LexInSym = lex in SYMBOLS
                LexInKey = lex in KEYWORDS

                # if NextIsWS or NextInKey or LexInKey: # (Prev)
                if NextIsWS or NextInSym or LexInComment or LexInSym or (LexInReserved and (NextInSym or NextIsWS)):
                    if lex != '':
                        Tokens.append(lex)
                        lex = ''

    return Tokens
