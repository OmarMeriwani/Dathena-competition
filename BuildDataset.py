import pandas
import ReadExcel
import ReadWord
import ReadPDF
import ReadFolder

ds = pandas.DataFrame(columns=['fileid','company','text'])
df = pandas.read_csv('submission_mapper.csv', delimiter='|').values.tolist()
path = 'E:/dathena-competition/files'
seq = 0
for file in df:
    id = file[0]
    filename = file[1]
    folder = file[2]
    text = ''
    ext = ReadFolder.getFileExt(filename)
    try:
        if ext == 'pdf':
            text = ReadPDF.readPdfFile(path + '/' + folder + '/' +  filename)
        if ext == 'xls' or ext == 'xlsx':
            text = ReadExcel.ReadExcel(path + '/' + folder + '/' + filename)
        if ext == 'doc':
            text = ReadWord.ReadDoc(path + '/' + folder + '/' + filename)
        if ext == 'docx':
            text = ReadWord.ReadDocx(path + '/' + folder + '/' + filename)
    except:
        text = ''
    text = str(text)
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    print(id,folder, filename)
    ds.loc[seq] = [id,folder,text]
    seq+= 1
ds.to_csv('dataset.csv')