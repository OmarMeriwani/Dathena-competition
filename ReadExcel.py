import pandas

def ReadExcel(path):
    df = pandas.read_excel(path,sheet_name=None)#.values.tolist()
    text = ''
    for sheet in df:
        df2 = pandas.read_excel(path,sheet_name=sheet).values.tolist()
        for d in df2:
            dd = [str(n) for n in d]
            text += ' '.join(dd)
            text += '\n'
    print(text)
    return text

ReadExcel("E:/dathena-competition/files/Keppel/A-K.xls")