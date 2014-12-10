def get_function(sequence):
  first, dist = sequence[0], sequence[1] - sequence[0]
  valid = all(x == dist * i + first for i, x in enumerate(sequence))
  dist = 'x' if dist == 1 else '-x' if dist == -1 else '' if dist == 0 else str(dist) + 'x'
  first = str(first) if len(dist) == 0 else '' if first == 0 else ' - ' + str(first * -1) if first < 0 else ' + ' + str(first)
  return 'f(x) = ' + dist + first if valid else 'Non-linear sequence'



'my solution'

def get_function(sequence):
    if min(sequence) == max(sequence):
        return "f(x) = {}".format(sequence[0])
    # Non-linear sequence
    allk = []
    for i in range(1, len(sequence) - 1):
        this_k = (sequence[i] - sequence[0])/i
        allk.append(this_k)
    if min(allk) < max(allk) :
        return "Non-linear sequence"
    if sequence[0] == 0:
        return "f(x) = {}x".format(sequence[1]) if sequence[1] != 1 else "f(x) = x"
    else:
        if sequence[0] > 0:
            return "f(x) = {}x + {}".format(sequence[1]-sequence[0], sequence[0]) if sequence[1]-sequence[0] != 1 else "f(x) = x + {}".format(sequence[0])
        else:
            return "f(x) = {}x - {}".format(sequence[1]-sequence[0], -sequence[0]) if sequence[1]-sequence[0] != 1 else "f(x) = x - {}".format(-sequence[0])