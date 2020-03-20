from collections import deque


class Node():
    """
    Represent a Node in a tree data structure
    Args:
        data (Rectangle): A Rectangle object
    Attributes:
        data (Rectangle): A Rectangle object
        next (list): list of Node objects. These are immediate inner rectangles

    """
    def __init__(self, data=None):
        self.data = data
        self.next = []

    def __str__(self):
        return f"<{self.data}>"

    def __repr__(self):
        return self.__str__()


class LinkedList():
    """
    Implementation of n-arry tree based on linkedlist data structure
    Args:
        rectangles (list): List of Rectangle objects to add
    Attributes:
        head (Node): Node at the most top level, which is always a sea
        rectangles (list):  List of Rectangle objects, based on area
    Notes:
        you can use add_rectangle() function to add Rectangle objects one by one after instantiation a LinkeList object
        ll = LinkedList([Rectangle([1,1,5,5])])
        ll.add_rectangle(Rectangle([2,2,4,4]))

    """
    def __init__(self, rectangles):
        self.head = Node('head')
        self.__rectangles = rectangles
        self.__create_tree(self.__rectangles)

    def __create_tree(self, rectangles):
        """
        It adds rectangles to the tree structure.
        Args:
            rectangles (list):  descending list of Rectangle objects, based on area

        """
        for rectangle in rectangles:
            self.add_rectangle(rectangle)

    def add_rectangle(self, data):
        """
        Adds given rectangle to the LinkedList tree
        Args:
            data (Rectangle): Rectangle object to add to the LinkedList object
            Raises:
                ValueError: if 2 rectangles intersect with each other partially OR sharing same boundary.
        """
        # get head which is always sea
        curr = self.head
        n = Node(data)
        # if the head has no rectangle in it add the rectangle to its next list of immediate neighbours
        if not curr.next:
            curr.next.append(n)
            return
        # otherwise iterate over the other Nodes in the next list
        # and check if the current rectangle is immediately inside or outside any of them.
        else:
            candidate = curr
            remove_from_next = []
            while curr:
                for idx, child in enumerate(curr.next):
                    # if there is a rectangle with same coordination points do nothing
                    if child.data == data:
                        return

                    # rectangles must not overlap. This is important condition to be able to tag them as a land or sea.
                    # If the current rectangle overlaps with any rectangle we should raise exception
                    if child.data & data:
                        raise ValueError(f"{child.data} and {data} are overlapped")

                    # if the rectangle is outside an already existing rectangle in the data structure,
                    # take the rectangle as immediate outer neighbour of existing one
                    # AND remove the existing one from its previous parent 'next' list
                    if child.data < data:
                        n.next.append(child)
                        remove_from_next.append(child)
                        if idx == len(curr.next) - 1:
                            curr = None
                        continue

                    # if the rectangle is inside an already existing rectangle in the data structure,
                    # take the existing rectangle as candidate to be immediate outer neighbour
                    # then iterate over existing rectangle's child in the 'next' list
                    if child.data > data:
                        candidate = child
                        curr = None
                        # if current child node has some child itself we need to check them as well,
                        # to find immediate outer rectangle
                        if child.next:
                            curr = child
                        break
                    if idx == len(curr.next) - 1:
                        curr = None

            # Finally add the rectangle as a next node of its immediate outer neighbour (parent)
            candidate.next.append(n)
            candidate.next = [i for i in candidate.next if i not in remove_from_next]
            return

    def bfs(self):
        """
        Implementation of BFS to traverse LinkedList tree and finding nodes at each level
        Returns:
            dict: Key is the level and value is List of Node objects at that level
            int: number of nodes identified as a land

        """
        no_of_lands = 0
        root = self.head
        if not root:
            return []

        queue = deque(root.next)
        result = {}
        level = 0
        while len(queue):
            level += 1
            level_result = []
            for i in range(len(queue)):
                node = queue.popleft()
                level_result.append(node)
                if level % 2 != 0:
                    no_of_lands += 1
                for child in node.next:
                    queue.append(child)
            result[level] = level_result

        return result, no_of_lands

    def __str__(self):
        result, no_of_lands = self.bfs()
        return str(f"Tree Structure:\n{result}\n\nNumber of lands: {no_of_lands}")

    def __repr__(self):
        return self.__str__()
