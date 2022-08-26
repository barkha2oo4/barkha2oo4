def minimum(kunal):
    mini = 1000
    for i in kunal:
        if i< mini :
            mini=i
ls = [1,3,23,45,76,94,48,87,35,66]
print(minimum(ls))
print(min(ls))
ls = [1,3,23,45,76,94,48,87,35,66]
sums = 0
for i in ls:
    sums+= i
print(sums)
print(sum(ls))
# for finding max using functioons
student_marks = [40,66,89,64,78,99]
max_marks = max(student_marks)
print(max_marks)
# for finding sum using functions
student_marks = [40,66,89,64,78,99]
sum_of_marks = sum(student_marks)
print( sum_of_marks )
# method 1 of writing power of 2 using built in functions
print(2**10)
print(pow(2,10))
# method 2 of writing power of 2
def power(value1,value2):
    return value1**value2
    print(power(2,10))
