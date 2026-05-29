from typing import OrderedDict, Any

from datetime import datetime

from entities.Person import Person
from entities.Address import Address
from entities.PhysicalPerson import PhysicalPerson
from entities.Corporate import Corporate

from entities.Project import Project
from entities.Facility import Facility
from entities.FacilityPart import FacilityPart

Applicant = Person  # žiadateľ
ProjectOwner = Person # stavebník



def parse(data: OrderedDict[str, Any]) -> tuple[list[Applicant], list[ProjectOwner], Project]:
    """This is just a dummy parser. The actual implementation is hidden. See `README.md` for more info"""
    address = Address("Stromova", "42", "12345", "Kholinar", "Central", "Alethkar")
    applicants = [PhysicalPerson("Ing.", "Jan", "Novak", address, "0912345678", "mail@gmail.com")]
    project_owners = [PhysicalPerson("Ing.", "Jan", "Novak", address, "0912345678", "mail@gmail.com")]

    parcels = {
        "TeritoryA": {"A": "123", "B": "1235"},
        "TeritoryB": {"D": "452", "F": "5555", "H": "2447"}
    }
    facilites = [
        Facility("Code1", "Facility1", "class", [FacilityPart("Code5", "FacilityPart1")]),
        Facility("Code2", "Facility2", "class", [FacilityPart("Code5", "FacilityPart1")])
    ]

    project = Project("ID1524", "D1", address, parcels, facilites)

    return applicants, project_owners, project

def get_project_id(root: OrderedDict[str, Any] | None, project: Project | None) -> str:
    if project is not None:
        return project.id
    
    return "ID stavby nebolo nájdené"


INCOMPLETE_DATA = "Ostatné údaje nie sú dostupné v žiadosti ani v PD."

def prepare_applicants(applicants: list[Person],
                       header_data: dict[str, str],
                       data: dict[str, str]) -> None:
    for applicant in applicants:
        header_data["Meno Priezvisko"] = \
            header_data.get("Meno Priezvisko", "") + f"{applicant.get_full_name()}"
        
        header_data["Ulica číslo"] = \
            header_data.get("Ulica číslo", "") + f"{applicant.address.street} {applicant.address.building_number}"
        
        header_data["PSČ Mesto"] = \
            header_data.get("PSČ Mesto", "") + f"{applicant.address.postal_code} {applicant.address.city} \n"
        
        data["Žiadateľ"] = \
            data.get("Žiadateľ", "") + f"{applicant.to_string()} \n"
        
        if not applicant.is_complete():
             data["Žiadateľ"] += f"\n{INCOMPLETE_DATA}\n"
    return


def prepare_project_owners(project_owners: list[Person],
                           data: dict[str, str]) -> None:
    for project_owner in project_owners:
        data["Stavebník"] = \
            data.get("Stavebník", "") + f"{project_owner.to_string()} \n"
        
        if not project_owner.is_complete():
             data["Stavebník"] += f"\n{INCOMPLETE_DATA}\n"


def prepare_project(project: Project, data: dict[str, str]) -> None:
    data["ID stavby \n(ak bolo pridelené Portálom výstavby)"] = project.id
    data["Názov stavby"] = project.title
    data["Identifikačné údaje stavby"] = project.format_parcels()
    data["Členenie stavby"] = project.format_facilities()
    return


def prepare_data(applicants: list[Person],
                 project_owners: list[Person],
                 project: Project,
                 qna: dict[str, str],
                 date_time: datetime) -> tuple[dict[str, str], dict[str, str]]:
    header_data: dict[str, str] = {}
    data: dict[str, str] = qna

    date = date_time.strftime("%d.%m.%Y")
    header_data["V Bratislave, dňa"] = f"V Bratislave, dňa {date}"
     
    prepare_applicants(applicants, header_data, data)
    prepare_project_owners(project_owners, data)
    prepare_project(project, data)

    return header_data, data

