# 链表
class LinkNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# 算法
# 判断链表是否循环
def is_cycle(head: LinkNode):
    """根据追击问题, 设定两个不同速度的指针, 若其能碰到, 则说明具备环

    :param head: 链表头结点
    :return: 是否存在环
    """
    p1 = p2 = head
    while p1.next and p2.next.next:
        if p1.next == p2.next.next:
            return True
        p1 = p1.next
        p2 = p2.next.next
    return False


# 求环的长度
def cycle_length(head: LinkNode):
    """第二次相遇 - 第一次相遇 时的循环次数则为环长

    :param head: 链表头结点
    :return: 环长度
    """
    p1 = p2 = head
    flag = 0
    length = 0
    while p1.next and p2.next.next:
        if p1.next == p2.next.next:
            flag += 1  # 两指针相遇次数
            if flag == 2:
                break
        if flag > 0:
            length += 1
        p1 = p1.next
        p2 = p2.next.next

    return length


# 求环的起点
def cycle_origin(head: LinkNode):
    """
    两指针分别从起点和首次相遇点每次向前移动一格, 则相遇点则为环的起点
    :param head: 头指针
    :return: 位置
    """
    # 求首次相遇点
    def first_point(head: LinkNode):
        p1 = p2 = head
        while p1.next and p2.next.next:
            if p1.next == p2.next.next:
                return p1.next
            p1 = p1.next
            p2 = p2.next.next

    p2 = first_point(head)
    p1 = head
    while 1:
        if p1.next == p2.next:
            return p1.next
        p1 = p1.next
        p2 = p2.next


if __name__ == '__main__':
    node1 = LinkNode(5)
    node2 = LinkNode(3)
    node3 = LinkNode(7)
    node4 = LinkNode(2)
    node5 = LinkNode(6)
    node6 = LinkNode(8)
    node7 = LinkNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node4
    # 5-3-7-2-6-8-1-2
    print(is_cycle(node1))
    print("环长: ", cycle_length(node1))
    print("起点: ", cycle_origin(node1).value)

