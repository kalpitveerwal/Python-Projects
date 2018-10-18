import pickle
import random
import string
# take input of the data
def fill_choice():
    data = []
    for i in range (101):
        raw = random.randint(1,5001)
        chars=string.ascii_uppercase
        j = ''.join(random.choice(chars) for x in range(len(str(raw))))
        ans=str(raw)+' '+j
        data.append(ans)

    file = open('new_int.p', 'wb')
    pickle.dump(data, file)
    file.close()
fill_choice()
#2nd part
def ask_choice():
    t=int(input("Enter Number: "))
    file = open('new_int.p','rb')
    data = pickle.load(file)
    file.close()
    flag=1
    for item1 in data:
        for item2 in data:
        	if int(item1.split(' ')[0])<int(item2.split(' ')[0]) :
        	    if int(item1.split(' ')[0])+int(item2.split(' ')[0])==t :
        		    print(item1.split(' ')[1],item1.split(' ')[0],item2.split(' ')[1],item2.split(' ')[0])
        		    flag=0
    if flag == 1 :
        for item1 in data:
            for item2 in data:
        	    if int(item1.split(' ')[0])<int(item2.split(' ')[0]) :
        	        if int(item1.split(' ')[0])+int(item2.split(' ')[0]) < t :
        	            print(item1.split(' ')[1],item1.split(' ')[0],item2.split(' ')[1],item2.split(' ')[0])

ask_choice()        