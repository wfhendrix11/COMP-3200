# Class Token - Encapsulates the tokens in TINY
#
# type = the type of token
# text = the text of the token


class Token:
    # Token Class Variables
    EOF = "EOF"
    LPAREN = "("
    RPAREN = ")"
    ADDOP = "+"
    SUBOP = "-"
    EQQOP = "="
    ORROP = "|"
    MULOP = "*"
    DIVOP = "/"
    PRINT = "PRINT"
    ALPHA = "ALPHA"
    DIGIT = "DIGIT"
    EXP = "EXP"
    WS = "whitespace"
    # ... more needed here DIGIT and ALPHA
    
    # Constructor
    def __init__(self, type, text):
        self.type = type
        self.text = text

    # String representation of an instance of Token
    def toString(self):
        return '[Type: {}, Text: {}]'.format(self.type, self.text)
