class Node:
   
    def __init__(self,character = None, isTerminal : bool = False) -> None:
      self.character = character
      self.children = {}
      self.isTerminal = isTerminal

class Trie:
    def __init__(self) -> None:
        self.root = Node('')
    
    def insert(self,word:str) -> None:
        """
        This method inserts a word into the trie
        """
        curr = self.root
        for char in word:
           
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]
       
        curr.isTerminal=True
    
    def __contains__(self,word:str) -> bool:
        """
        This method helps to check if the trie contains a certain word as 
        a valid word (i.e ->  The word ends with a Terminal Character node)
        """
        curr = self.root
        for char in word:
           
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.isTerminal
    
    def getPrefixes(self,word) -> list:
        """
        This method returns all the possible prefixes of a word already existing in
        the trie
        """
        prefix = ''
        prefixes = []
        curr = self.root
        for char in word:
            """
            Whenever the currently read character is not found within the children of
            the current trie, the prefixes list is returned, else we traverse all the
            characters in the word 
            """
            if char not in curr.children:
                return prefixes
            curr = curr.children[char]
            prefix += char
            if curr.isTerminal:
                prefixes.append(prefix)
        return prefixes