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

from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
# import io

def convert(filename):
    resource_manager = PDFResourceManager()
    fake_file_handle = StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(filename, 'rb') as fh:

        for page in PDFPage.get_pages(fh,
                                    caching=True,
                                    check_extractable=True):
            page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()
    converter.close()
    fake_file_handle.close()
    print(text)

def read_text(filename):
    output_string = StringIO()
    with open(filename, 'rb') as in_file:
        text2=extract_text(in_file)
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
    return output_string.getvalue()


if __name__ == "__main__":
    filename="cec2019\Evolving task priority rules for heterogeneous assembly line balancing.pdf"
    filename="08790014.pdf"
    # filename="cec2020\A Comparative Study of Genetic Algorithm and Particle Swarm optimisation for Dendritic Cell Algorithm.pdf"
    # text=read_text(filename)
    # pattern=re.compile(r"[0-9a-zA-Z_\.]+@[0-9a-zA-Z_]+(?:\.[a-zA-Z]+)+")
    # pattern2=re.compile(r"\{[0-9a-zA-Z_\.\,]+\}@[0-9a-zA-Z_]+(?:\.[a-zA-Z]+)+")
    # result=pattern2.findall(text)
    # print(text)

    
    
    convert(filename)