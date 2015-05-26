# 筛法


def shaifa(n):
    output = []
    numbers = range(2, n)
    if numbers is not None:
        start = numbers.pop(0)
        output.append(start)

        while numbers[-1] ** 2 > start:
            print numbers
            for i in range(start**2, n-1, start):
                if i in numbers:
                    numbers.remove(i)
            start = output.pop(0)
            output.append(start)

    return output

print shaifa(25)