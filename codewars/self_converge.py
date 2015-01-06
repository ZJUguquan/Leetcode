def cal_reminder(number):
        descending_number = int(''.join(sorted(str(number), reverse=True)))
        ascending_number = int(''.join(sorted(str(number), reverse=False)))
        reminder = descending_number - ascending_number
        return reminder


def self_converge(number):
    counter = 0
    sub_result = []
    while cal_reminder(number) > 0:
        if cal_reminder(number) in sub_result:
            return counter
        sub_result.append(cal_reminder(number))
        counter += 1
        number = cal_reminder(number)
    return -1


print(
self_converge(123)
)