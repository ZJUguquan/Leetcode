def translate(word):
    dictor = {'to': '2', 'too': '2',
        'for':'4', 'four':'4', 'fore':'4',
        'oo':'00', 'be':'b','are':'r', 'you':'u',
         'please':'plz', 'people':'ppl',
        'really':'rly', 'have':'haz', 'know':'no'}
    flag = 0
    for k in dictor:
        if k in word:
            word = word.replace(k, dictor[k])
            flag = -1

def n00bify(text):
    '''
    to, too -> 2    today => 2day
    for, four, fore -> 4
    double o -> relace with 0
    be, are , you, -> b, r, u
    please - > plz
    people -> ppl
    really -> rly
    have haz
    know -> no   (part of word also replace)
    s -> z   maintaining case
    LOL (if beginning with a 'w')
    OMG (after LOL, if len = 32)
    evenly numbered words -> CAPS
    ALL CAPS output (if input start with 'h')
    , . remove
    ?  multiple base words. ---->  word count.
    !  -->  !1!1
    '''

    #Your code here
    return lambda x: translate(x)





#############################################################################
import re

dict = {"[\.,']": "", "too?": "2", "fore?": "4", "oo": "00", "be": "b",
        "are": "r", "you": "u", "please": "plz", "people": "ppl",
        "really": "rly", "have": "haz", "know": "no", "s": "z"}

def n00bify(text):
    for word in dict:
        text = re.sub(word, dict[word], text, flags=re.IGNORECASE)

    if text[0] in "hH":
        text = text.upper()

    if text[0] in "wW":
        text = "LOL " + text

    if len(re.sub("[\?!]*", "", text)) >= 32:
        text = re.sub("\A(LOL |)", "\g<1>OMG ", text)

    text = " ".join(w.upper() if i % 2 != 0 else w for i, w in enumerate(text.split()))

    text = re.sub("(\?|!)", "\g<1>" * len(text.split()), text).replace("!!", "!1")

    return text
