import camelot
import fitz
import re
import pandas as pd

class ContentExtractor:
    """Class to extract historic data"""
    def __init__(self, historic):
        self._historic = historic
        self.aproved_courses = []
        self.extract_tables()
        self.curriculun_number = ''
        self.extract_curriculum()

    def _is_a_done_table(self, table):
        """Returns True if a table is a done table"""
        pandas_table = table.df
        if len(pandas_table.columns) == 9:
            return True
        else:
            return False

    def _add_to_done_table(self, table):
        """Save aproved courses in a list"""
        for i, linha in table.df.iterrows():
            if 'APR' in linha[8]:
                self.aproved_courses.append(linha[2])

    def extract_tables(self):
        """Extract historic tables"""
        tables = camelot.read_pdf(self._historic, pages='all')

        for index, table in enumerate(tables):
            if self._is_a_done_table(table):
                self._add_to_done_table(table)

    def find_curriculum(self, text):
        """
        Prepare the text for extration and
        find curriculum number using regex
        """
        blocks = re.split('\n\n', text)
        # 
        for block in blocks:
            pattern = r"\d+/-?\d -"
            match = re.findall(pattern, block)
            match = "".join(match)
            self.curriculun_number = match.replace('-', '')
            return self.curriculun_number

    def extract_curriculum(self):
        """Read first page text to extract curriculum"""
        doc = fitz.open(self._historic)  
        text = doc[0].get_text()
        text = self.find_curriculum(text)
