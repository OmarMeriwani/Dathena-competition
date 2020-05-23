import pandas as pd
import re

df = pd.read_csv('dataset.csv').values.tolist()
df2 = pd.DataFrame(columns=['fileid','company','text'])
seq = 0
for doc in df:
    id = doc[1]
    company = str(doc[2])
    print(company)
    text = str(doc[3])
    usefultext = ''
    #paragraphs = [str(p).lower() for p in text.split('.')]
    paragraphs = re.split('.', text)
    for p in paragraphs:
        print(p)
        if p.lower().find(company.lower()) != -1:
            usefultext += p + '\n'
            print(p)
    df2.loc[seq] = [id,company, usefultext]
    seq += 1
df2.to_csv('dataset2.csv')

