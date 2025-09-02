from docx import Document
from docx.shared import RGBColor
from Person import Person
from Project import Project

INCOMPLETE_DATA = "Ostatné údaje nie sú dostupné v žiadosti ani v PD."


def fill(doc: Document, cell, applicant: Person, project_owner: Person, project: Project,
         table: int, row: int, c: int ) -> None:
    if cell.text.strip() == "Meno Priezvisko":
        cell.text = applicant.get_full_name()
    
    elif cell.text.strip() == "Ulica číslo":
        cell.text = f"{applicant.address.street} {applicant.address.building_number}"

    elif cell.text.strip() == "PSČ Mesto":
        cell.text = f"{applicant.address.postal_code} {applicant.address.city}"
    
    if cell.text == "Žiadateľ":
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = applicant.to_string()
        if not applicant.is_complete():
            next_cell.text += f"\n\n{INCOMPLETE_DATA}"
    
    if cell.text == "Stavebník":
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = project_owner.to_string()
        if not project_owner.is_complete():
            next_cell.text += f"\n\n{INCOMPLETE_DATA}"
    
    if "ID stavby" in cell.text:
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = project.id
    
    if cell.text == "Názov stavby":
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = project.title

    if cell.text == "Identifikačné údaje stavby":
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = project.format_parcels()
    
    if cell.text == "Členenie stavby":
        next_cell = doc.tables[table].rows[row].cells[c + 1]
        next_cell.text = project.format_facilities()



def fill_doc(file_name: str, applicant: Person, project_owner: Person, project: Project, timestamp: str) -> list[str]:
    doc = Document(file_name)   

    for t, table in enumerate(doc.tables):
        for r, row in enumerate(table.rows):
            for c, cell in enumerate(row.cells):
                fill(doc, cell, applicant, project_owner, project, t, r, c)
    
    doc.paragraphs[len(doc.paragraphs) - 1].text = f"Edited by script on {timestamp}"
    run = doc.paragraphs[len(doc.paragraphs) - 1].runs[0]
    run.font.color.rgb = RGBColor(255, 255, 255)
    doc.save(file_name)


