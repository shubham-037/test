#Code for tower of hanoi by the help of recursion
def tower(n,s,h,d):
    if(n == 0):
       return 1
    tower(n-1,s,d,h)
    print(s , "->",  d)
    tower(n-1,h,s,d,)

tower(3,'A','B','c')
# code of factorial using recursion 
# '''def factorial(n):
#    if( n == 0 or n == 1):
#        return 1
#    return n * factorial(n-1)

# n = int(input("Enter the number"))
# print (factorial(n))'''
# # use of the lambda function
# # x = lambda a,b,c : a + b + c 
# # print(x(2,3,5))