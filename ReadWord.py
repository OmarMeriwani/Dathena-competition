import textract
import docx2txt
import os
import pandas

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Git/mingw64/bin'
def ReadDocx(path):
    my_text = docx2txt.process(path)
    return my_text

def ReadDoc(path):
    text = textract.process(path)
    return text
#print(ReadDoc('E:/dathena-competition/files/Keppel/P020160628597921671163.doc'))
