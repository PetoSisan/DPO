from Person import Person


def log(log_name: str, new_doc: str, error: str,applicant: Person,
        project_owner: Person, project_id: str) -> None:
    with open(log_name, "a", encoding="utf-8") as f:
        f.write(f"Záznam o priebehu spracovaní žiadosti stavby s ID \"{project_id}\": \n")

        if (len(error) != 0):
            f.write(error)
            return

        missing_data = ""
        missing_attrs = applicant.get_missing_attrs()

        if len(missing_attrs) != 0:
            missing_data += f"V žiadosti chýbajú niektoré dáta o žiadateľovi: {missing_attrs} \n"

        missing_attrs = project_owner.get_missing_attrs()

        if len(missing_attrs) != 0:
            missing_data += f"V žiadosti chýbajú niektoré dáta o stavebníkovi: {missing_attrs} \n"
        
        if len(missing_data) != 0:
            f.write(missing_data)
        
        f.write(f"Program prebehol úspešne. Výstup môžete nájsť v súbore \"{new_doc}\". \n\n")