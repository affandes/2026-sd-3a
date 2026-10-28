from collections import deque


class Search:
    def __init__(self, start_node):
        self._start_node = start_node

    def find_target(self, finish_node):
        print("Run: Find Target")

        queue = deque()
        queue.append(self._start_node)
        steps = []

        current_node = queue.pop();
        is_solved = False
        
        while not is_solved:
            print("Loop....: ", current_node)
            if current_node == finish_node:
                is_solved = True
                break;  

            children = current_node.get_children()
            queue.extend(children)
            current_node = queue.pop()