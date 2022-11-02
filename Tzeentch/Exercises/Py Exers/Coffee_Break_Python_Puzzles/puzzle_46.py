#############################
## id 399
## Puzzle Elo 1749
## Correctly solved 40 %
#############################

# popular instagram accounts
# (millions followers)
inst = {"@instagram":232,
        "@selenagomez":133,
        "@victoriassecret":59,
        "@cristiano":120,
        "@beyonce":111,
        "@nike":76}

# popular twitter accounts
# (millions followers)
twit = {"@cristiano":69,
        "@barackobama":100,
        "@ladygaga":77,
        "@selenagomez":56,
        "@realdonaldtrump":48}


inst_names = set(filter(lambda key: inst[key]>60, inst.keys()))
twit_names = set(filter(lambda key: twit[key]>60, twit.keys()))

superstars = inst_names.intersection(twit_names)
print(list(superstars)[0])
