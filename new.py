#in a list[] the commands that can performed
        
if __name__ == '__main__':
   N = int(input())

k =[]
for i in range(0,N):
    p = input().split()
    if (p[0] =='insert'):
        k.insert(int(p[1]),int(p[2]))
    elif (p[0] =='print'):
        print(k)
    elif(p[0] =='remove'):
        k.remove(p[1])
    elif(p[0] =='append'):
        k.append(p[1])
    elif(p[0] =='sort'):
        k.sort()
    elif(p[0] =='pop'):
        k.pop()
    else:
        k.reverse()

#in a list[] the commands that can performed
        
L=[]
for i in range(0,N):
        cmd=input().split()
        if cmd[0] == "insert":
            L.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "pop":
            L.pop()
        elif cmd[0] == "print":
            print(L)
        elif cmd[0] == "remove":
            L.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            L.sort()
        else:
             L.reverse()


            #  to define the list and location of elements in list
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 56, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])







