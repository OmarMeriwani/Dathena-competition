import pandas as pd

df = pd.read_csv('dataset.csv').values.tolist()
df2 = pd.DataFrame(columns=['fileid','company','text'])
seq = 0
for doc in df:
    id = doc[1]
    company = str(doc[2])
    print(company)
    text = str(doc[3])
    usefultext = ''
    paragraphs = [str(p).lower() for p in text.split('.')]
    for p in paragraphs:
        if p.find(company.lower()) != -1:
            usefultext += p + '\n'
            print(p)
    df2.loc[seq] = [id,company, usefultext]
    seq += 1
df2.to_csv('dataset2.csv')

