def race(v1, v2, g):
    if v1>=v2:
        return None
    else:
        time = float(g)/(v2 - v1)
        hrs, remainder = divmod(time * 60**2, 3600)
        mins, secs = divmod(remainder, 60)
        return [int(hrs), int(mins), int(secs)]

    # hrs = int(time)
    # mins = int(60 * (time - hrs))
    # secs = int(60 * (60 * (time - hrs) - mins))
    # return [hrs, mins, secs]

if __name__=="__main__":
    print(race(820, 850, 550))
