from Token import Token
import os.path
import sys

# Class Scanner - Reads a TINY program and emits tokens.
class Scanner:

        # Constructor - Is passed a file to scan and outputs a token
        # each time nextToken() is invoked.
        def __init__(self, fileName):
            self.position = 0
            self.fileName = fileName
            # check that the file name exists...
            if not os.path.isfile(self.fileName):
                print("File does not exist!")
                sys.exit()
            self.nextChar()

        # Function nextChar() updates c with the next Character
        def nextChar(self):
            self.f = open(self.fileName, 'r')
            self.f.seek(self.position)
            self.c = self.f.read(1)

            if not self.c:
                self.c = 'eof'
            else:
                self.position = self.f.tell()
            self.f.close()

        # Function nextToken() reads characters in the file and returns
        # the next token - THIS FUNCTION NEEDS TO BE COMPLETED
        def nextToken(self):
            # if its the end of file...
            if self.c == 'eof':
                token = Token(Token.EOF, 'eof')
            # if it a whitespace...
            elif self.c.isspace():
                str = ''
                while self.c.isspace():
                    str += self.c
                    self.nextChar()
                token = Token(Token.WS, str)
            # if it is addition operator
            elif self.c == '+':
                token = Token(Token.ADDOP, self.c)
                self.nextChar()
            # if it is subtraction operator
            elif self.c == '-':
                token = Token(Token.SUBOP, self.c)
                self.nextChar()
            # if it is equal operator
            elif self.c == '=':
                token = Token(Token.EQQOP, self.c)
                self.nextChar()
            # if it is multiplication operator
            elif self.c == '*':
                token = Token(Token.MULOP, self.c)
                self.nextChar()
            # if it is division operator
            elif self.c == '/':
                token = Token(Token.DIVOP, self.c)
                self.nextChar()
            # if it is LEFT parenthesis
            elif self.c == '(':
                token = Token(Token.LPAREN, self.c)
                self.nextChar()
            # if it is RIGHT parenthesis
            elif self.c == ')':
                token = Token(Token.RPAREN, self.c)
                self.nextChar()
            # if its a number
            elif self.c.isdigit():
                str = ''
                while self.c.isalnum():
                    str += self.c
                    self.nextChar()
                token = Token(Token.DIGIT, str)
            # if multiple upper or lower case characters...
            elif self.c.islower() or self.c.isupper():
                str = ''
                while self.c.isupper() or self.c.islower():
                    str += self.c
                    self.nextChar()
                # if it spells "print"
                if str == "print":
                    token = Token(Token.PRINT, str)
                elif str == "EXP":
                    token = Token("EXP", str)
                elif str == "EPSILON":
                    token = Token("unknown", str)
                elif str == "STMT":
                    token = Token("unknown", str)
                else:
                    token = Token(Token.ALPHA, str)
            # if its unknown...
            else:
                token = Token("unknown", self.c)
                self.nextChar()
            return token

        # prints all the tokens in a sentence in a file
        def printAllTokens(self):
            print("File name: " + self.fileName)
            str = ''
            while str != '[Type: EOF, Text: eof]':
                str = self.nextToken().toString()
                print(str)


