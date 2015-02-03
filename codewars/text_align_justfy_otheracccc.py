import textwrap


def justify(text, width):
    def justify_line(line):
        if '' not in line:
            return line
        places = line.count(' ')
        spaces = width - len(line) + places
        interval, extra = divmod(spaces, places)
        return ''.join(word + ' ' * (interval + (i < extra)) for i, word in enumerate(line.split())).strip()

    lines = textwrap.wrap(text, width, break_on_hyphens=False)
    return '\n'.join(list(map(justify_line, lines[:-1])) + [lines[-1]])


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

print(justify(text, 30))


def justify(text, width):
    lines, last = [[]], -1
    for word in text.split():
        if last + 1 + len(word) > width:
            lines.append([word])
            last = len(word)
        else:
            lines[-1].append(word)
            last += len(word) + 1

    def justify_line(words):
        if len(words) == 1:
            return words[0]
        interval, extra = divmod(width - sum(map(len, words)), len(words) - 1)
        init = (word + ' ' * (interval + (i < extra))
                for i, word in enumerate(words[:-1]))
        return ''.join(init) + words[-1]
    return '\n'.join(map(justify_line, lines[:-1]) + [' '.join(lines[-1])])
