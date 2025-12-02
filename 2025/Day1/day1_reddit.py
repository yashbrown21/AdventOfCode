def part1_arithmatic(input): # Part 1
    current = 50
    password = 0
    for line in input.splitlines():
        if line.startswith("R"):
            number = int(line[1:])
            current = (current + number)%100
        elif line.startswith("L"):
            number = int(line[1:])
            current = abs((current - number)%100)
        if current == 0:
            password += 1
    print(password)

def part1_linked_list(input, current): # Part 1 but with linked list
    password = 0

    for line in input.splitlines():
        dir = line[0]
        num = int(line[1:])
        for _ in range(num):
            if dir == "R":
                current = current.next
            elif dir == "L":
                current = current.prev
        if current.value == 0:
            password += 1
    print(password)

def part2_linked_list(input, current): # Part 2
    password = 0

    for line in input.splitlines():
        dir = line[0]
        num = int(line[1:])
        for _ in range(num):
            if dir == "R":
                current = current.next
            elif dir == "L":
                current = current.prev
            if current.value == 0:
                password += 1
    print(password)

class linkedListNode:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

if __name__ == "__main__":
    f = open(r"Day1\input_d1.txt")
    data = f.read() 
    # linked list of 100 nodes
    head = linkedListNode(0)
    current = head
    for i in range(1, 100):
        newNode = linkedListNode(i)
        current.next = newNode
        newNode.prev = current
        current = newNode
    
    # make it circular
    current.next = head
    head.prev = current
    # set current to node 50
    current = head
    for _ in range(50):
        current = current.next

    part1_arithmatic(data)
    part1_linked_list(data, current)
    part2_linked_list(data, current)

    f.close()