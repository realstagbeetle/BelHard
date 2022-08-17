sentence = input('Please, write your sentence with spaces: ')
sentence = sentence.translate(str.maketrans(' ', '-'))
print(sentence)
