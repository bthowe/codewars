def is_triangle(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

if __name__=="__main__":
    print is_triangle(1,2,3)
