import PyPDF2

def readPdfFile(path):
    pdfFileObj = open(path, 'rb')


    '''pdfFileObj = open('E:/dathena-competition/files/Keppel/KLL_SR2011.pdf', 'rb')'''
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    fullText = ""
    for i in range(0,pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        pagetext = str(pageObj.extractText())
        #print(pagetext)
        fullText += pagetext
    return fullText

#print(readPdfFile('E:/dathena-competition/files/Keppel/KLL_SR2011.pdf'))
