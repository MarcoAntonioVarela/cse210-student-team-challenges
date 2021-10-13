import random


class Word_Tracker:

    def __init__(self):
        self.selectedWord = ''
        self.listCorrectLetters = []

    def setSelectedWord(self, selectedWord):
        self.selectedWord = selectedWord

    # (AH) called from Director Class, do_updates() Method.
    # (AH) _if_ letter is in random word from Word_Select Class, return True.
    def trackLetter(self, letter):
        self.listCorrectLetters.append(letter)
        if letter in self.selectedWord:
            return True
        else:
            return False

    # (AH) called from Director Class, do_outputs() Method.
    # (AH) returns string with dashes and correct letters in place.
    def word_string(self):
        string_list = []
        for alphabet in self.selectedWord:
            if alphabet in self.listCorrectLetters:
                string_list.append(alphabet)
            else:
                string_list.append('-')
        return ' '.join(string_list)

    def printSelectedWord(self):
        return self.selectedWord
