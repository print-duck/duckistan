'''
QUEUE, two terminal ends, LILO
ENQUEUE and DEQEUE
'''
a=[1, 2, 3, 4, 54, 343, 232]
#let a be the queue structure
print('''
a - is the Queue,
Enqueue operation:
enq(name_of_queue,data_to_enqueue),
Dequeue operation:
deq(name_of_queue)
''')
#Enqueue operation: adding data at the back of queue
def enq(queue, enq_dat):
    queue.append(enq_dat)

def deq(queue):
    queue.pop(0)
