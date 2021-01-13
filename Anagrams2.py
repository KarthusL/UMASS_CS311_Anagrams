import sys
import time
import numpy as np
'''
Project created on Oct 23, 2017
    created by Yifu Liu
'''
'''The program should perform better than nklogn + nklogk'''
primes = [5, 71, 37, 29, 2, 53, 59, 19, 11, 83, 79, 31, 43, 13, 7, 67, 97, 23, 17, 3, 41, 73, 47, 89, 61, 101]
#Based on the wiki_pedia
#https://en.wikipedia.org/wiki/Letter_frequency
number_of_word = 0


class Main():

    def __init__(self):
        file_index = input('Please enter the file name (1/2) that you want to use :')
        start_time = time.time()
        global number_of_word
        self.table = Table()
        file = [line.rstrip('\n') for line in open(file_index)]
        for word in file:
            a,b = self.get_hash(word)
            self.table.insert(word, a,b)
        print(time.time() - start_time)

    def find_modulus(self):
        global number_of_word
        modulus = 1
        for number in range(1, 28):
            modulus = 2 ** number
            if modulus > number_of_word and (float(number_of_word) / modulus) < (2.0/3):
                break
        return modulus

    def get_hash(self, word):
        global primes
        num = []
        for char in word:
            num.append(primes[ord(char) - 97])
        Lhash = np.prod(num, None, np.int32)
        return Lhash, (Lhash % self.find_modulus())


class Table():
    def __init__(self):
        self.table = []
        self.size = 0

    def insert(self, newWord, a, b):
            if len(self.table) <= b:
                # If table is too small, make more space
                # O(4) time
                difference = (b - len(self.table)) + 1
                self.table[len(self.table):] = [None] * difference
                self.table[b] = (a, [newWord])
                self.size += 1
            elif self.table[b]:
                if self.table[b][0] == a:
                    # O(1) time for check
                    # O(1) for append
                    self.table[b][1].append(newWord)
                else:
                    b += 1
                    #                 conflicts = 1
                    while (True):
                        #                     self.totalConflicts += 1
                        '''
                        This loop could at MOST run at O(n) time.
                        However can run at Omega(1) time.
                        With the modulus size, this should be ~O(3)
                        '''
                        if b == len(self.table):
                            # O(2) time
                            self.table.append((a, [newWord]))
                            self.size += 1
                            break
                        elif self.table[b] is None:
                            # O(2) time
                            self.table[b] = (a, [newWord])
                            self.size += 1
                            break
                        elif self.table[b][0] == a:
                            # O(1) time for check
                            # O(1) for append
                            self.table[b][1].append(newWord)
                            break
                        else:
                            b += 1
                            #                     conflicts+=1
                            #                 if conflicts > self.maxConflicts:
                            #                     self.maxConflicts = conflicts
            else:
                # O(2) time
                self.table[b] = (a, [newWord])
                self.size += 1

if __name__ == '__main__':
    sys.argv.append("dict1.txt")
    sys.argv.append("dict2.txt")
    sys.argv.append("dict3.txt")
    Anagrams = Main()


