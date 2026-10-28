from code03_puzzle_slider.model.tile import Tile
from code03_puzzle_slider.model.tree_node import TreeNode
from code03_puzzle_slider.service.search import Search


def main():
    print("Run...")

    start_tile = Tile([1,2,6,5,4,7,8,3,0])
    finish_tile = Tile([1,2,3,4,5,6,7,8,0])
    
    start_node = TreeNode(start_tile)
    finish_node = TreeNode(finish_tile)

    search = Search(start_node)
    search.find_target(finish_node)
    
if __name__ == "__main__":
    main()