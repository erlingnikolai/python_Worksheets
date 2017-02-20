import requests
import bs4
import string # for string.punctuation
import csv


"""
The translation dictionary is defined once at the start of the file
and then not changed.
"""
translation = str.maketrans({p : None for p in string.punctuation})


        

def remove_punctuation(text):
    """
    removePunctuation takes a string parameter and returns
    a copy of the string with the punctuation removed.
    """
    text = text.translate(translation)
    return text

def make_words(para_text):
    """Chop a paragraph into cleaned words"""
    no_newlines    = para_text.strip()
    lowercase_text = no_newlines.lower()
    no_punc        = remove_punctuation(lowercase_text)
    words          = no_punc.split()
    return words


# Edit code below this line
# ---------------------------------------------------

def request_and_soup(url):
  
    response = requests.get(url)
    print(response.status_code)
    xml_text = response.text
    soup = bs4.BeautifulSoup(xml_text, "xml")
    #print(soup)
    return soup


def get_wordBlocks(soup):
    paras = soup.find_all(attrs={"class":"hs_Para"})
    return [make_words(p.text) for p in paras]

def make_counts(wordBlocks):
    words_dict = {}
    for block in wordBlocks:
        for word in block:
        
            if word in words_dict:
                words_dict[word]+=1
            else:
                words_dict[word] = 1
    
    
    # add code here 
    return words_dict


def report_counts(freqs, infile_name, outfile_name):
    with open (outfile_name, "w", newline = '\n') as my_outfile:
        csv_out = csv.writer(my_outfile, dialect = "excel")
        with open (infile_name, "r") as my_inputfile:         
            for line in my_inputfile:
                removeEnter = line.rstrip()
                if removeEnter in freqs:
                    csv_out.writerow([removeEnter, freqs[removeEnter]])
            #    for word in freqs:
             #       if (removeEnter == word):
              #          print(removeEnter)
               #         print(word)
                #        csv_out.writerow([removeEnter, freqs[word]])


    
    


def main():
    url = "https://hansard.parliament.uk/Commons/2016-11-23/debates/4F39F2C9-583D-407B-A529-3956F6A927F1/AutumnStatement"
    soup = request_and_soup(url)
    paras = get_wordBlocks(soup)
    freqs = make_counts(paras)
  #  print (freqs)
    report_counts(freqs, "words.txt", "out.csv")


if __name__ == "__main__":
    main()