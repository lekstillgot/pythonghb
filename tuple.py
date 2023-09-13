import sys
import platform
import time
a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd']

t = tuple(zip(a, b))
print(t)
print(type(t))
print(t[0])
print(t[0][1])

a_list = []
a_tuple = ()
a_list = ["test", "for", "memory"]
a_tuple = ("test", "for", "memory")

print(sys.getsizeof(a_list), "bytes")
print(sys.getsizeof(a_tuple), "bytes")

v_list = list(range(10000001))
v_tuple = list(range(10000001))

# list test performance
start = time.time_ns()
for i in range(len(v_list)):
    a = v_list[i]
end = time.time_ns()
print("Total time for list:", end - start)

start = time.time_ns()
for i in range(len(v_tuple)):
    a = v_tuple[i]
end = time.time_ns()
print("Total time for list:", end - start)
