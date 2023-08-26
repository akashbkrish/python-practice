'''
arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]

for i in range(0, 4):
       print(arr[i].pop(), end=" ")



arr_1 = [1,2,3,45]
print(arr_1.pop()
      )


list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
list2 = list1
list3 = list1[:]

print(list1, list2, list3)



list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
list2 = list1
list3 = list1[:]

list2[0] = 'Guava'
list3[1] = 'Kiwi'

total = 0
for ls in (list1, list2, list3):
  if ls[0] == 'Guava':
    total += 1

  if ls[1] == 'Kiwi':
    total += 20

print (total, list3[0])
a= [1,2,3,4,5]
b=a
c=a[:]
b[1] = [-1]


print("a", a)
print("b", b)
print("c", c)

‘Hello’


list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
list2 = list1
list3 = list1[:]

list2[0] = 'Guava'
list3[1] = 'Kiwi'

total = 0
for ls in (list1, list2, list3):
  if ls[0] == 'Guava':
    total += 1

  if ls[1] == 'Kiwi':
    total += 20

print (total, list3[0])


arr = [a+" "+b for a in [ "Hello", "Good"] for b in ["Dear", "Bye"]]
print(arr) 


tup1 = (1,2,3)
tup1 = tup1 + (4,)
print(tup1)

dict1 = {1:"Akash",2:"Balakrishnan"}
for k in dict1:
    print("key : ",k, ", ","Value : ",dict1[k])

def bar(x,y):
       if y==0:
             return 0
       return (x+bar(x,y-1))

def foo(x,y):
    if y==0:
        return 1
    return bar(x,foo(x,y-1))
print(foo(3,5))


lis = [(0, 2), (1, 3), (2, 4)]
result = sum (n for _,n in lis)
print(result)

dict = {1:"Apple" , 2: "Orange", 3: "Banana"}
dict[1] = "S"
print(dict)




def filter_odd(numbers):

   for number in range(numbers):

       if(number%2!=0):

           yield number 

odd_numbers = filter_odd(20)

print(list(odd_numbers))

'''

def solve(A):
    lst = A.split()
    str = ""
    print(len(lst))
    l =[]
    for i in range(len(lst)-1,-1,-1):
        str = str + lst[i]+" "
        l.append(lst[i])
    print(str.strip())
    print(l)
    print(" ".join(l))
A = "The sky is blue"
solve(A)



def solve2(A):
    print("inside solve2"+"\n")
    lst = []
    lst = A.split()[::-1]
    print(" ".join(lst))
  




B = "The sky is blue"
solve2(B)

class Solution:
  def solve3(self,A):
      print("\n", "Inside function 3","\n")
      A = A.strip().split()[::-1]  # here the execution is starts at right to left it's same as below
      '''
        A = A.strip()
        A = A.split()
        A = A[::-1]
      '''
      return ' '.join(A)
    
A = "The sky is blue"
p = Solution()
print(p.solve3(A))