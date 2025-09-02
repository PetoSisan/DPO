from Person import Person


def log(log_name: str, new_doc: str, timestamp: str, error: str, applicant: Person, project_owner: Person) -> None:
    with open(log_name, "a", encoding="utf-8") as f:
        if (len(error) != 0):
            f.write(error)
            return

        missing_data = ""

        if not applicant.is_complete():
            missing_data += f"V žiadosti chýbajú niektoré dáta o žiadateľovi: {applicant.get_missing_attrs()}"

        if not project_owner.is_complete():
            missing_data += f"V žiadosti chýbajú niektoré dáta o stavebníkovi: {project_owner.get_missing_attrs()}"
        
        if len(missing_data) != 0:
            f.write(missing_data)
        
        f.write(f"Program prebehol úspešne. Výstup môžete nájsť v súbore \"{new_doc}\".")