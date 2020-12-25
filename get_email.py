import os
import io
import pdfminer
import re
from tqdm import tqdm
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser



laparams = pdfminer.layout.LAParams()
setattr(laparams, 'all_texts', True)
ans=set()

def read_text(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=laparams)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, 
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()

    if text:
        return text



def main():
    path='cec2020'
    file=os.listdir(path)
    # print(file)
    for lastname in tqdm(file):
        filename=path+os.sep+lastname
        try:
            text=read_text(filename)
            pattern=re.compile(r"[0-9a-zA-Z_\-\.]+@[0-9a-zA-Z_]+(?:\.[a-zA-Z\-\_]+)+")
            pattern2=re.compile(r"\{[0-9a-zA-Z\-_\.\,]+\}@[0-9a-zA-Z_]+(?:\.[a-zA-Z\-\_]+)+")
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