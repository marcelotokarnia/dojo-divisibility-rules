def div_rule(m):
    value = 1
    while(True):
        yield value
        value = value*10 % m
        if value > m/2:
            value -= m

