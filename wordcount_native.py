import timeit
start = timeit.default_timer()
f = open('/home/andrew/Downloads/1987.txt')
total = 0
for line in f:
    if "SJC" in line:
        total += 1
f.close()
print total
stop = timeit.default_timer()
print stop - start 

#Benefit only with big data files (trillion lines)
