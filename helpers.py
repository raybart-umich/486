import nltk
from bs4 import BeautifulSoup
import requests

nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

def check_for_freebies(description):
    """
    Scans provided event description for 
    keywords and parts of speech.
    """

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
                tuple_tag = nltk.pos_tag(nltk.word_tokenize(next_word))
                tag = tuple_tag[0][1]
                if(tag == 'NN' or tag == 'NNS' or tag == 'NNPS' or tag == 'NNP'):
                    return True

    return False

def get_soup(url):
    """
    Establishes connection to event url and
    returns BeautifulSoup object.
    """
    s = requests.Session()
    s.headers.update({'User-Agent': 'Mozilla/5.0'})
    req = s.get(url=url)
    page = req.text
    return BeautifulSoup(page, 'html.parser')

def calc_precision_and_recall():
    """
    For project summary use only. 
    Computes dataset precision and recall.
    """
    retrieved = open("retrieved.txt", "r")
    full_data = open("full_data_set.txt", "r")
    list_of_retrieved = retrieved.readlines()
    count = 0
    relevant = 0
    not_relevant = 0
    for line in list_of_retrieved:
        count += 1
        if(line[0] == "*"):
            relevant += 1
        if(line[0] == "#"):
            not_relevant += 1

    list_of_full_data = full_data.readlines()
    total_relevant = 0
    rel_not_retrieved = 0
    not_and_irrel = 0
    for line in list_of_full_data:
        if (line[0] == "!" or line[0] == "*"):
            total_relevant += 1
            if (line[0] == "!"):
                rel_not_retrieved += 1
        if (line[0] == "-"):
            not_and_irrel += 1


    
    precision = relevant/count
    recall = relevant/total_relevant
    print("Precision = " + str(precision))
    print("Recall = " + str(recall))
    print("Retrieved & Relevant = " + str(relevant))
    print("Retrieved & Not Relevant = " + str(not_relevant))
    print("Not Retrieved & Relevant = " + str(rel_not_retrieved))
    print("Not Retrieved & Irrelevant = " + str(not_and_irrel))
    
