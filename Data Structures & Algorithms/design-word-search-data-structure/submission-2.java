class WordDictionary {
    Node root;
    public static class Node {
        boolean isEnd;
        Map<Character, Node> children;
        char ch;

        public Node(char c) {
            ch=c;
            children= new HashMap<>();
        }
    }
    public WordDictionary() {
        root = new Node('#');
    }

    public void addWord(String word) {
        Node cur = root;
        for(char ch: word.toCharArray()) {
            cur.children.putIfAbsent(ch, new Node(ch));
            cur = cur.children.get(ch);
        }
        cur.isEnd=true;
    }

    public boolean search(String word) {
         return dfs(word,0, root);   
    }

    public boolean dfs(String word, int pos, Node root) {
        Node cur = root;
        for(int i=pos;i<word.length();i++) {
            char ch = word.charAt(i);
            if(ch!='.' && cur.children.containsKey(ch)) {
                cur = cur.children.get(ch);
            } else if(ch!='.' && !cur.children.containsKey(ch)) {
                return false;
            } else if(ch=='.') {
                for(char wc: cur.children.keySet()) {
                    if(dfs(word, i+1, cur.children.get(wc))) {
                        return true;
                    }
                }
                return false;
            }
        }
        return cur.isEnd;

    }
}
