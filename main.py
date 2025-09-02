import sys
import os

# Add the folder containing main.py to module search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from xmlReader import read_XML
from parser import parse
from shutil import copy
from datetime import datetime
from filler import fill_doc
from loger import log


def main() -> None:
    error = ""
    
    now = datetime.now()
    # Format it as YYYY-MM-DD_HH-MM
    timestamp = now.strftime("%Y-%m-%d_%H-%M")

    applicant = None
    project_owner = None
    new_doc = ""
    
    try:
        template_name = "VZOR - Záväzné vyjadrenie DPO.docx"
        input_file = "šišan.xml" 
        data = read_XML(input_file)
        applicant, project_owner, project = parse(data)

        new_doc = f"Záväzné vyjadrenie DPO {applicant.get_full_name()} ({timestamp}).docx"
        copy(template_name, new_doc)

        fill_doc(new_doc, applicant, project_owner, project, timestamp)
    
    except FileNotFoundError as e:
        error = "Súbor sa nenašiel. Prosím skontrolujte, či zadaný súbor existuje v pracovnom adresári." \
                " Vyhodená chyba: \n" + str(e)
    
    except Exception as e:
        error = "Počas behu programu sa objavila neočakávaná chyba :(. Vyhodená chyba: \n" + str(e)
    
    log_name = f"log_{timestamp}.txt"
    log(log_name, new_doc, timestamp, error, applicant, project_owner)
    print(f"Program zbehol. Záznam o priebehu je v súbore {log_name}")
    input("Press Enter to exit...")
        

if __name__ == "__main__":
    main()