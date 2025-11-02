from openpyxl import load_workbook


class StudentLivesXlsx:
    def __init__(self, path_to_table: str):
        self._wb = load_workbook(path_to_table)
        self._ws = self._wb.active
    
if __name__ == "__main__":
    StudentLivesXlsx("source\StudentLives.xlsx")   