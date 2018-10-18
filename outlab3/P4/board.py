file=open("students.txt")
f=file.readlines()
dict={}
list1=[]
for i in range(1,int(f[0])+1):
	dict={f[i].split()[0]:f[i].split()[1]}
	list1.append(dict.copy())

