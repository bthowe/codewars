def duck_duck_goose(players, goose):
    l = len(players)
    return players[(goose - 1)%l]



if __name__=="__main__":
    print duck_duck_goose(['a', 'b', 'c', 'd'], 5)
