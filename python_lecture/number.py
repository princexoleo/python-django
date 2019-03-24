a = 5
print(a+a)
a= a*5
print(a) #comments
#Lists::
mylist=[2,1,3,5,4]
print("Before sorting...")
print(mylist)
print("After sorting...")
mylist.sort()
print(mylist)
print("Nested :ists")
mylist=[1,2,['x','y','z']]
print(mylist[2][2])
martrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]
first_col = [row[0] for row in martrix]
print("First Column: ")
print(first_col)
