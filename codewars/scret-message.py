def find_secret_message(paragraph):
    res=[];paragraph=paragraph.lower().replace(".","").replace(":","").replace("?","").replace("!","").replace(",","").split(" ")
    for i in range(1,len(paragraph)):
        if paragraph[i] in paragraph[:i] and paragraph[i] not in res: res+=[paragraph[i]]
    return " ".join(res)