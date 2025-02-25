set={1,2,3,4,5}
print(set)
e=int(input("enter an element"))
if e in set:
    remove =set.remove(e)
    print("remove element succesfully")
else:
        raise keyerror("set is empty")
print("arbitrary set is ",set)
print(set)
