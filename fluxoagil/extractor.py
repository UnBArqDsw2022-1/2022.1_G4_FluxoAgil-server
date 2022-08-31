import camelot
import fitz
import re
import pandas

class ContentExtractor:
    """Class to extract historic data"""
    def __init__(self, historic):
        self._historic = historic
        self.curriculun_number = ''
        self.extract_curriculum()
        self.aproved_courses = []
        self.academic_history = {}
        self.extract_tables()

    def _is_a_done_table(self, table):
        """Returns True if a table is a done table"""
        pandas_table = table.df
        if len(pandas_table.columns) == 9:
            return True
        else:
            return False

    def _is_a_hour_table(self, table):
        """Returns True if a table is a hour table"""
        pandas_table = table.df
        if len(pandas_table.columns) == 5:
            return True
        else:
            return False

    def _add_to_done_table(self, table):
        """Save aproved courses in a list"""
        for i, linha in table.df.iterrows():
            if 'APR' in linha[8]:
                self.aproved_courses.append(linha[2])

    def _add_to_academic_history(self, table):
        for i, linha in table.df.iterrows():
            if i == 1:  # Mandatory
                required_mandatory = linha[1].replace(" h", "")
                required_optional = linha[2].replace(" h", "")
                required_supplementary = linha[3].replace(" h", "")
                required_total = linha[4].replace(" h", "")
                
            if i == 2:  # Integrated
                integrated_mandatory = linha[1].replace(" h", "")
                integrated_optional = linha[2].replace(" h", "")
                integrated_supplementary = linha[3].replace(" h", "")
                integrated_total = linha[4].replace(" h", "")

            if i == 3:  # Pending
                pending_mandatory = linha[1].replace(" h", "")
                pending_optional = linha[2].replace(" h", "")
                pending_supplementary = linha[3].replace(" h", "")
                pending_total = linha[4].replace(" h", "")

        academic_history = self.make_academic_history(
            required_mandatory = int(required_mandatory),
            required_optional = int(required_optional),
            required_supplementary = int(required_supplementary),
            required_total = int(required_total),
            integrated_mandatory = int(integrated_mandatory),
            integrated_optional = int(integrated_optional),
            integrated_supplementary = int(integrated_supplementary),
            integrated_total = int(integrated_total),
            pending_mandatory = int(pending_mandatory),
            pending_optional = int(pending_optional),
            pending_supplementary = int(pending_supplementary),
            pending_total = int(pending_total)
        )
        self.academic_history = academic_history


    def extract_tables(self):
        """Extract historic tables"""
        tables = camelot.read_pdf(self._historic, pages='all')

        for index, table in enumerate(tables):
            if self._is_a_done_table(table):
                self._add_to_done_table(table)
            if self._is_a_hour_table(table):
                self._add_to_academic_history(table)

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
            self.curriculun_number = match.replace(' -', '')
            return self.curriculun_number

    def extract_curriculum(self):
        """Read first page text to extract curriculum"""
        doc = fitz.open(self._historic)  
        text = doc[0].get_text()
        text = self.find_curriculum(text)
    
    def make_academic_history(self, **kwargs):
        return {
            "curriculum_id": self.curriculun_number,
            "approved_courses": self.aproved_courses,
            "workload": {
                "mandatory": {
                    "required": kwargs['required_mandatory'],
                    "integrated": kwargs['integrated_mandatory'],
                    "pending": kwargs['pending_mandatory']
                },
                    "optional": {
                    "required": kwargs['required_optional'],
                    "integrated": kwargs['integrated_optional'],
                    "pending": kwargs['pending_optional']
                },
                "supplementary": {
                    "required": kwargs['required_supplementary'],
                    "integrated": kwargs['integrated_supplementary'],
                    "pending": kwargs['pending_supplementary']
                },
                "total": {
                    "required": kwargs['required_total'],
                    "integrated": kwargs['integrated_total'],
                    "pending": kwargs['pending_total']
                }
            }
        }
