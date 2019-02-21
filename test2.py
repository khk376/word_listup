import time
import pandas as pd

from konlpy.tag import Kkma, Okt, Komoran

from konlpy.tag import Okt
from collections import Counter

from konlpy.tag import Kkma, Okt, Komoran
pos_taggers = [('kkma', Kkma()), ('twitter', Okt()), ('Komoran', Komoran())]
results = []

texts = pd.read_csv('C:\\Users\\Playdata\\Desktop\\output2.csv', header=None)
texts.columns=['문장']
for name, tagger in pos_taggers:
    if name=='Komoran':
        tokens = []
        process_time = time.time()
        for text in texts['문장']:
            tokens.append(tagger.pos(text))
        process_time = time.time() - process_time
        print('tagger name = %10s, %.3f secs' % (name, process_time))
        results.append(tokens)

print(results)