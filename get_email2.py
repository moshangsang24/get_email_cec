import os
from io import StringIO
import re
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from tqdm import tqdm


ans=set()

def read_text(filename):
    output_string = StringIO()
    with open(filename, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return output_string.getvalue()



def main():
    path='gecco2020'
    file=os.listdir(path)
    # print(file)
    for lastname in tqdm(file):
        filename=path+os.sep+lastname
        try:
            text=read_text(filename)
            pattern=re.compile(r"[0-9a-zA-Z_\.]+@[0-9a-zA-Z_]+(?:\.[a-zA-Z]+)+")
            pattern2=re.compile(r"\{[0-9a-zA-Z_\.\,]+\}@[0-9a-zA-Z_]+(?:\.[a-zA-Z]+)+")
            result=pattern2.findall(text)
            result2=pattern.findall(text)
            ans.update(result)
            ans.update(result2)
            print(result,result2)
        except:
            print("{} is wrong!".format(lastname))
    with open(path+"_email.txt","w") as f:
        for i in ans:
            print(i,file=f)
if __name__ == "__main__":
    main()