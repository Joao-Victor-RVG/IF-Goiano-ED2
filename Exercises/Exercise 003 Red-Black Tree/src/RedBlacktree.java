class RedBlackTree {
    public static final boolean BLACK = false;
    public static final boolean RED = true;

    public Node root;

    public void delete(int randomNumber) {
    }

    public void search(int randomNumber) {
    }

    public static class Node {
        int key;
        Node left, right;
        boolean color;

        public Node(int key, boolean color) {
            this.key = key;
            this.color = color;
        }
    }
    

 
    public void insert(int key) {
        root = insert(root, key);
        root.color = BLACK; 
    }

    public Node insert(Node node, int key) {
        if (node == null) {
            return new Node(key, RED);
        }

        if (key < node.key) {
            node.left = insert(node.left, key);
        } else if (key > node.key) {
            node.right = insert(node.right, key);
        } else {
            node.key = key;
        }


        if (isRed(node.right) && !isRed(node.left)) {
            node = rotateLeft(node);
        }
        if (isRed(node.left) && isRed(node.left.left)) {
            node = rotateRight(node);
        }
        if (isRed(node.left) && isRed(node.right)) {
            flipColors(node);
        }

        return node;
    }

    public boolean isRed(Node node) {
        return node != null && node.color == RED;
    }

    public Node rotateLeft(Node h) {
        Node x = h.right;
        h.right = x.left;
        x.left = h;
        x.color = h.color;
        h.color = RED;
        return x;
    }

    public Node rotateRight(Node h) {
        Node x = h.left;
        h.left = x.right;
        x.right = h;
        x.color = h.color;
        h.color = RED;
        return x;
    }

    public void flipColors(Node h) {
        h.color = RED;
        h.left.color = BLACK;
        h.right.color = BLACK;
    }

}
