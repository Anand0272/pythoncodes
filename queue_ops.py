l=[]

while True:
    c=int(input(
        '''
            1. Enqueue: Adds an item to the queue
            2. Dequeue: Removes and item from the queue
            3. Front: Get the front item from the queue
            4. Rear: Get the last item from queue
            5. Exit
        Enter your choice:
        '''
    ))

    if c==1:
        item=input("Enter element: ")
        l.append(item)

    elif c==2:
        if(len(l)==0):
            print("Queue is empty!")
        else:
            