from docx import Document
from docx.shared import RGBColor
from Person import Person
from Project import Project

INCOMPLETE_DATA = "Ostatné údaje nie sú dostupné v žiadosti ani v PD."


def fill(doc: Document, cell, applicants: list[Person], project_owners: list[Person],
         project: Project, table: int, row: int, c: int) -> None:
    text = cell.text.strip()

    if text == "Meno Priezvisko":
        cell.text = ""
        for applicant in applicants:
            cell.text += applicant.get_full_name()
    
    elif text == "Ulica číslo":
        cell.text = ""
        for applicant in applicants:
            cell.text += f"{applicant.address.street} {applicant.address.building_number}"

    elif text == "PSČ Mesto":
        cell.text = ""
        for applicant in applicants:
            cell.text += f"{applicant.address.postal_code} {applicant.address.city}"
    
    elif text == "Žiadateľ":
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = ""
        for applicant in applicants:
            next_cell.text += applicant.to_string()

            if not applicant.is_complete():
                next_cell.text += f"\n{INCOMPLETE_DATA}\n"
            
    
    elif text == "Stavebník":
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = ""
        for project_owner in project_owners:
            next_cell.text += project_owner.to_string()

            if not project_owner.is_complete():
                next_cell.text += f"\n{INCOMPLETE_DATA}\n"
    
    elif "ID stavby" in cell.text:
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = project.id
    
    elif text == "Názov stavby":
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = project.title

    elif text == "Identifikačné údaje stavby":
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = project.format_parcels()
    
    elif text == "Členenie stavby":
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = project.format_facilities()



def fill_doc(file_name: str, applicants: list[Person], project_owners: list[Person],
             project: Project, timestamp: str) -> list[str]:
    doc = Document(file_name)   

    for t, table in enumerate(doc.tables):
        for r, row in enumerate(table.rows):
            for c, cell in enumerate(row.cells):
                fill(doc, cell, applicants, project_owners, project, t, r, c)
    
    doc.paragraphs[len(doc.paragraphs) - 1].text = f"Edited by script on {timestamp}"
    run = doc.paragraphs[len(doc.paragraphs) - 1].runs[0]
    run.font.color.rgb = RGBColor(255, 255, 255)
    doc.save(file_name)


