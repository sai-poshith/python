# example showing to print even numbers in a list
numbers = [10,11,12,13,14,15,16]
for n in numbers:
  if n%2==0:
    print(n)
# count positive numbers in a list
num = [-2,5,4,-8,-9]
count=0
for n in num:
  if n>=0:
    count+=1
print(count)
# take input into a list and print sum
list=[]
s=int(input())
for i in range(s):
    n=int(input())
    list.append(n)
print(sum(list))
#Find maximum manually (NO max())
numbers=[10,55,41,12,0,78]
max=numbers[0]
for n in numbers:
    if max<n:
        max=n
print(max)
#Pass / Fail program
marks=[]
for i in range(5):
    n=int(input())
    marks.append(n)
for m in marks:
    if m>=50:
        print("pass")
    else:
        print("Fail")
