mode=input()
if mode == 'even':
    counter=0
    value=1
    n=input()
    while True:
        if counter == int(n):
            break
        else:
            if value%2 == 0:
                print(value)
                counter += 1
                
            elif value%2 != 0:
                pass

            value+=1

elif mode == 'odd':
    counter=0
    value=1
    while True:
        if counter == int(input()):
            break
        else:
            if value%2 != 0:
                print(value)
                counter += 1
            elif value%2 == 0:
                pass

            value+=1
        counter +=1
