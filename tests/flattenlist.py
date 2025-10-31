

def flatten_list(l):
    l1 = []
    for i in l:

        if isinstance(i,list):
             l1.extend(flatten_list(i))
        else:
            l1.append(i)
    return l1




















# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8]
l = [1, [2, 3], [4, [5, 6], 7], 8]
print(flatten_list(l))
#flatten_list(l)

