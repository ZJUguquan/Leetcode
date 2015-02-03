import textwrap

def justify(text, width):
    def justify_line(line):
        if '' not in line:
            return line
        places = line.count(' ')
        spaces = width - len(line) + places
        interval, extra = divmod(spaces, places)
        return ''.join(word + ' ' * (interval + (i<extra)) for i, word in enumerate(line.split())).strip()

    lines = textwrap.wrap(text, width, break_on_hyphens=False)
    return '\n'.join(map(justify_line, lines[:-1]) + [lines[-1]])


text = '''
Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
'''

width = 20
import re
text_array = re.split('[\n\s]+', text)


def full_justify(words, width):
    ''' fullly put words into one line length : width
    '''
    count_words = len(words)
    if len(' '.join(words)) == width or count_words == 1:
        return ' '.join(words).ljust(width)
    m, n = divmod(width - len(''.join(words)), count_words - 1)
    return ((' ' * (m + 1)).join(words[:n + 1]) + ' ' * m + (' ' * (m)).join(words[n + 1:])).strip()


def justify(text, width):
    import re
    if len(text) <= width:
        return ' '.join(text.split())
    result = []
    text = [w for w in re.split('\s+', text) if len(w) > 0]
    # print(text)
    buffer = text.pop(0)
    while len(buffer) <= width and len(text) > 0:
        if len(text[0]) + 1 + len(buffer) <= width:
            buffer += ' ' + text.pop(0)
        else:
            # print(buffer)
            buffer = buffer.strip()
            buffer_words = buffer.split()
            if len(buffer) == width:
                result.append(buffer)
            else:
                a = full_justify(buffer_words, width)
                # print(a)
                result.append(a)
            buffer = text.pop(0)
        if len(text) == 0:
            buffer = buffer.strip()
            result.append(' '.join(buffer.split()))

    return '\n'.join(result)


# from pprint import pprint
print('*' * 30)

print(justify(text, width))
