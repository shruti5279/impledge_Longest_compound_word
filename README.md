# impledge_Longest_compound_word
A brief study of the problem:
Compounded words are the words formed using one or more of the valid words only in the selected file.
Since the files are already sorted alphabetically and only contain one word per line some of the the valid words that compose the compounded words are bound to come before the compounded word itself.
Thus the compounded word can be thought of as the combination of some of the the words that have been already read i.e. -> prefix, and a suffix.
If there is a situation where some letters which are not the part of any valid word in the file but occurs within any position of the word currently being read. Then the word can not be considered as a compounded word.

Approach:-
The above code defines a Python class `Solution` that builds a trie data structure and then finds the longest and second longest compound words within that trie using a queue-based algorithm. Here's a breakdown of the code:

1. Import necessary libraries: The code imports the `Trie` class (defined in a separate file) and the `deque` class from the `collections` module. It also imports the `time` module for measuring execution time.

2. `Solution` class constructor:
   - Initializes an instance of the `Trie` class as `self.trie`.
   - Initializes an empty deque as `self.queue`.

3. `buildT` method:
   - Reads a file specified by the `filePath` parameter.
   - For each line in the file, it strips the newline character and attempts to find prefixes of the word within the trie.
   - If prefixes are found, it divides the word into its suffixes and enters `(word, suffix)` pairs into the deque.
   - Finally, it inserts the word into the trie.

4. `findLongestCompoundWords` method:
   - Initializes variables for tracking the longest and second longest compound words.
   - Iterates through the deque until it's empty.
   - For each entry in the deque, it checks if the suffix is a valid word in the trie and if the length of the current word is greater than the previously recorded longest length.
   - If the conditions are met, it updates the longest and second longest words.
   - If not, it finds possible prefixes for the suffix and continues processing.

5. The code then includes two `if __name__ == "__main__":` blocks:
   - In the first block, it initializes an instance of the `Solution` class, reads input from "Input_01.txt", builds the trie, and finds the longest and second longest compound words. It measures the execution time and prints the results.
   - The second block does the same but with "Input_02.txt".

