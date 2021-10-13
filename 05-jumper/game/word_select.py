import random

class Word_Select:
    """
    A class that picks a word from the wordlist10000.txt file.

    """
    def Word_Select(self):
        """
        Returns a randomly selected word from the given file named wordselect10000.py

        arguments:
                 self, an instance of Word_Select.

        returns:
                 a string containing the picked word.
        """
        # (SA) reads the file and splits it into a list
        with open("wordlist10000.txt", "r") as word_file:
            content = word_file.read()
        content_list = content.split()
        # (SA) picks a word
        picked_word = random.sample(content_list,1)
        # (SA) converts list length 1 into a string
        final_word = ""
        for ele in picked_word:
            final_word = ele
        # (SA) returns string word
        return final_word






