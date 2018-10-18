from board import list1
def find_total(x1, y1, x2,y2):
    ans=abs(x2-x1+y2-y1)
    print(ans)

x1,y1,x2,y2 = raw_input().split()
d1={x1:y1}
d2={x2:y2}
if (not(d1 in list1)):
    print('-1')
elif (not(d2 in list1)):
    print('-1')
else:       
    x1=int(x1)
    x2=int(x2)
    y1=int(y1)
    y2=int(y2)

    if(x2>=x1 and y2>=y1):
       find_total(x1,y1,x2,y2)
    else:
       print('-1')
    
