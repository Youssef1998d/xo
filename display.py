def init():
    return ["-" for v in range(9)]
def display(l):
    for i in range(0,9,3):
        print(l[i],"|",l[i+1],"|",l[i+2])
    return True
