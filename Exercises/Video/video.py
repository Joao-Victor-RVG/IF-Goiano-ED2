import time
import ast


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def update_height(node):
    if not node:
        return 0
    node.height = 1 + max(height(node.left), height(node.right))
    return node.height

def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def left_rotate(y):
    x = y.right
    T2 = x.left

    x.left = y
    y.right = T2

    update_height(y)
    update_height(x)

    return x

def right_rotate(x):
    y = x.left
    T2 = y.right

    y.right = x
    x.left = T2

    update_height(x)
    update_height(y)

    return y

def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    update_height(root)

    balance = balance_factor(root)

    # Left Heavy
    if balance > 1:
        if root.left and key < root.left.key:
            return right_rotate(root)
        else:
            if root.left:
                root.left = left_rotate(root.left)
            return right_rotate(root)

    # Right Heavy
    if balance < -1:
        if root.right and key > root.right.key:
            return left_rotate(root)
        else:
            if root.right:
                root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def inorder_traversal(root):
    result = []
    if root:
        result += inorder_traversal(root.left)
        result.append(root.key)
        result += inorder_traversal(root.right)
    return result

def avl_sort(data):
    root = None
    for num in data:
        if isinstance(num, list):
            for element in num:
                root = insert(root, element)
        else:
            root = insert(root, num)

    return inorder_traversal(root)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# ... (o código anterior permanece inalterado)

if __name__ == "__main__":
    # Leitura do arquivo
    with open("dados500_mil.txt", "r") as file:
        data = []
        for line in file:
            numbers = ast.literal_eval(line.strip())
            data.extend(numbers)

    # Medição do tempo para AVL
    start_time_avl = time.time()
    avl_sorted_data = avl_sort(data)
    end_time_avl = time.time()
    avl_time = end_time_avl - start_time_avl

    # Medição do tempo para Merge Sort
    start_time_merge_sort = time.time()
    merge_sorted_data = merge_sort(data)
    end_time_merge_sort = time.time()
    merge_sort_time = end_time_merge_sort - start_time_merge_sort

    # Medição do tempo para Quicksort
    start_time_quicksort = time.time()
    quick_sorted_data = quicksort(data)
    end_time_quicksort = time.time()
    quicksort_time = end_time_quicksort - start_time_quicksort

    # Impressão dos resultados e tempos
    print("Árvore AVL:")
    print(f"Tempo para ordenação com AVL: {avl_time} segundos\n")

    print("Merge Sort:")
    print(f"Tempo para ordenação com Merge Sort: {merge_sort_time} segundos\n")

    print("Quicksort:")
    print(f"Tempo para ordenação com Quicksort: {quicksort_time} segundos")
