
#Make a squence of strings of A and B , no of A's and B's will be provided with maximum occurence of the letter in a substring


def stringmaker(counta,countb,maxa,maxb):
    li=[]
    if counta >= countb:
        for i in range(counta+countb):
            if maxa <= counta:
                for j in range(maxa):
                    li.append('A')
            elif maxa > counta:
                for j in range(counta):
                    li.append('A') 
            if maxb <= countb:
                for j in range(maxb):
                    li.append('B')
            elif maxb > countb:
                for j in range(countb):
                    li.append('B') 

    elif counta < countb:
        for i in range(counta+countb):
            if maxb <= countb:
                for j in range(maxb):
                    li.append('B')
            elif maxb > countb:
                for j in range(countb):
                    li.append('B') 
            if maxa <= counta:
                for j in range(maxa):
                    li.append('A')
            elif maxa > counta:
                for j in range(counta):
                    li.append('A')        
    st=''
    for l in li:
        st=st+l
    st=st[0:(counta+countb)]
    print(st)
    print(len(st))











def getOptimalStringLength(countA, countB, maxA, maxB):
    var=''
    CA=0
    CB=0
    totalA=0
    totalB=0  
    if countA>=countB:
      
        for i in range(countA+countB):
            
            if CA<maxA  and totalA<countA:
                var+='A'
                CA+=1
                CB=0
                totalA+=1
            elif CB<maxB and totalB<countB:
                var+='B'
                CB+=1
                CA=0
                totalB+=1
    elif countA<=countB:

        for i in range(countA+countB):
            
            
            if CB<maxB and totalB<countB:
                var+='B'
                CB+=1
                CA=0
                totalB+=1
            
            elif CA<maxA  and totalA<countA:
                var+='A'
                CA+=1
                CB=0
                totalA+=1
            
    print(var)
    print(len(var))



ca=int(input('?'))
cb=int(input('?'))
ma=int(input('?'))
mb=int(input('?'))

stringmaker(ca,cb,ma,mb)

getOptimalStringLength(ca,cb,ma,mb)



    
