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
