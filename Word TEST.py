import ReadWord
import os
import zipfile
#other tools useful in extracting the information from our document
import re
#to pretty print our xml:
import xml.dom.minidom
document = zipfile.ZipFile('E:/Week 6 Pain metaphors and pain constructions.docx')
#print(ReadWord.ReadDocx('E:/Week 6 Pain metaphors and pain constructions.docx'))
document.namelist()

uglyXml = xml.dom.minidom.parseString(document.read('word/fontTable.xml')).toprettyxml(indent='  ')

text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
prettyXml = text_re.sub('>\g<1></', uglyXml)

print(prettyXml)
uglyXml = xml.dom.minidom.parseString(document.read('word/document.xml')).toprettyxml(indent='  ')

text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)
prettyXml = text_re.sub('>\g<1></', uglyXml)

print(prettyXml)
#first to turn the xml content into a string:
xml_content = document.read('word/document.xml')
document.close()
xml_str = str(xml_content)
print(xml_str)
link_list = re.findall('http.*?\<',xml_str)[1:]
link_list = [x[:-1] for x in link_list]
print(link_list)