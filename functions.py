def length(corona):
    count = 0
    for i in corona:
        count += 1
    return(count)


ls = [1,3,23,45,76,94,48,87,35,66]
for i in range(length(ls)):
      print(ls(i))
ls1 =[1,3,4,9,7,87,56,90,876,34,79]
print(length(ls1))

# lets perform nCr
# formula n!/((r!)*(n-r)!)
# method 1
n =5
r = 2
n_fact = 1
for i in range(1,n+1):
    n_fact = n_fact*i
r_fact = 1
for i in range(1,n+1):
    r_fact =r_fact*i
n_minus_r = 1
for i in range(1,n+1):
    n_minus_r = n_minus_r*i
ans = n_fact/(r_fact*n_minus_r)
print(ans)

# method 2
def fact(num):
    ans = 1
    for i in range(1,num+1):
        ans =ans*i
    return ans

n = 5
r = 2
n_fact = fact(n)
r_fact = fact(r)
n_minus_r = fact(n-r)
ans = n_fact/(r_fact*n_minus_r)
print(ans)
