def is_merge(s, part1, part2):
    part1_lst = [letter for letter in part1]
    part2_lst = [letter for letter in part2]

    for letter in s:
        if part1_lst[0]==part2_lst[0]:


        else:
            if part1_lst and (letter==part1_lst[0]):
                part1_lst.pop(0)
                print part1_lst
            elif part2_lst and (letter==part2_lst[0]):
                part2_lst.pop(0)
                print part2_lst
            else:
                return False
    return True





if __name__=="__main__":
    print is_merge('codewars', 'cod', 'wars')
