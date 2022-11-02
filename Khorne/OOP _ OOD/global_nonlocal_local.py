#GLOBAL DATA
a="AAA"
x="XXX"
y="YYY"
z="ZZZ"

def upper():
    global a #global a gets altered to - 111
    a=111 #this is now global
    x=222
    y=333
    z=444
    
    def middle():
        global a #global a gets altered again to -1
        global x #global a gets altered again to -2
        a=1 #this is now global
        x=2 #this is now global
        nonlocal y
        y=3
        #global z
        z=4
        
        def lower():
            a="one"
            #nonlocal a/x - returns Syntax error when non local used for a global variable
            x="two"
            nonlocal y #non local y gets assigned for the enclosed block middle()'s : y to -"three"
            y="three" #this is now nonlocal
            global z #only global z gets altered to -"four"
            z="four" #this is now global
            #nonlocal b - returns Syntax error assigning a nonlocal variable that is not present in the enclosed block
            b=1898

            print('Lower ',a,x,y,z,b)
            
        lower()
        print('Middle ',a,x,y,z)

    middle() 
    print('Upper ',a,x,y,z)

upper()
print('Global ',a,x,y,z)


#///////////////////////////////////////////////////////////////////////////////////////////////////


#upper()
# middle() #nested functions must be called inside the defined functions.
