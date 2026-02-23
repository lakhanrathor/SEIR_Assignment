
import re #regex function
import sys # to get urls from command line
import requests 
from bs4 import BeautifulSoup 

# download the webpage and clean the text
def webToText(url):
    data = requests.get(url)  
    page_content = data.text
    soup = BeautifulSoup(page_content, "html.parser")
    remove_tags = soup(["script", "style"])

    for tag in remove_tags:
        tag.extract() # removing those tags from html page

    body_text = soup.get_text() 
    text = body_text.lower()
    text = re.sub(r'[^a-z0-9\s]',' ', text)
    text = re.sub(r'\s+', ' ', text)
    clean_text = text.strip()
    return clean_text

def tokenization(clean_text):
    wordList = clean_text.split()
    return wordList


# creating dictionary  {word: frequency}
def frequency(wordList):
    dic={}
    for word in wordList:
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1
    return dic

#converting each word into 64 bit polynomial rolling hash
def rolling_hash(word):
    p = 53
    mod = 2**64
    hash=0
    power =1

    for char in word:
        hash = (hash + ord(char)* power) %mod
        power = (power*p)%mod
    return hash


# simhash function: creating 64 bit fingerprint for the document 
def simhash(frequency_dic, hash_dic):
    vector =[0]* 64
    for word, freq in frequency_dic.items():
        hash = hash_dic[word]
        for i in range(64):
            bit =(hash >>i)&1
            if bit == 1:
                vector[i]+= freq
            else:
                vector[i] -= freq
    final_hash =0
    for i in range(64):
        if vector[i]>0:
            final_hash |= (1<<i)
    return final_hash

 # compare two documents based on their fingerprints
def common_bits(h1, h2):
    xor = h1^h2
    diff_bit = bin(xor).count('1')
    similar_bits = 64- diff_bit
    return similar_bits


# executing our program 
def main():
    if len(sys.argv) < 3:
        print("input format: python script.py url1 url2")
        sys.exit()

    url1 = sys.argv[1]
    url2 = sys.argv[2]

    text1 = webToText(url1)
    words1 = tokenization(text1)
    freq1 = frequency(words1)

    dic1_hash = {}
    for word in freq1:
        dic1_hash[word] = rolling_hash(word)

    doc1_hash = simhash(freq1, dic1_hash)

    text2 = webToText(url2)
    word2 = tokenization(text2)
    freq2 = frequency(word2)

    dic2_hash = {}
    for word in freq2:
        dic2_hash[word] = rolling_hash(word)

    doc2_hash = simhash(freq2, dic2_hash)

    similar = common_bits(doc1_hash, doc2_hash)
    print("Number of common bits:", similar)


main()