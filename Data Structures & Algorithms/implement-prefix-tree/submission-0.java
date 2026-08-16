public class PrefixTree {
    Node root;
    public static class Node {
        Map<Character, Node> children;
        char ch;
        boolean isEnd;

        public Node(char c) {
            this.ch = c;
            children = new HashMap<>();
        }
    }
    public PrefixTree() {
         root = new Node('.');
    }

    public void insert(String word) {
        Node cur = root;
        for(char ch: word.toCharArray()) {
            cur.children.putIfAbsent(ch, new Node(ch));
            cur = cur.children.get(ch);
        }
        cur.isEnd=true;
    }

    public boolean search(String word) {
        Node cur = root;
        for(char ch: word.toCharArray()) {
            Node child = cur.children.get(ch);
            if(child==null) return false;
            cur = child;
        }
        return cur.isEnd;
    }

    public boolean startsWith(String prefix) {
     Node cur = root;
        for(char ch: prefix.toCharArray()) {
            Node child = cur.children.get(ch);
            if(child==null) return false;
            cur = child;
        }
        return true;
    }
}
