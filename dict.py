d = {"name":"Jackson","followers":66666, "online":True,34:"id"}
'''
keys:- name,followers,online,34
values:-Jackson,66666,True,id
'''
for i in d.keys():
    print(d[i])
    print(d)
    print(type(d))
print(type(d.keys()))
print(d.keys())
print(d.values())
print(d["online"])
print(d[34])
e= {"name":"Jackson","followers":66666, "online":True,"name":"id"}
print(e.values())
print(e.keys())
f = {"name":["Jackson","messi"],"followers":66666, "online":True}
print(f.values())
# h = {"name":"Jackson","followers":66666, "online":True,34:["age":24]}
# print(h.values())

# to add the keys and values in dictionary
d["sports"] = "Football"
print(d)
d.update({"hobby":"painting"})
print(d)
# to delete items in dictionary
del d["name"][0]
print(d)
# to clear whole dictionary
d.clear()
print(d)

