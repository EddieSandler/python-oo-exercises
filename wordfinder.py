"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    ...

    def __init__(self,path):
        '''constructor method which accepts a file path and
        calls the read_file method '''
        self.path=path
        self.read_file()

    def __repr__(self):
        return f"location of file to be read by Wordfinder"

    def read_file(self):
        '''reads word file into a list '''
        counter=0
        self.words=[]
        with open(self.path,) as file:

            for word in file:
                word=word.strip()
                self.words.append(word)
                counter+=1
        return print(f"{counter} words read")


    def random(self):
        '''generates a random number used as the
        index for the words list
        returns the word at that random index'''
        rando=randint(0, len(self.words))
        return self.words[rando]


