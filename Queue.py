class Node(object):
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

class Queue(object):
    def __init__(self):
        self.head = None
        self.rear = None
    
    def is_empty(self):
        return self.head is None

    def enqueue(self,elem):
        p = Node(elem)
        if self.is_empty():
            self.head = p
            self.rear = p
        else:
            self.rear.next = p
            self.rear = p

    def dequeue(self):
        if self.is_empty():  # 判断队列是否为空
            print('Queue_is_empty')  # 若队列为空，则退出 dequeue 操作
        else:
            result = self.head.elem  # result为队列头部元素
            self.head = self.head.next  # 改变队列头部指针位置
            return result  # 返回队列头部元素

    def peek(self):
        if self.is_empty():  # 判断队列是否为空
            print('NOT_FOUND')  # 为空则返回 NOT_FOUND
        else:
            return self.head.elem  # 返回队列头部元素

    def print_queue(self):
        print("queue:")
        temp = self.head
        myqueue = []  # 暂时存放队列数据
        while temp is not None:
            myqueue.append(temp.elem)
            temp = temp.next
        print(myqueue)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(21)
    queue.enqueue(35)
    queue.enqueue(58)
    queue.enqueue(13)
    queue.print_queue()
    print(queue.peek())
    queue.dequeue()
    queue.print_queue()
    print(queue.peek())