#print("Enter the first coordinate : ")
#x1=int(input())
#y1=int(input()) 
c1=input("Enter the first coordinate : ")
c2=input("Enter the second coordinate : ")
c3=input("Enter the third coordinate : ")
c4=input("Enter coordinates of the key : ")
x1=float(c1.split()[0])
y1=float(c1.split()[1])
x2=float(c2.split()[0])
y2=float(c2.split()[1])
x3=float(c3.split()[0])
y3=float(c3.split()[1])
x4=float(c4.split()[0])
y4=float(c4.split()[1])
def insideOut(x1,x2,x3,x4,y1,y2,y3,y4):
    if(x1-x2 == 0):
        flag=(((y3-y1)/(x3-x1))*x4-y4+y1-((y3-y1)/(x3-x1))*x1)*(((y3-y2)/(x3-x2))*x4-y4+y3-((y3-y2)/(x3-x2))*x3)
    elif(x3-x2 == 0):
        flag=(((y3-y1)/(x3-x1))*x4-y4+y3-((y3-y1)/(x3-x1))*x3)*(((y1-y2)/(x1-x2))*x4-y4+y2-((y1-y2)/(x1-x2))*x2)        
    else :    
       
        flag=(((y1-y2)/(x1-x2))*x4-y4+y1-((y1-y2)/(x1-x2))*x1)*(((y3-y2)/(x3-x2))*x4-y4+y2-((y3-y2)/(x3-x2))*x2)
    if(flag>0):
        print ("OUTSIDE")
    else :
        print ("INSIDE")
insideOut(x1,x2,x3,x4,y1,y2,y3,y4)
