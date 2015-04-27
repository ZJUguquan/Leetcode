def solution(string,markers):
    lines = string.split('\n')
    res = []
    for line in lines:
        for marker in markers:
            while marker in line:
                line = line.split(marker)[0]
        res.append(line.strip())

    return '\n'.join(res)

print(
solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
)