from entities.Person import Person
from datetime import datetime


def find_missing_attrs(person: Person, person_role: str) -> str:
    missing_data = ""
    missing_attrs = person.get_missing_attrs()

    if len(missing_attrs) != 0:
        missing_data += f"V žiadosti chýbajú niektoré dáta o osobe \"{person.get_full_name()}\" s rolou '{person_role}': {missing_attrs} \n"

    return missing_data


def find_missing_data(applicants: list[Person], project_owners: list[Person]) -> str:
    missing_data = ""
    for applicant in applicants:
        missing_data += find_missing_attrs(applicant, "Žiadateľ")

    for project_owner in project_owners:
        missing_data += find_missing_attrs(project_owner, "Stavebník")

    return missing_data


def log(
    log_name: str, new_doc_name: str, error: str, project_id: str, missing_data: str
) -> None:

    with open(log_name, "a", encoding="utf-8") as f:
        f.write(f'Záznam o priebehu spracovaní žiadosti stavby s ID "{project_id}": \n')

        if len(error) != 0:
            f.write(error)
            return

        if len(missing_data) != 0:
            f.write(missing_data)

        f.write(
            f'Program prebehol úspešne. Výstup môžete nájsť v súbore "{new_doc_name}". \n\n'
        )


def record(
    error: str,
    date_time: datetime,
    new_doc_name: str,
    project_id: str,
    missing_data: str,
) -> None:

    timestamp = date_time.strftime("%Y-%m-%d_%H-%M")
    success = "úspešne" if error == "" else "neúspešne"
    log_name = f"DPO-log_{success}_{timestamp}.txt"

    log(log_name, new_doc_name, error, project_id, missing_data)

    print(f"Program prebehol {success}.")
    if len(error) != 0:
        print(f"{error} \n")

    print(f"Záznam o priebehu programu je uložený v súbore {log_name}")
