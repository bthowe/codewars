import numpy as np
def spiralize(size):
    a = np.full([size, size],np.nan)

    move = True
    position = [0,0]
    direction = 'right'

    quit_loc = size/2

    while move:
        a[position[0], position[1]] = 1
        if direction=='right':
            if ((position[1]<=size-3) and (a[position[0], position[1]+2]==1)) or \
                ((position[1]>size-3) and (position[1]+1==size)):
                if a[position[0]+2, position[1]]!=1:
                    direction='down'
                    position = [position[0]+1, position[1]]
                else:
                    move=False
            else:
                position = [position[0], position[1]+1]

        elif direction=='left':
            if ((position[1]>=2) and (a[position[0], position[1]-2]==1)) or \
                ((position[1]<2) and (position[1]-1==-1)):
                if a[position[0]-2, position[1]]!=1:
                    direction='up'
                    position = [position[0]-1, position[1]]
                else:
                    move=False
            else:
                position = [position[0], position[1]-1]

        elif direction=='up':
            if ((position[0]>=2) and (a[position[0]-2, position[1]]==1)) or \
                ((position[0]<2) and (position[0]-1==-1)):
                if (a[position[0], position[1]+2]!=1) and (a[position[0]+1, position[1]+1]!=1):
                    direction='right'
                    position = [position[0], position[1]+1]
                else:
                    move=False
            else:
                position = [position[0]-1, position[1]]

        else:
            if ((position[0]<=size-3) and (a[position[0]+2, position[1]]==1)) or \
                ((position[0]>size-3) and (position[0]+1==size)):
                if (a[position[0], position[1]-2]!=1) and (a[position[0]-1, position[1]-1]!=1):
                    direction='left'
                    position = [position[0], position[1]-1]
                else:
                    move=False
            else:
                position = [position[0]+1, position[1]]

    a = np.where(a==1, 1, 0)
    return a.tolist()





if __name__=="__main__":
    size = 2
    print spiralize(size)
