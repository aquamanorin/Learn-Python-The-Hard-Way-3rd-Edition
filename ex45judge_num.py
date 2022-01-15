def num_or_not(num):

    for i in num:
        if int(i,35) < 10:
            continue
        else:
            return False
    return True

def three_digit_or_not(num):

    if int(num) < 0 or int(num) > 999:
        return False
    else:
        return True

def judge_num(num):

    if num_or_not(num) is False or three_digit_or_not(num) is False:
        return False
    else:
        return True



