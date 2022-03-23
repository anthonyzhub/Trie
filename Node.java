package Trie;
import java.util.HashMap;

public class Node {

    // Create class variables
    public boolean endOfWord = false;
    public HashMap<Character, Node> children = new HashMap<Character, Node>();
}