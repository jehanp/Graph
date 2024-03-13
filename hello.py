
print("hello world")

for i in range(4):
    print(i)


matrix = {(0,3):1, (2,1):2, (4,3):3}
print(matrix)


def linear_search(xs, target):
    """Find and return the index of target in sequence xs"""
    for(i,v) in enumerate(xs):
        if(v==target):
            return i
    return -1

friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]

found=linear_search(friends, "Zoe")==1
print(found)