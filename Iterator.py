  
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, ll=None):
        self.head = None

        if ll:
            for item in reversed(ll): 
                self.insert(item) 

    def __iter__(self):
        def values_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return values_generator()


    def __len__(self):
        return len(list(iter(self)))


    def __get_item__(self, index):
        if index < 0:
            index = len(self) + index

        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError

    def __eq__(self, other):
        return list(iter(self)) == list(iter(other))


    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

    def __str__(self):
        result = ""
        for i in self:
            result += f"( {i} ) -> "
        return result + "None"
if __name__ == "__main__":

    def it():
        for i in range(10):
            yield i

    n = it()

    try:
        for i in range(20):
            print(next(n))
    except StopIteration:
        print("stop")

## add ability to be used in a for in loop

    def iterator():
        i = 0
        while True:
            yield i
            i += 5

    lazy = iterator()
    for i in range(20):
        print(next(lazy))
        