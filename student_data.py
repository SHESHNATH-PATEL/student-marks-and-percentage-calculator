lst=[]
lst1=[]
n=int(input("Enter the number of subject:"))
print("Enter the name of subjects:")
for i in range(0,n):
 sub=input()
 lst.append(sub)
print(lst)
print("Enter marks of subjects:")
for i in range(0,n):
 mark=int(input())
 lst1.append(mark)
m=n*100
print(lst1)
print(sum(lst1))
print(m)
percentage=(sum(lst1)/m)*100
print(percentage)