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
                if (description_lst[i+1].lower() != 'to'):
                    return True

    return False