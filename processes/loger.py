from entities.Person import Person

def add_missing_attrs(person: Person) -> str:
    missing_data = ""
    missing_attrs = person.get_missing_attrs()

    if len(missing_attrs) != 0:
        missing_data += f"V žiadosti chýbajú niektoré dáta o osobe \"{person.get_full_name()}\": {missing_attrs} \n"

    return missing_data



# missing_data = ""
# for applicant in applicants:
#     missing_data += add_missing_attrs(applicant)

# for project_owner in project_owners:
#     missing_data += add_missing_attrs(project_owner)


def log(log_name: str, new_doc_name: str, error: str,
        project_id: str, missing_data: str) -> None:
    
    with open(log_name, "a", encoding="utf-8") as f:
        f.write(f"Záznam o priebehu spracovaní žiadosti stavby s ID \"{project_id}\": \n")

        if (len(error) != 0):
            f.write(error)
            return
        
        if len(missing_data) != 0:
            f.write(missing_data)
        
        f.write(f"Program prebehol úspešne. Výstup môžete nájsť v súbore \"{new_doc_name}\". \n\n")



def record(error: str, timestamp: str, new_doc_name: str, project_id: str,
           missing_data: str) -> int:
    success = "úspešne" if error == "" else "neúspešne"
    log_name = f"log_{success}_{timestamp}.txt"
    
    log(log_name, new_doc_name, error, project_id, missing_data)

    print(f"Program prebehol {success}.")
    if len(error) != 0:
        print(f"{error} \n")

    print(f"Záznam o priebehu programu je uložený v súbore {log_name}")
