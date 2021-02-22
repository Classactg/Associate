def func_compute(n):
 return lambda x : x * n
result = func_compute(7)
print (result(32))