#graph - Breadth First Search
a7=[]
a5=[]
a4=[]
a10=[]
a13=[]
a14=[]
a15=[]
a12=[a14,a15]
a11=[a12,a13]
a6=[a11]
a2=[a4,a5,a6]
a9=[a14]
a8=[a9,a10]
a3=[a7,a8]
a1=[a2,a3]

my_queue=[]
num=0


def enq(data,queue=my_queue):
    queue.append(data)

def deq(queue=my_queue):
    return queue.pop(0)

def vis(data):
    global num
    num+=1
    visitation=(num,"Visited")
    data.append(visitation)

enq(a1)
vis(a1)

while len(my_queue) != 0:
    my_node=deq()
    for i in my_node:
        if "Visited" not in i:
            vis(i)
            enq(i)

print(a1)
'''
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)
print(a9)
print(a10)
print(a11)
print(a12)
print(a13)
print(a14)
print(a15)
'''
