import numpy

def arrays(arr):
    arr.sort(reverse=True)
    np = numpy.array(list(map(float, arr)))
    return np

arr = input().strip().split(' ')
result = arrays(arr)
print(result)