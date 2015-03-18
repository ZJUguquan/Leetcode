
def  shortener(message):
    # todo: shorten your message to 160:
    if len(message) <= 160:
        return message
    spaces = message.count(" ")
    words = message.split(' ')
    result = ''
    for index, element in enumerate(words):
