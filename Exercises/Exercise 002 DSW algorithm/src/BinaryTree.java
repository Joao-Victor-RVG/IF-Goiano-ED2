import java.util.ArrayList;
import java.util.Random;

public class BinaryTree {
    private TreeNode root;

    public void insert(int data) {
        root = insertRec(root, data);
    }

    private TreeNode insertRec(TreeNode root, int data) {
        if (root == null) {
            root = new TreeNode(data);
            return root;
        }

        if (data < root.data) {
            root.left = insertRec(root.left, data);
        } else if (data > root.data) {
            root.right = insertRec(root.right, data);
        }

        return root;
    }

    public void printTree() {
        printTree(root, 0);
    }

    private void printTree(TreeNode root, int level) {
        if (root != null) {
            printTree(root.right, level + 1);
            for (int i = 0; i < level; i++) {
                System.out.print("   ");
            }
            System.out.println(root.data);
            printTree(root.left, level + 1);
        }
    }

    public void createRandomArray(int size) {
        Random random = new Random();
        ArrayList<Integer> randomNumbers = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            randomNumbers.add(random.nextInt(101));
        }

        System.out.println("Array of Random Numbers:");
        System.out.println(randomNumbers);
        System.out.println();

        // Build the initial tree with the random numbers
        for (int num : randomNumbers) {
            insert(num);
        }

        System.out.println("Initial Tree:");
        printTree();
        System.out.println();

        // Balance the tree using DSW algorithm
        balanceTree();

        System.out.println("Balanced Tree:");
        printTree();
        System.out.println();

        // Add 20 more random numbers to the tree
        for (int i = 0; i < 20; i++) {
            int newNum = random.nextInt(101);
            randomNumbers.add(newNum);
            insert(newNum);
        }

        System.out.println("Tree after adding 20 more random numbers:");
        printTree();
    }

    private void balanceTree() {
        ArrayList<TreeNode> nodes = new ArrayList<>();
        flattenTree(root, nodes);

        root = null;
        buildBalancedTree(nodes);
    }

    private void flattenTree(TreeNode root, ArrayList<TreeNode> nodes) {
        if (root != null) {
            flattenTree(root.left, nodes);
            nodes.add(root);
            flattenTree(root.right, nodes);
        }
    }

    private void buildBalancedTree(ArrayList<TreeNode> nodes) {
        int n = nodes.size();
        int m = (int) Math.pow(2, Math.floor(Math.log(n + 1) / Math.log(2))) - 1;
        rotateRight(root, n - m);

        for (int i = m; i > 1; i /= 2) {
            rotateLeft(root, i - 1);
        }
    }

    private void rotateRight(TreeNode node, int n) {
        TreeNode temp = node;
        for (int i = 0; i < n; i++) {
            temp = temp.right;
        }
        for (int i = 0; i < n; i++) {
            rotateRightOnce(node);
        }
    }

    private void rotateLeft(TreeNode node, int n) {
        TreeNode temp = node;
        for (int i = 0; i < n; i++) {
            temp = temp.right;
        }
        for (int i = 0; i < n; i++) {
            rotateLeftOnce(node);
        }
    }

    private void rotateRightOnce(TreeNode node) {
        TreeNode child = node.left;
        node.left = child.right;
        child.right = node;
        node = child;
    }

    private void rotateLeftOnce(TreeNode node) {
        TreeNode child = node.right;
        node.right = child.left;
        child.left = node;
        node = child;
    }
}
