
import re



def flesch_kincaid(text):
    #your code here
    # (0.39 * average number of words per sentence) +
    # (11.8 * average number of syllables per word) - 15.59
    sentences =[sen for sen in  re.split(r'[^a-zA-Z\s]', text) if len(sen) > 0]

    words =[word for word in  re.split(r'\W+', text) if len(word) > 0]
    words_cnt = len(words) / float(len(sentences))


    pattern = re.compile(r'([aeiou]+)')

    m = re.findall(pattern, text.lower())#, flags=re.IGNORECASE)
    syllables = len(m)


    total = 0.39 * words_cnt + 11.8 * syllables/words_cnt/len(sentences)
    return round(total - 15.59, 2)




class Test(object):
    @staticmethod
    def assert_equals(left, right):
        if left == right:
            print left, 'done'
        else:
            print 'something happend, be careful!'
            print left
        print '-' * 60

if __name__ == '__main__':

    # test = Test()


    Test.assert_equals(flesch_kincaid("The turtle is leaving."), 3.67)
    Test.assert_equals(flesch_kincaid("A good book is hard to find."),-1.06)
    #remember to use the average number of word BY SENTENCE; below: 2 sentences
    Test.assert_equals(flesch_kincaid("To be or not to be. That is the question."),-0.66)



    text = 'To be or not to be. That is the question.'

    sentences =[sen for sen in  re.split(r'[^a-zA-Z\s]', text) if len(sen) > 0]

    words =[word for word in  re.split(r'\W+', text) if len(word) > 0]
    words_cnt = len(words) / float(len(sentences))
    print sentences, words, words_cnt

    print (15.59-.66 -0.39*5)/ 11.8