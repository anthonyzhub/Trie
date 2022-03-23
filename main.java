class main{

    public static void main(String[] args) {
    
        // Create a Trie
        Trie trie = new Trie();

        // Insert string to trie
        trie.insertString("App");
        trie.insertString("Appl");

        // Search for string inside of trie
        trie.searchString("Application");
        trie.searchString("Ape");
        trie.searchString("App");
    }
}