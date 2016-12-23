def bouncingBall(h, bounce, window):
    if h>0 and 0<bounce<1 and h>window:
        views = 0
        ball_height = h*bounce
        while ball_height>window:
            ball_height*=bounce
            views+=2
        return views+1
    else:
        return -1


if __name__=="__main__":
    print bouncingBall(10, 0.6, 10)
