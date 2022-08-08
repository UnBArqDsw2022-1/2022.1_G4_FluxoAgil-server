import camelot
import pandas as pd

class ContentExtractor:
    """Classe para extrair dados do histórico"""
    def __init__(self, historic):
        self._historic = historic
        self.aproved_courses = []
        self.extract_tables()

    def _is_a_done_table(self, table):
        pandas_table = table.df
        if len(pandas_table.columns) == 9:
            return True
        else:
            return False

    def _add_to_done_table(self, table):
        for i, linha in table.df.iterrows():
            if 'APR' in linha[8]:
                self.aproved_courses.append(linha[2])

    def extract_tables(self):
        tables = camelot.read_pdf(self._historic, pages='all')

        for index, table in enumerate(tables):
            if self._is_a_done_table(table):
                self._add_to_done_table(table)
