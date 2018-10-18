
def board_total(x1,y1,x2,y2):
    count=2
    for i in range(x1+1,x2):
        for j in range(y1+1,y2):
                if((y2-y1)*(i-x1)==(j-y1)*(x2-x1)):
                    count=count+1
    print count

x1,y1,x2,y2 = raw_input().split()
x1=int(x1)
x2=int(x2)
y1=int(y1)
y2=int(y2)

board_total(x1,y1,x2,y2)


