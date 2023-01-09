# position track
names=['raj','ram','har','dar']
# pos=0
# for i in names:
#     print(f"{pos}--->{i}")
#     pos+=1
# output
# 0--->raj
# 1--->ram
# 2--->har
# 3--->dar

# by enumerate function
# for pos,name in enumerate(names):
#     print(f"{pos}---->{name}")
    
    
# finding pos of string
def find_pos(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return -1
        
# print(find_pos(names,'raj')) #0
# print(find_pos(names,'rohi')) #-1
# print(find_pos(names,'har')) #2
