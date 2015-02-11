from re import compile

TOKENIZER = compile('(0+)')

class Cluster(object):
    def __init__(self, center, weight, mn, mx):
        self.center = center
        self.weight = weight
        self.mn = mn
        self.mx = mx

def decodeBitsAdvanced(bits):
    bits = bits.strip('0')
    if not bits:
        return ''
    tokens = TOKENIZER.split(bits.strip('0'))
    lengths = sorted(len(token) for token in tokens)
    (minLen, maxLen) = (lengths[0], lengths[-1])
    lenRange = float(maxLen - minLen)
    # Employ 3-means clustering
    clusters = tuple(Cluster(minLen + lenRange * x / 8, 0, maxLen, minLen) for x in (1, 3, 7))
    for sample in lengths:
        # Find the closest cluster for this sample
        cluster = min(clusters, key = lambda cluster: abs(sample - cluster.center))
        # Adjust cluster: each sample has weight of 1, cluster center is adjusted, its weight increases
        cluster.center = (cluster.center * cluster.weight + sample) / (cluster.weight + 1)
        cluster.weight += 1
        if sample < cluster.mn:
            cluster.mn = sample
        if sample > cluster.mx:
            cluster.mx = sample
    # Fill the gaps if we really have less than 3 clusters
    clusters = [cluster for cluster in clusters if cluster.weight] # Filter out empty clusters
    if len(clusters) == 2:
        if float(clusters[1].mn) / clusters[0].mx >= 5: # If 1 and 7 are present while 3 is not, add a syntetic cluster for 3
            clusters.insert(1, Cluster((clusters[0].mx + clusters[1].mn) / 2.0, 0, clusters[0].mx + 1, clusters[1].mn - 1))
    if len(clusters) < 3: # If only 1 is present (or only 1 and 3 are), add syntetic clusters for 3 and 7 (or just 7)
        limit = clusters[-1].mx + 1
        clusters.extend(Cluster(limit, 0, limit, limit) for i in xrange(3 - len(clusters)))
    # Calculating edges between dots and dashes, and dashes and word pauses
    maxDot = (clusters[0].mx + clusters[1].mn) / 2.0
    maxDash = (clusters[1].mx + clusters[2].mn) / 2.0
    # Perform transcoding
    ret = []
    for token in tokens:
        if token[0] == '1':
            ret.append('.' if len(token) <= maxDot else '-')
        elif len(token) > maxDot:
            ret.append(' ' if len(token) <= maxDash else '   ')
    return ''.join(ret)

def decodeMorse(morseCode):
    morseCode = morseCode.strip()
    if not morseCode:
        return ''
    return ' '.join(''.join(MORSE_CODE[c] for c in word.split(' ')) for word in morseCode.split('   '))