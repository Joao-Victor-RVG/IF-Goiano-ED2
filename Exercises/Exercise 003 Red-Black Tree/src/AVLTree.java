class AVLTree {
    public Node root;

    public void delete(int randomNumber) {
    }

    public void search(int randomNumber) {
    }

    public static class Node {
        int key;
        int height;
        Node left, right;

        public Node(int key) {
            this.key = key;
            this.height = 1;
        }
    }
    public void insert(int key) {
        root = insert(root, key);
    }

    public Node insert(Node node, int key) {
        if (node == null) {
            return new Node(key);
        }

        if (key < node.key) {
            node.left = insert(node.left, key);
        } else if (key > node.key) {
            node.right = insert(node.right, key);
        } else {
            return node;
        }

        node.height = 1 + Math.max(height(node.left), height(node.right));

        int balance = getBalance(node);


        if (balance > 1 && key < node.left.key) {
            return rotateRight(node);
        }


        if (balance < -1 && key > node.right.key) {
            return rotateLeft(node);
        }


        if (balance > 1 && key > node.left.key) {
            node.left = rotateLeft(node.left);
            return rotateRight(node);
        }


        if (balance < -1 && key < node.right.key) {
            node.right = rotateRight(node.right);
            return rotateLeft(node);
        }

        return node;
    }
    

    public int height(Node node) {
        return (node == null) ? 0 : node.height;
    }

    public int getBalance(Node node) {
        return (node == null) ? 0 : height(node.left) - height(node.right);
    }

    public Node rotateRight(Node y) {
        Node x = y.left;
        Node T2 = x.right;
        
        x.right = y;
        y.left = T2;
        
        y.height = 1 + Math.max(height(y.left), height(y.right));
        x.height = 1 + Math.max(height(x.left), height(x.right));

        return x;
    }

    public Node rotateLeft(Node x) {
        Node y = x.right;
        Node T2 = y.left;
        
        y.left = x;
        x.right = T2;
        
        x.height = 1 + Math.max(height(x.left), height(x.right));
        y.height = 1 + Math.max(height(y.left), height(y.right));

        return y;
    }
}
