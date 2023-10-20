import Trie as T
from collections import deque
import time

class Solution:
    def __init__(self) -> None:
      self.trie = T.Trie()
      self.queue = deque()

    def buildT(self,filePath : str = None) -> None:
        """
        Builds the trie. 
        """
        try:
            with open(filePath, mode = 'r') as f:
                for line in f:
                    """
                    strip the endl charachter from the end of each word and tries to find
                    the prefixes of the word if any lies within the trie.
                    If prefixes are found, simply we divide the word into its respective
                    suffixes and enter the (word,suffix) into the dequeue.
                    Finally we insert the word into the trie.
                    """
                    word = line.rstrip('\n')
                    prefixes = self.trie.getPrefixes(word)
                    for prefix in prefixes:
                        self.queue.append((word, word[len(prefix):]))
                    self.trie.insert(word)
        except:
            print("There was some error within the file!")
            exit(0)
    
    def findLongestCompoundWords(self) -> tuple:
        """
        Finds the longest and second longest compound words within the trie
        and returns them as a  (longest, secondLongest)
        """
        longest_word = ''
        longest_len = 0
        second_longest = ''
        #Iterate the dequeue while it is not empty
        while self.queue:
            #Pop out the first tuple from the front side of the dequeue
            #In this way only the compound words are taken into account
            word, suffix = self.queue.popleft()
           
            if suffix in self.trie and len(word) > longest_len:
                second_longest = longest_word
                longest_word = word
                longest_len = len(word)
            else:
                """
                Else we will get the possible prefixes for the suffix of the word.
                If prefixes are found, simply divide the word into its respective
                suffixes and enter the (word,suffix) into the deque.
                """ 
                prefixes = self.trie.getPrefixes(suffix)
                for prefix in prefixes:
                    self.queue.append((word, suffix[len(prefix):]))

        return (longest_word,second_longest)

if __name__ == "__main__":
    sol = Solution()
    st = time.time()
    sol.buildT("Input_01.txt")
    first,second = sol.findLongestCompoundWords()
    en = time.time()*1000
    print("Longest Compound Word:",first)
    print("Second Longest Compound Word:",second)
    print("Time taken: ",str(en - st), "milliseconds")

if __name__ == "__main__":
    sol = Solution()
    st = time.time()
    sol.buildT("Input_02.txt")
    first,second = sol.findLongestCompoundWords()
    en = time.time()*1000
    print("Longest Compound Word:",first)
    print("Second Longest Compound Word:",second)
    print("Time taken: ",str(en - st), "milliseconds")