#jay Gajanan

#sum_0_to_n is a function which will take 'n' int where n>=1 and will return the sum of all numbers from
#1 to N
#ex if n=3 it will return 6 as 1+2+3
def sum_0_to_n(n):
    return n * (n + 1) // 2

#sum_0_to_n is a function which will take 'n' int where n>=1 and will return the sum of all numbers from
#1 squared to N squared
#ex if n=3 it will return 14 as 1+4+9(1^2+2^2+3^2)
def sum_0_to_n_squared(n):
    return n * (n + 1) * (2 * n + 1) // 6

#sum_0_to_n is a function which will take 'n' int where n>=1 and will return the sum of all numbers from
#1 cubed to N cubed
#ex if n=3 it will return 36 as 1+8+27(1^3+2^3+3^)
def sum_0_to_n_cubed(n):
    return n * (n + 1) * (n + 1) * (n + 2) // 24

#subsets function will take 'data' as parameter where data can be non-empty List or String and
# will return all the subsets of the 'data' as a List
#ex if data='abc' it will return ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']
#ex if data=[1,2,3] it will return [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
def subsets(data):
    if type(data) not in (list,str): raise TypeError("Only List and String Are Allowed")
    def all_subset_str(p,up=""):
        if p=="":
            return [up] 
        else:
            ans=[]
            ans.extend(all_subset_str(p[1:],up+p[0]))
            ans.extend(all_subset_str(p[1:],up))
            return ans
    def all_subset_arr(p,up=[]):
        if p==[]:
            return [up] 
        else:
            ans=[]
            ans.extend(all_subset_arr(p[1:],up+[p[0]]))
            ans.extend(all_subset_arr(p[1:],up))
            return ans
    return all_subset_arr(data) if type(data)==list else all_subset_str(data)

#factorial function will take 1 input 'n' as a non zero positive integer
#and will return factorial of that number
#ex if n=5 will return 120 as 5*4*3*2*1
def factorial(n):
    ans=1
    for i in range(1,n+1): ans*=i
    return ans

#fib_at_n function will take 1 input "n" as n>=0 and will return 
# fibonacci number at n'th position
# ex n=9 will return 34 
def fib_at_n(n):
    fib1,fib2=0,1
    for i in range(n-1):
        fib3=fib1+fib2
        fib1,fib2=fib2,fib3
    return fib3


    
#fib_up_to_n function will take 1 input 'n' as n>=0 will return 
# a list contaning all fibonacci number up to n
# ex n= 10 will return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
def fib_up_to_n(n):
    fib=[0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib