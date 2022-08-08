import camelot
import pandas as pd

class ContentExtractor:
    """Classe para extrair dados do histórico"""
    def __init__(self):
        self._historic = self._load_historic()

    def _load_historic(self):
        filename = ''
        return filename

    def add_to_pendency_table(self, table):
        pass

    def add_to_done_table(self, table):
        for i, linha in table.df.iterrows():
                    print(f"course: {linha[3]}, situation: {linha[8]}") 

    def extract_tables(self):
        tables = camelot.read_pdf(self._historic, pages='all')
        pendent_table = len(tables) -1 
        limit = len(tables) - 3
        for index, table in enumerate(tables):

            if index == pendent_table:
                self.add_to_pendency_table(table)
            elif index >= limit:
                pass
            else:
                self.add_to_done_table(table)
