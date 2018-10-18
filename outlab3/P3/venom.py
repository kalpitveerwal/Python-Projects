file = open("snakes.txt") 
f=file.readlines()
for j in range(int(f[0])+3,int(f[int(f[0])+1])+int(f[0])+3):
    for i in range(2,int(f[0])+2):
        if(f[j-1].split()[0]=="V"):
            if(f[j-1].split()[1]==f[i-1].split()[2]):
                print(f[i-1].split()[0])
        if(f[j-1].split()[0]=="L"):
            if(f[j-1].split()[1]==f[i-1].split()[1]):
                print(f[i-1].split()[0])