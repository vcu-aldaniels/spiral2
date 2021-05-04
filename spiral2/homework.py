def spiralize(size, n=1):
    """ Your code goes somewhere in here"""
    size = 101  # this the sum of numbers size from diagonal
    n = 25  # this is what the number is in place of 1 essentially its 25 counting backwards to one instead of from 1

    for x in range(25, n - 1): #this is here so that every is counting down from 25 instead of counting up from 1.
        if n == 25:
            return n

    return_value = n
    return return_value


if __name__ == "__main__":
    find_sum = spiralize(501)

    return find_sum
