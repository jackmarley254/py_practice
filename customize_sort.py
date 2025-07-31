#using the keyword argument key = function.
def myfunc(n):
	return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)