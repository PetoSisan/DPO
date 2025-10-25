from Person import Person

def add_missing_attrs(person: Person) -> str:
    missing_data = ""
    missing_attrs = person.get_missing_attrs()

    if len(missing_attrs) != 0:
        missing_data += f"V žiadosti chýbajú niektoré dáta o osobe \"{person.get_full_name()}\": {missing_attrs} \n"

    return missing_data


def log(log_name: str, new_doc: str, error: str, applicants: list[Person],
        project_owners: list[Person], project_id: str) -> None:
    with open(log_name, "a", encoding="utf-8") as f:
        f.write(f"Záznam o priebehu spracovaní žiadosti stavby s ID \"{project_id}\": \n")

        if (len(error) != 0):
            f.write(error)
            return

        missing_data = ""
        for applicant in applicants:
            missing_data += add_missing_attrs(applicant)
        
        for project_owner in project_owners:
            missing_data += add_missing_attrs(project_owner)
        
        if len(missing_data) != 0:
            f.write(missing_data)
        
        f.write(f"Program prebehol úspešne. Výstup môžete nájsť v súbore \"{new_doc}\". \n\n")