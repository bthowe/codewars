def split_without_loss(s, split_p):
    a = split_p.split('|')
    string = []
    for ind, piece in enumerate(s.split(split_p.replace('|', ''))):
        if ind==0:
            string.append(piece + a[0])
        elif ind==len(s.split(split_p.replace('|', '')))-1:
            string.append(a[1] + piece)
        else:
            string.append(a[1] + piece + a[0])
    return [piece for piece in string if piece!='']


if __name__=="__main__":
    split_without_loss("hello world!", " |") #=> ["hello ", "world!"]
    split_without_loss("hello world!", "o|rl") #=> ["hello wo", "rld!"]
    split_without_loss("hello world!", "h|ello world!") #=> ["h", "ello world!"]
    split_without_loss("hello world! hello world!", " |")
                      #=> ["hello ", "world! ", "hello ", "world!"]
    split_without_loss("hello world! hello world!", "o|rl")
                      #=> ["hello wo", "rld! hello wo", "rld!"]
    split_without_loss("hello  hello  hello", " | ")
                      #=> ["hello ", " hello ", " hello"]
    split_without_loss(" hello world", " |")
                      #=> [" ", "hello ", "world"]
    split_without_loss("  hello hello hello", " |")
                      #=> [" ", " ", "hello ", "hello ", "hello"]
    split_without_loss("  hello hello hello  ", " |")
                      #=> [" ", " ", "hello ", "hello ", "hello ", " "]
    split_without_loss("  hello hello hello", "| ")
                      #=> [" ", " hello", " hello", " hello"]
