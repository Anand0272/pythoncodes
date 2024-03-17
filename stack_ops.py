l=[]
while True:
    c=int(input('''
        1. Push element
        2. Pop element
        3. Peek element
        4. Display Stack
        5. Exit
        Enter your choice:
            '''))
    if c==1:
        ele=input("Enter element to push: ")
        l.append(ele)
    elif c==2:
        if len(l)==0:
            print("Stack is empty!")
        else:
            print(l.pop(-1))
    elif c==3:
        if len(l)==0:
            print("Stack is empty!")
        else:
            print(l[-1])
    elif c==4:
        print(l)
    elif c==5:
        break
    else:
        print("Enter valid choice:")
