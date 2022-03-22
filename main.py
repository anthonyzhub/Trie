#! /bin/python3

# Reference: https://pythonwife.com/trie-in-python/

class Node:
    def __init__(self) -> None:
        self.endOfWord = False
        self.children = dict() # <= Key will be a letter and value will be a reference to a node holding that letter

class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insertString(self, newWord):

        """
        OBJECTIVE: Add the new word to the Trie
        Time complexity is O(m) where m is the length of the word
        Space complexity is O(m) where, in the worst case, m nodes will need to be created to hold each letter
        """

        # Create a temporary node
        curNode = self.root

        # Traverse word
        for letter in newWord:

            # Get child node holding letter
            child = curNode.children.get(letter)

            # If child is None, create a new child node
            if child is None:

                # Create a new node
                newNode = Node()

                # Update key entry
                # I.e., [{a: 0x134}, {r: 0x831}, {e: 0x840}]
                curNode.children.update({letter: newNode})

            curNode = curNode.children[letter]

        # Update boolean variable
        # I.e., Current node is a leaf node, so nothing exist below it
        curNode.endOfWord = True
        print(f"Added {newWord} to Trie")

    def searchString(self, wordToFind):

        """
        OBJECTIVE: Try to find a word inside the trie
        Time complexity is O(m) where m is the length of the word to search for
        Space complexity is O(1) because no new nodes were created
        """

        # Create a temporary node
        curNode = self.root

        # Traverse word
        for letter in wordToFind:

            # Get child node holding letter
            child = curNode.children.get(letter)

            # If neither children has the letter, exit function
            if child is None:
                print(f"{wordToFind} doesn't exist")
                return

            # If child is not none, update curNode and check child's children list
            curNode = curNode.children[letter]

        # Check if curNode holds the last letter in wordToFind
        # I.e., After traversing the trie, if the for-loop ended then it means 2 things.
        #       (1) The leaf has been reached and word does exist
        #       (2) The leaf hasn't been reached yet, so word doesn't exist
        if curNode.endOfWord:
            print(f"Found {wordToFind}")
        else:
            print(f"{wordToFind} doesn't exist. Only prefix was found.")

def main():

    # Create a Trie
    trie = Trie()

    # Insert words to string
    trie.insertString("App")
    trie.insertString("Appl")

    # Search for word inside trie
    trie.searchString("App")
    trie.searchString("Ape")
    trie.searchString("Application")

main()
