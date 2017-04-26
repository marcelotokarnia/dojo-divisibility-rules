from divisibility_rule import div_rule


def is_divisible(n,m):
    divisibility_rule = div_rule(m)
    sum = 0
    n = n[::-1]
    for i in n:
        param = divisibility_rule.__next__()
        sum += int(i) * param
        print(sum)
        if abs(sum) > 3*m:
            if sum > 0:
                sum -= 3*m
            else:
                sum += 3*m
    return sum % m == 0
