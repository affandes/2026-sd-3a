class Node:
    """Kelas untuk merepresentasikan simpul (node) pada Pohon Biner."""
    def __init__(self, value):
        self.value = value
        self.left = None   # Rujukan ke sub-pohon kiri
        self.right = None  # Rujukan ke sub-pohon kanan


# 1. Pre-Order Traversal (Root -> Left -> Right)
def pre_order(node):
    if node is None:
        return
    print(node.value, end=" ")   # Kunjungi Root
    pre_order(node.left)         # Penelusuran Sub-pohon Kiri
    pre_order(node.right)        # Penelusuran Sub-pohon Kanan


# 2. In-Order Traversal (Left -> Root -> Right)
def in_order(node):
    if node is None:
        return
    in_order(node.left)          # Penelusuran Sub-pohon Kiri
    print(node.value, end=" ")   # Kunjungi Root
    in_order(node.right)         # Penelusuran Sub-pohon Kanan


# 3. Post-Order Traversal (Left -> Right -> Root)
def post_order(node):
    if node is None:
        return
    post_order(node.left)         # Penelusuran Sub-pohon Kiri
    post_order(node.right)        # Penelusuran Sub-pohon Kanan
    print(node.value, end=" ")   # Kunjungi Root

# --- Contoh Penggunaan ---
if __name__ == "__main__":
    # Membangun struktur pohon biner contoh:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Pre-order Traversal  :", end=" ")
    pre_order(root)
    print()

    print("In-order Traversal   :", end=" ")
    in_order(root)
    print()

    print("Post-order Traversal :", end=" ")
    post_order(root)
    print()