def checkout(string):
    d = {'A': 50, 'B': 30, 'C': 20, 'D': 15}

    try:
        if (all(x.isupper() for x in string)):
            num_a, num_b  = string.count('A'), string.count('B')
            n = num_a/3
            m = num_b/2
            if n.is_integer() and n > 0 :
                n = n
                string = [x for x in list(string) if x != ('A')]
            else:
                n = 0
            if m.is_integer() and m > 0:
                m = m
                string = [x for x in list(string) if x != ('B')]
            else:
                m = 0

            total = (n * 120) + (m * 50) + sum([d[x] for x in list(string)])

        else:
            total = -1

    except:
        total = -1

    return total
