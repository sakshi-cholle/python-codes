#use of for loops

#for-else
for x in "coco":
    print(x)
else:
    print("null")
print("end")

#for-dictionary
mydict={'coco':'1', 'moco':'2', 'poco':'3'}
for keys in mydict:
    print("the keys are:", keys)

#for-list/tuple
fruits=('apple', 'banana', 'orange', 'mango')
for x in fruits:
    print(x)


#for-string
name='coco'
for x in name:
    print(x)

#for-break
for x in range(1,10):
    if x==4:
        print("break applied")
        break
    print(x)

#for-continue
for x in range(1,10):
    if x==4:
        continue
    print(x)

