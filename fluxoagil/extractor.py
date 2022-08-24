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
                required_mandatory = linha[1]
                required_optional = linha[2]
                required_supplementary = linha[3]
                required_total = linha[4]
                
            if i == 2:  # Integrated
                integrated_mandatory = linha[1]
                integrated_optional = linha[2]
                integrated_supplementary = linha[3]
                integrated_total = linha[4]

            if i == 3:  # Pending
                pending_mandatory = linha[1]
                pending_optional = linha[2]
                pending_supplementary = linha[3]
                pending_total = linha[4]

        academic_history = self.make_academic_history(
            required_mandatory = required_mandatory,
            required_optional = required_optional,
            required_supplementary = required_supplementary,
            required_total = required_total,
            integrated_mandatory = integrated_mandatory,
            integrated_optional = integrated_optional,
            integrated_supplementary = integrated_supplementary,
            integrated_total = integrated_total,
            pending_mandatory = pending_mandatory,
            pending_optional = pending_optional,
            pending_supplementary = pending_supplementary,
            pending_total = pending_total
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
            "curriculumId": self.curriculun_number,
            "approvedCourses": self.aproved_courses,
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

