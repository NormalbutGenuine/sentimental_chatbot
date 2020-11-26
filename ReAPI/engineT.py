from konlpy.tag import Komoran
import numpy as np
from numpy import dot
from numpy.linalg import norm
from gensim.models import Word2Vec
import json
# 코사인 유사도 계산
def cos_sim(vec1, vec2):
    return dot(vec1, vec2)/(norm(vec1)*norm(vec2))

def make_term_doc_mat(sentence_bow, word_dics):
    freq_mat = {}
    for word in word_dics:
        freq_mat[word]=0
        
    for word in word_dics:
        if word in sentence_bow:
            freq_mat[word] +=1

    return freq_mat

# 단어 벡터 만들기
def make_vector(tdm):
    vec=[]
    for key in tdm:
        vec.append(tdm[key])
    return vec

def engine(query):
    komoran = Komoran()
    

    file_path = "감성대화말뭉치.json"
    with open(file_path, "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)

    jdic1 = json_data[0]
    jdic2 = jdic1['talk']
    jdic3 = jdic2['content']
    # HS01 = jdic3['HS01']

    HS01 = [k for k in range(0,9171)] # len = 9171
    HS02 = [j for j in range(0, 9171)]
    HS03 = [q for q in range(0, 9171)]
    SS01 = [r for r in range(0, 9171)]
    SS02 = [x for x in range(0, 9171)]
    SS03 = [z for z in range(0, 9171)]

    for i in range(0, len(json_data)):
        jdic1 = json_data[i]
        jdic2 = jdic1['talk']
        jdic3 = jdic2['content']
        HS01[i] = jdic3['HS01']
        HS02[i] = jdic3['HS02']
        HS03[i] = jdic3['HS03']
        SS01[i] = jdic3['SS01']
        SS02[i] = jdic3['SS02']
        SS03[i] = jdic3['SS03']

    SSBOX = SS01+SS02+SS03
    f = open("sratings.txt", "r", encoding="utf-8")
    fr = f.read()
    flr = list(fr)
    fr2 = fr.split("\t")
    fr3 = fr2[3:len(fr2)]
    BOW = SS01+SS02+SS03+fr3
    len2 = [k for k in range(0, len(BOW))]
    vecto = [v for v in range(0, len(BOW))]

    t=1
    r1 = 0
    print('대화시작')
    while t:
            
        if query != "종료":
            sen1 = komoran.nouns(query)
            sen2 = [komoran.nouns(BOW[i]) for i in range(0, len(BOW))]
            for j in range(0, len(BOW)):
                sent = sen1+sen2[j]
                word_dics = []
                for token in sent:
                    if token not in word_dics:
                        word_dics.append(token)    
                    
                freq_list1 = make_term_doc_mat(sen1, word_dics)
                freq_list2 = make_term_doc_mat(sen2[j], word_dics)
                
                vec1 = np.array(make_vector(freq_list1))
                vec2 = np.array(make_vector(freq_list2))

                r1 = cos_sim(vec1, vec2)
                vecto[j] = r1
                
            
            rmax = max(vecto)
            idx = vecto.index(rmax)
            return BOW[idx]
            
                
        elif query == "종료":
            t=0
