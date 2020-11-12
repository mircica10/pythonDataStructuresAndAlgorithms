class List:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def printList(self, list):
        res = ''
        if list is None:
            return ''
        while list is not None:
            res += str(list.val) + ','
            list = list.next
        return res[0:len(res) - 1]

    def reverseListHelper(self, list):
        if list.next is None:
            return (list, list)
        (prev, root) = self.reverseListHelper(list.next)
        prev.next = list
        list.next = None
        return (list, root)
  
    def reverseList(self, list):
        (list, root) = self.reverseListHelper(list)
        return root

    def sortList(self, list):
        swap = True
        while swap == True:
            swap = False  
            index = list              
            while index.next is not None:
                if index.val > index.next.val:
                    aux = index.val
                    index.val = index.next.val
                    index.next.val = aux
                    swap = True       
                index = index.next
        return list

    def deleteDuplicates(self, list):
        index = list
        while index.next is not None:
            if index.next is not None and index.val == index.next.val:
                index.next = index.next.next
                index = index.next
            index = index.next
        return list
            


def initTest():
    l7 = List(9)
    l6 = List(2, l7)
    l5 = List(3, l6)
    l4 = List(4, l5)
    l3 = List(5, l4)
    l2 = List(2, l3)
    l1 = List(1, l2)
    return l1

l1 = initTest()
assert('1,2,5,4,3,2,9' == l1.printList(l1) )
# l1.printList(l1)
l = l1.reverseList(l1)
assert('9,2,3,4,5,2,1' == l1.printList(l))
l1 = initTest()
l = l1.sortList(l1)
assert('1,2,2,3,4,5,9' == l1.printList(l))
l1 = initTest()
l = l1.sortList(l1)
l2 = l.deleteDuplicates(l)
assert('1,2,3,4,5,9' == l2.printList(l2))


                

