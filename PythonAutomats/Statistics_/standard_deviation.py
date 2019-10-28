import math
def std(arr):
    avg = sum(arr) / len(arr)
    return math.sqrt(sum([(x-avg)**2 for x in arr])/len(arr))