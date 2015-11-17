def get_average(marks):
    try:
        if len(marks) < 1:
            return
        else:
            return round(sum(marks) / len(marks))
    except Exception as e:
        print(e)
        raise NotImplementedError("TODO: get_average")
