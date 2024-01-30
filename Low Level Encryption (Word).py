import random
import string

def rndm_crcter_gnrtr(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def wrd_les_thn3(word):
    new_wrd = word[1] + word [0]
    return new_wrd

code_decode = input('Enter the word to code c or to decode d: ')
if code_decode == "c":
    print('You want to code a word')
    wrd = input('Enter the word you want to code: ') 
    print('The entered string is ', wrd)
    print()
    if len(wrd) < 3:
        a = wrd_les_thn3(wrd)
        print('The coded word is: ', a)    
    else:
        for j in range(len(wrd)):
            print('Processing........') 
        code1 = rndm_crcter_gnrtr(3) + wrd[1:j+1] + wrd[0] + rndm_crcter_gnrtr(3)
        print('The code word is: ', code1)
    
else:
    print('You want to decode a word')
    word = input('Enter the word you want to decode ')
    print('The entered string is: ', word )
    if len(word) < 3:
        b = wrd_les_thn3(word)
        print('The decoded word is: ', b)
    else:
        for j in range(len(word)):
            print('Processing........')
        decoded2 = word[-4] + word[3:-4]
        print('The decode word is: ', decoded2)