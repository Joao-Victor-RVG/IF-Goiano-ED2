import java.util.Random;

public class Main {
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        Random random = new Random();


        for (int i = 0; i < 20; i++) {
            int randomNumber = random.nextInt(101);
            System.out.print(randomNumber + " ");
            tree.insert(randomNumber);
        }

        System.out.println("\n\nImpressão em Pré-ordem:");
        tree.preOrderTraversal(tree.root);

        System.out.println("\n\nImpressão em Ordem:");
        tree.inOrderTraversal(tree.root);

        System.out.println("\n\nImpressão em Pós-ordem:");
        tree.postOrderTraversal(tree.root);

        System.out.println("\n\nImpressão em Nível:");
        tree.levelOrderTraversal();


        for (int i = 0; i < 5; i++) {
            int elementToBeRemoved = random.nextInt(101);
            System.out.println("\n\nRemovendo o elemento " + elementToBeRemoved);
        }

        System.out.println("\n\nApós a remoção, Impressão em Pré-ordem:");
        tree.preOrderTraversal(tree.root);

        System.out.println("\n\nApós a remoção, Impressão em Ordem:");
        tree.inOrderTraversal(tree.root);

        System.out.println("\n\nApós a remoção, Impressão em Pós-ordem:");
        tree.postOrderTraversal(tree.root);

        System.out.println("\n\nApós a remoção, Impressão em Nível:");
        tree.levelOrderTraversal();
    }
}
