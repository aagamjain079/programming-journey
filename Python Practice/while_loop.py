# i=5
# while i >=1:
#     print(i)
#     i-=1

def factorial(num):
    if num == 0:
        fact=1
        print(fact)
    elif num > 0:
        fact=0
        while num>1:
            fact = num*num-1
            num = num-1
        print(fact)

factorial(5)