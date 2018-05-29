import unittest
from Token import Token
from Scanner import Scanner


# test the Token and Scanner classes
class Tests(unittest.TestCase):
    # ===============Token=Tests=======================
    # test Token constructor
    def test_constructor_Token(self):
        token = Token('my type', 'my text')
        self.assertEqual('my type', token.type)
        self.assertEqual('my text', token.text)

    # Test token toString() function
    def test_toString_Token(self):
        token = Token('my type', 'my text')
        self.assertEqual('[Type: my type, Text: my text]', token.toString())
        self.assertEqual('my type', token.type)
        self.assertEqual('my text', token.text)

    # =================Scanner-Tests==================
    # test Scanner constructor
    def test_constructor_Scanner(self):
        scanner = Scanner('Tiny.txt')
        self.assertEqual('Tiny.txt', scanner.fileName)

    # test nextChar() function
    def test_nextChar_Scanner(self):
        scanner = Scanner('Tiny.txt')
        scanner.nextChar()
        self.assertEqual('r', scanner.c)

    # test nextToken() function, Tests that all tokens are found, and
    # any thing that is NOT a token is assigned to an unknown token
    def test_nextToken_Scanner1(self):
        scanner1 = Scanner('Tiny.txt')
        passTest = True

        # test if "print" token is found
        if not '[Type: PRINT, Text: print]' == scanner1.nextToken().toString():
            passTest = False
        # test if "=" token is found
        if not '[Type: =, Text: =]' == scanner1.nextToken().toString():
            passTest = False
        # test if "+" token is found
        if not '[Type: +, Text: +]' == scanner1.nextToken().toString():
            passTest = False
        # test if "-" token is found
        if not '[Type: -, Text: -]' == scanner1.nextToken().toString():
            passTest = False
        # test if "*" token is found
        if not '[Type: *, Text: *]' == scanner1.nextToken().toString():
            passTest = False
        # test if "/" token is found
        if not '[Type: /, Text: /]' == scanner1.nextToken().toString():
            passTest = False
        # test is "(" token is found
        if not '[Type: (, Text: (]' == scanner1.nextToken().toString():
            passTest = False
        # test if ")" token is found
        if not '[Type: ), Text: )]' == scanner1.nextToken().toString():
            passTest = False
        # test if SINGLE character ALPHA is found
        if not '[Type: ALPHA, Text: a]' == scanner1.nextToken().toString():
            passTest = False
        # test if whitespace token is found
        if not '[Type: whitespace, Text:  ]' == scanner1.nextToken().toString():
            passTest = False
        # test if MULTIPLE character ALPHA is found
        if not '[Type: ALPHA, Text: abc]' == scanner1.nextToken().toString():
            passTest = False
        # the next token is whitespace, which has already been tested, so skip
        scanner1.nextToken()
        # test if SINGLE DIGIT token is found
        if not '[Type: DIGIT, Text: 1]' == scanner1.nextToken().toString():
            passTest = False
        # the next token is whitespace, which has already been tested, so skip
        scanner1.nextToken()
        # test if MULTIPLE DIGIT tokens are found
        if not '[Type: DIGIT, Text: 123]' == scanner1.nextToken().toString():
            passTest = False
        # the next token is whitespace, which has already been tested, so skip
        scanner1.nextToken()
        # test if EPSILON is found, not a token, but could be in a sentence
        if not '[Type: unknown, Text: EPSILON]' == scanner1.nextToken().toString():
            passTest = False
        # the next token is whitespace, which has already been tested, so skip
        scanner1.nextToken()
        # test if EXP token is found
        if not '[Type: EXP, Text: EXP]' == scanner1.nextToken().toString():
            passTest = False
        # the next token is whitespace, which has already been tested, so skip
        scanner1.nextToken()
        # test if STMT is found, not a token, but could be part of a sentence
        if not '[Type: unknown, Text: STMT]' == scanner1.nextToken().toString():
            passTest = False
        # the next token is whitespace, which has already been tested, so skip
        scanner1.nextToken()
        # test if the "eof" token is printed at the end of the file
        if not '[Type: EOF, Text: eof]' == scanner1.nextToken().toString():
            passTest = False

        # if all tokens are found, the test passes
        self.assertTrue(passTest)


# main
if __name__ == '__main__':
    unittest.main()
