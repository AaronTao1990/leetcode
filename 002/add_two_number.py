
class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

def gen_list(values):
    last_node = None
    head = None
    for value in values:
        head = ListNode(value)
        head.next = last_node
        last_node = head
    return head

def print_list(node_list):
    p = node_list
    while p.next is not None:
        print p.val
        p = p.next
    print p.val

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        promote = 0
        last_node = None
        head = None
        p1 = l1
        p2 = l2
        while p1 is not None or p2 is not None:
            value = None
            if p1 is None:
                value = (p2.val + promote)%10
                promote = (p2.val + promote)/10
            elif p2 is None:
                value = (p1.val + promote)%10
                promote = (p1.val + promote)/10
            else:
                value = (p1.val + p2.val + promote)%10
                promote = (p1.val + p2.val + promote)/10
            new_node = ListNode(value)
            if head is None:
                head = new_node
            else:
                last_node.next = new_node
            last_node = new_node

            p1 = p1.next if p1 is not None else None
            p2 = p2.next if p2 is not None else None

        if promote != 0:
            new_node = ListNode(promote)
            last_node.next = new_node

        return head

def main():
    l1 = gen_list([1])
    l2 = gen_list([9, 9])
    result = Solution().addTwoNumbers(l1, l2)
    print_list(result)

if __name__ == '__main__':
    main()
