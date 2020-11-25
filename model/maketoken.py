from konlpy.tag import Kkma
from konlpy.tag import Komoran
from gensim.models import Word2Vec
import json

# 코모란 형태소 분석기 객체 생성
komoran = Komoran(userdic="./user_dic.txt")
text = "ㅋㅋㅋ 너에게 가는 이 길이 엔엘피와 같구나. 어떻게 구트" 
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

model = Word2Vec(sentences=SSBOX, size=250, window=1, hs=1, min_count=1, sg=1)
model.save('word.model')
print(model.corpus_count)
print(model.corpus_total_words)

s2 = [k for k in range(0, len(SSBOX))]

for i in range(0, len(SSBOX)):
    s2[i] = komoran.nouns(SSBOX[i])

model2 = Word2Vec(sentences=s2, size=250, window=1, hs=1, min_count=1, sg=1)
model2.save('word2.model')
print(model2.corpus_total_words)
# 형태소 추출
# morphs = komoran.morphs(text)
# print(morphs)

# # 형태소와 품사 태그 추출
# pos = komoran.pos(text)
# print(pos)

# 명사만 추출
# nouns = komoran.nouns(text)
# print(nouns)

