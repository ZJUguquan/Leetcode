def my_parse_int(string):
    #your code here, return the string "NaN" when the input is not an integer value
    if '.' in string:
        return 'NaN'
    try:
        return int(string)
    except:
        return 'NaN'