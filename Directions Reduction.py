import re

def dirReduc(arr):
    regex = r'NORTH\s+SOUTH|SOUTH\s+NORTH|WEST\s+EAST|EAST\s+WEST'
    directions = ' '.join(arr)
    go = 0
    while go==0:
        if re.findall(regex, directions):
            directions = re.sub(regex, '', directions)
        else:
            go=1
    return directions.split()

if __name__=="__main__":
    a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    print dirReduc(a)
