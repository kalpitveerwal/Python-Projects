with open("employees.txt") as f:
    content = f.readlines()

for x in content:
       y= x.split()
       z=y[0]
       first= z[3:]
       second=z[0:3]
       z=first+second
       print(z)  

      
