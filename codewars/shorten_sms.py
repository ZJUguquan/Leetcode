
def  shortener(message):
    # todo: shorten your message to 160:
    if len(message) <= 160:
        return message
    spaces = message.count(" ")
    needs_trunc = len(message) - 160
    words = message.split(' ')
    result = []
    for i in range(1,needs_trunc +1):
        result.append(words[-i].title())
    output = ' '.join(words[:-needs_trunc])  + ''.join(result[::-1])
    return output
    # print( len(output), output)

message = """No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! And that will be it."""
# No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!AndThatWillBeIt.
print(shortener(message))

result = 'No one expects the Spanish Inquisition! Our chief weapon is surprise, fear and surprise; two chief weapons, fear,NoIt.BeWillThatAndEfficiency!RuthlessAnd'
print(len(result))
