print("Enter The Number Of Rows!")
r = int(input())
print("Enter 0 To Print The Pattern In Ascending Order And 1 To Print The Pattern In Descending Order!")
b = int(input())
if b == 0 :
	for r in range(0,r+1):
	    print(r*"*")
else: 
	for r in reversed(range(0+r+1)):
		print(r*"*")