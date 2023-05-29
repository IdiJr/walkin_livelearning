#!/usr/bin/python3

def get_data(atuple):
    nums = ()
    words = ()
    for t in atuple:
        nums = nums + (t[0],)
        if (t[1] not in words):
            words = words + (t[1],)
        min_num = min(nums)
        max_num = max(nums)
        u_words = len(words)
        return (min_num, max_num, u_words)


    print(get_data(y))
