import nltk

nltk.download('averaged_perceptron_tagger')

def check_for_freebies(description):

    description_lst = description.split()
    punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for i in range(0, len(description_lst)):
        tmp = description_lst[i]
        tmp = tmp.lower()
        for letter in tmp:
            if letter in punct:
                tmp = tmp.replace(letter, "")
        if (tmp == 'free'):
            if (i < (len(description_lst) - 1)):
                # clean next word
                next_word = description_lst[i+1]
                next_word = next_word.lower()
                for letter in next_word:
                    if letter in punct:
                        next_word = next_word.replace(letter, "")
                tuple_tag = nltk.pos_tag(next_word)
                tag = tuple_tag[0][1]
                if(tag == 'NN' or tag == 'NNS' or tag == 'NNPS' or tag == 'NNP'):
                    return True

    return False