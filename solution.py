from typing import TypeVar, Tuple  # For use in type hinting

# Type Declarations
T = TypeVar('T')  # generic type
SLL = TypeVar('SLL')  # forward declared
Node = TypeVar('Node')  # forward declare `Node` type


class SLLNode:
    """
    Node implementation
    Do not modify.
    """

    __slots__ = ['val', 'next']

    def __init__(self, value: T, next: Node = None) -> None:
        """
        Initialize an SLL Node
        :param value: value held by node
        :param next: reference to the next node in the SLL
        :return: None
        """
        self.val = value
        self.next = next

    def __str__(self) -> str:
        """
        Overloads `str()` method to cast nodes to strings
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __repr__(self) -> str:
        """
        Overloads `repr()` method for use in debugging
        return: string
        """
        return '(Node: ' + str(self.val) + ' )'

    def __eq__(self, other: Node) -> bool:
        """
        Overloads `==` operator to compare nodes
        :param other: right operand of `==`
        :return: bool
        """
        return self is other if other is not None else False


class RecursiveSinglyLinkedList:
    """
    Recursive implementation of an SLL
    """

    __slots__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        :return: None
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        """
        return self.to_string(self.head)

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right hand operand of `==`
        :return: `True` if equal, else `False`
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    # ============ Modify below ============ #

    def push(self, value: T, back: bool = True) -> None:
        """
        Appends or prepends a new SLL node to an existing linked list
        :param value: value to push to the list
        :param back: appends to end of list unless set to false
        :return: None
        """
        new_node = SLLNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node

        elif back == True:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def to_string(self, curr: Node) -> str:
        """
        Converts an SLL to a printable string
        :param curr: the node currently being evaluated and added to the return line
        :return: string representation of the linked list
        """

        if self.head == None:
            return "None"

        if curr.next != None:
            return str(curr.val + " --> " + self.to_string(curr.next))

        else:
            return curr.val

    def length(self, curr: Node) -> int:
        """
        Counts the number of nodes present in a linked list
        :param curr: the node currently being evaluated and added to the return line
        :return: an int representing the number of nodes in a linked list
        """
        if self.head == None:
            return 0

        if curr.next != None:
            return 1 + self.length(curr.next)

        else:
            return 1

    def sum_list(self, curr: Node) -> T:
        """
        Adds all values of each node present in an SLL
        :param curr: the node currently being evaluated and added to the return line
        :return: the sum of all node values
        """
        if self.head == None:
            return None

        if curr.next != None:
            return curr.val + self.sum_list(curr.next)

        else:
            return curr.val

    def search(self, value: T) -> bool:
        """
        Looks for a specific value within an SLL; outer ensures SLL is not empty
        :param value: val to be searched for in SLL
        :return: True boolean if value is found, False if not
        """
        if self.head == None:
            return False

        def search_inner(curr: Node) -> bool:
            """
            Inner search function to find value passed by outerfunction
            :param curr: the node currently being evaluated
            :return: boolean value True if value is found, False otherwise and a recursive call to search inner \
                if necessary
            """
            if curr.val != value and curr.next != None:
                return search_inner(curr.next)
            elif value == curr.val:
                return True
            else:
                return False

        return search_inner(self.head)

    def count(self, value: T) -> int:
        """
        Determines the number of times value appears in an SLL; outer ensures not empty
        :param value: the value to search for in the SLL
        :returns: an int specifying the number of times value appears in a SLL
        """
        if self.head == None:
            return 0

        def count_inner(curr: Node) -> int:
            """
            Inner function of count to determine the number of times value appears in an SLL
            :param curr: the node currently being evaluated and added to the return line
            :returns: either a 1 or 0 and a recursive call to count_inner if necessary
            """
            if curr.val == value:
                if curr.next != None:
                    return 1 + count_inner(curr.next)
                else:
                    return 1
            elif curr.next != None:
                return 0 + count_inner(curr.next)
            else:
                return 0

        return count_inner(self.head)

    def remove(self, value: T) -> bool:
        """
        Removes the first iteration of param value in a SLL; outer ensures list is not empty
        :param value: the value to be searched for in an SLL
        :returns: True if value is found and removed, false otherwise
        """
        if self.head == None:
            return False

        def remove_inner(curr: Node) -> Tuple[Node, bool]:
            """
            Inner function of remove. Iterates through SLL recursively looking for value
            :param curr: the node currently being evaluated
            :returns: True if value is found and removed. False otherwise & potential recursive call
            """
            if curr.val == value and curr == self.head:  # remove at head
                self.head = curr.next
                if self.head == None:
                    self.tail = None
                return True

            elif curr.next != None and curr.next.val == value:  # remove others
                if curr.next == self.tail:  # reset tail when removed at end
                    self.tail = curr
                curr.next = curr.next.next
                return True

            elif curr == self.tail:
                return False

            else:
                return remove_inner(curr.next)

        return remove_inner(self.head)

    def remove_all(self, value: T) -> bool:
        """
        Removes all instances of the specified value from an SLL; Calls remove_all_inner
        :param value: the value to be removed from an SLL
        :returns: boolean True if value found and removed, otherwise False
        """
        if self.head == None:
            return False

        def remove_all_inner(curr: Node) -> Tuple[Node, bool]:
            """
            Inner function of remove_all; rids SLL of specified value
            :param curr: the current node being used to check values
            :returns: a tuple of a boolean and the header node of the SLL
            """
            if curr.val == value and curr == self.head:  # remove at head
                self.head = curr.next
                if self.head == None:  # 1 element in list
                    self.tail = None
                    return (self.head, True)
                remove_all_inner(curr.next)  # remove head & check rest of SLL (not len == 1)
                return (self.head, True)

            elif curr.next != None and curr.next.val == value:  # remove others
                if curr.next == self.tail:  # reset tail when removed at end
                    self.tail = curr
                    curr.next = None
                    return (self.head, True)
                curr.next = curr.next.next
                remove_all_inner(curr.next)
                return (self.head, True)

            elif curr == self.tail:  # end of list w/out removal
                return (self.head, False)

            else:
                return remove_all_inner(curr.next)

        return remove_all_inner(self.head)[1]


def reverse(data: SLL, curr: Node) -> None:
    """
    Reverse the elements in an SLL; recursive
    :param data: SLL to be reversed
    :param curr: current node being evaluated by the function
    :returns: None; list is reversed but nothing is returned
    """
    if curr == None:  # list is empty
        return

    next = curr.next

    if next == None:  # ends recursion when last node is in sight
        data.head = curr
        return

    if curr == data.head:  # sets tail on first iteration
        data.tail = curr

    reverse(data, next)
    next.next = curr
    curr.next = None
