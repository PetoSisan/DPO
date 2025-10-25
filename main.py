from xmlReader import read_XML
from parser import parse
from parser import get_project_id
from shutil import copy
from datetime import datetime
from filler import fill_doc
from loger import log
from Person import Person
from Project import Project


def main() -> None:
    error = ""
    
    now = datetime.now()
    # Format it as YYYY-MM-DD_HH-MM
    timestamp = now.strftime("%Y-%m-%d_%H-%M")

    applicants: list[Person] | None = None
    project_owners: list[Person] | None = None
    project: Project = None
    new_doc = ""
    data = None
    
    try:
        template_name = "VZOR - Záväzné vyjadrenie DPO.docx"
        input_file = "šišan.xml" 
        data = read_XML(input_file)
        applicants, project_owners, project = parse(data)

        new_doc = f"{project.id} - DPO ({timestamp}).docx"
        copy(template_name, new_doc)

        fill_doc(new_doc, applicants, project_owners, project, timestamp)
    
    except FileNotFoundError as e:
        error = "Súbor sa nenašiel. Prosím skontrolujte, či zadaný súbor existuje v pracovnom adresári." \
                f" Vyhodená chyba: \n {str(e)} \n"
    
    except Exception as e:
        error = f"Počas behu programu sa objavila neočakávaná chyba :(. Vyhodená chyba: \n {str(e)} \n"
    
    success = "úspešne" if error == "" else "neúspešne"
    log_name = f"log_{success}_{timestamp}.txt"

    project_id = "ID stavby nebolo nájdené"
    if project is not None:
        project_id = project.id
    
    if project is None and data is not None:
        project_id = get_project_id(data)
    
    log(log_name, new_doc, error, applicants, project_owners, project_id)

    print(f"Program prebehol {success}.")
    if len(error) != 0:
        print(f"{error} \n")

    print(f"Záznam o priebehu programu je uložený v súbore {log_name}")

    input("Press Enter to exit...")
        

if __name__ == "__main__":
    main()