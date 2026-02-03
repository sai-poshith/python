def even_or_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
n=int(input())
result=even_or_odd(n)
print(result)
