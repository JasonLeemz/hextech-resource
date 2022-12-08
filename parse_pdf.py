import json

import pdfplumber
import pandas as pd


def parse():
    pdf_file = r'/Users/limingze/PycharmProjects/pythonProject/b4lz.pdf'

    pdf = pdfplumber.open(pdf_file)

    result_df = pd.DataFrame()
    for page in pdf.pages[55:56]:
        words = page.extract_text()
        print(words)
        # words_str = json.dumps(words)
        # print('name============================================================')
        # print(words_str)

        # text = page.annots
        # text_str = json.dumps(text)
        # print('text============================================================')
        # print(text_str)

        # tables = page.extract_tables()
        # if tables:
        #     for table in tables:
        #         print('table============================================================')
        #         table_str = json.dumps(table)
        #         print(table_str)
