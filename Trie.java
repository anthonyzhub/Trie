import Trie.Node;

public class Trie {

    // Create a root node
    Node root = new Node();

    public void insertString(String newWord) {

        /*
        OBJECTIVE: Try to find a word inside the trie
        Time complexity is O(m) where m is the length of the word to search for
        Space complexity is O(1) because no new nodes were created
        */

        // Create a temporary node
        Node curNode = root;

        // Traverse word
        for (Character letter: newWord.toCharArray()) {

            // Get child node holding letter
            Node child = curNode.children.get(letter);

            // If child is null, create a new node
            if (child == null) {

                // Create a new node
                Node newNode = new Node();

                // Add new node to hashmap
                curNode.children.put(letter, newNode);
            }

            // Update curNode
            curNode = curNode.children.get(letter);
        }

        // Update last node's boolean variable
        curNode.endOfWord = true;
        System.out.printf("Added %s to Trie\n", newWord);
    }

    public void searchString(String wordToFind) {

        /*
        OBJECTIVE: Try to find a word inside the trie
        Time complexity is O(m) where m is the length of the word to search for
        Space complexity is O(1) because no new nodes were created
        */

        // Create a temporary node
        Node curNode = root;

        // Traverse word
        for (Character letter: wordToFind.toCharArray()) {

            // Get child node holding letter
            Node child = curNode.children.get(letter);

            // If child is null, then exit function
            if (child == null) {
                System.out.println(wordToFind + " doesn't exist");
                return;
            }

            // If child is not null, move to the child's child that has the letter
            curNode = child;
        }

        // If curNode holds the last letter in wordToFind, print successful message if the bottom of the trie has been reached
        if (curNode.endOfWord) {
            System.out.println("Found " + wordToFind);
        }
        else {
            System.out.println(wordToFind + " doesn't exist.");
        }
    }
}