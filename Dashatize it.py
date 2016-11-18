import re
def dashatize(num):
    dash = re.sub(r'([13579])', r'-\1-', str(num))
    dash = re.sub(r'--', r'-', dash)
    return dash.strip('-')


if __name__=="__main__":
    print dashatize(-28369)
