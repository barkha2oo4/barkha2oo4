# list
'''ls= ["sneha", "vineeta", "riya", ......."janat"]

ls = ["name",True ,66.7,23]
print(ls)
print(type(ls))'''
# representation of list
'''ls = ["devraj" ,"shanaya" , "rehana","kahanvi", "suneha", "sheetal","reema"]
        0          1            2       3          4         5
        -6         -5          -4      -3         -2        -1
        '''
# showing the element according to their order
'''ls = ["devraj" ,"shanaya" , "rehana","kahanvi", "suneha", "sheetal","reema"]
print(ls[2])'''

ls =[False,"devraj" ,"shanaya" , "rehana", 88 , "kahanvi", "suneha",True ,"sheetal",77,"reema",45,"shiksha"]
# showing the element according to their order
'''print(ls[2])
print(ls[-2])
print(ls[-6])
print(ls[4], ls[6])
print(ls[4])
print(ls[1], ls[10])
print(ls)
ls[3] = "kunal"
print(ls)'''
# replacing an element with other
ls =[False,"devraj" ,"shanaya" , "rehana", 88 , "kahanvi", "suneha",True ,"sheetal",77,"reema",45,"shiksha"]
ls[-6] = "Thor"
print(ls)

# pushing an element into the list
ls.append(999)
print(ls)
# inserting an element to the list
ls.insert(2,"Cheetah")
print(ls)
# deleting an element from list
del(ls[2])
print(ls)
# slicing the list
print(ls[3:8])
print(ls[3:])
print(ls[:9])
print(ls[:])
# for finding length of list
ls = [1,3,23,45,76,94,48,87,35,66]
for i in range(len(ls)):
        print(ls[i])
        print(i)
# max value
maximum = -1
for i in ls:
        if maximum<i:
           maximum = i
print(maximum)
print(max(ls))
# repetition of the list i times
for i in ls:
        print(ls)

# case of error
for i in ls:
        if i< ls:                             #i is an integer which is non negative while ls can be -ve
                 print(i)
