import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

        int[] data = readDataFromFile();

        long rbStartTime = System.currentTimeMillis();
        RedBlackTree redBlackTree = new RedBlackTree();
        assert data != null;
        for (int key : data) {
            redBlackTree.insert(key);
        }
        long rbEndTime = System.currentTimeMillis();
        long rbExecutionTime = rbEndTime - rbStartTime;
        System.out.println("Tempo para preenchimento da árvore Rubro-Negra: " + rbExecutionTime + " ms");


        long avlStartTime = System.currentTimeMillis();
        AVLTree avlTree = new AVLTree();
        for (int key : data) {
            avlTree.insert(key);
        }
        long avlEndTime = System.currentTimeMillis();
        long avlExecutionTime = avlEndTime - avlStartTime;
        System.out.println("Tempo para preenchimento da árvore AVL: " + avlExecutionTime + " ms");


        Random random = new Random();
        for (int i = 0; i < 50000; i++) {
            int randomNumber = random.nextInt(19999) - 9999;

            if (randomNumber % 3 == 0) {
                redBlackTree.insert(randomNumber);
                avlTree.insert(randomNumber);
            } else if (randomNumber % 5 == 0) {
                redBlackTree.delete(randomNumber);
                avlTree.delete(randomNumber);
            } else {
                redBlackTree.search(randomNumber);
                avlTree.search(randomNumber);
            }
        }


        System.out.println("\nComparativo de Tempo:");
        System.out.println("Árvore Rubro-Negra: " + rbExecutionTime + " ms");
        System.out.println("Árvore AVL: " + avlExecutionTime + " ms");

    }

    private static int[] readDataFromFile() {
        try (BufferedReader br = new BufferedReader(new FileReader("../data.txt"))) {
            String line;
            int count = 0;
            int[] data = new int[100000];

            while ((line = br.readLine()) != null && count < 100000) {
                data[count++] = Integer.parseInt(line.trim());
            }

            return data;
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
}
