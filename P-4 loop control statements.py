#loop control statements

#break statement
count=0
while count<=10:
    if count==6:
        print("the break is applied")
        break
    print("the count is", count)
    count+=1


#continue statement
count=0
while count<=10:
    count+=1
    if count==4:
        print("the 4 is skipped")
        continue
    print(" the count is", count)
