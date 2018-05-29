from Scanner import Scanner

# test all the tokens that could be in a sentence
#scanner1 = Scanner('Tiny.txt')
#scanner1.printAllTokens()

# test two random sentences that could be generated
# from the grammar
#scanner2 = Scanner('sampleSentences.txt')
#scanner2.printAllTokens()

# test that the program ends gracefully when the
# file name doesnt exist
#scanner3 = Scanner('fileDoesntExist.txt')

scanner4  = Scanner('test.txt')
scanner4.printAllTokens()