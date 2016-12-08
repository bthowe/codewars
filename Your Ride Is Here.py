def ride(group,comet):
    group_count = reduce(lambda x, y: x*y, [ord(letter)-64 for letter in group])%47
    comet_count = reduce(lambda x, y: x*y, [ord(letter)-64 for letter in comet])%47
    if group_count == comet_count:
        return 'GO'
    else:
        return 'STAY'

if __name__=="__main__":
    group = "COMETQ"
    comet = "HVNGAT"
    print ride(group,comet)
