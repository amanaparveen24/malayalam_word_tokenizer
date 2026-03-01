import string
text = input('Enter your Malayalam text here: ')
#sentence segmentation
sentences = text.split('.')
for sentence in sentences:
    sentence = sentence.strip()
    if sentence != '':
        print('-',sentence)
print('\nWord Tokens Per Sentence:')
#word tokenization
for sentence in sentences:
    sentence = sentence.strip()
    if sentence != '':
        #remove punctuation
        clean_sentence = sentence.translate(str.maketrans('','',string.punctuation))
        words = clean_sentence.split()
        print('\nSentence:',sentence)
        print('Words:',words)
