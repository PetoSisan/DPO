from typing import OrderedDict, Any

from Person import Person
from Address import Address
from PhysicalPerson import PhysicalPerson
from Corporate import Corporate

from Project import Project
from Facility import Facility
from FacilityPart import FacilityPart

Applicant = Person  # žiadateľ
ProjectOwner = Person # stavebník

Cadastral_territory = str # Katastralne uzemie
Register = str # Register
Parcel = str # Čislo parcely
Code = str # Kód stavebého objektu
Title = str # názov stabeného objektu
Construction_parcels = dict[Cadastral_territory, dict[Register, Parcel]] # Stavebne pozemky

PHYSICAL_PERSON = "FON"
CORPORATE = "PO"


def get_person_type(person: OrderedDict[str, Any]) -> str:
    """ root - Applicant / ProjectOwner
        returns FON / PO
    """ 

    return get_item_code(person.get("PersonType", "") or "")


def get_item_code(root: OrderedDict[str, Any]) -> str:
    return root.get("Codelist", {}).get("CodelistItem", {}).get("ItemCode", "") or ""


def get_item_name(root: OrderedDict[str, Any]) -> str:
    return root.get("Codelist", {}).get("CodelistItem", {}).get("ItemName", {}).get("#text", "") or ""


def get_physical_person_name(physical_person: OrderedDict[str, Any]) -> tuple[str, str]:
    person_name: OrderedDict[str, str] = physical_person.get("PersonName", {})
    return person_name.get("GivenName", "") or "", person_name.get("FamilyName", "") or ""


def get_physical_person_title(physical_person: OrderedDict[str, Any]) -> str:
    return physical_person.get("Affix", {}).get("NonCodelistData", "") or ""


def create_address(physical_address: OrderedDict[str, Any]) -> Address:
    street_name = physical_address.get("StreetName", "") or "" 

    number = physical_address.get("PropertyRegistrationNumber") or ""
    building_number = physical_address.get("BuildingNumber", "") or ""
    number += f"/{building_number}"
        
    
    postal_code = physical_address.get("DeliveryAddress", {}).get("PostalCode") or ""

    city = physical_address.get("Municipality", {}).get("NonCodelistData", "") or ""
    if city == "":
        city = get_item_name(physical_address.get("Municipality", {}) or {})
        

    country: str = get_item_name(physical_address.get("Country", {}) or {})
    county: str = get_item_name(physical_address.get("County", {}) or {})

    return Address(street_name, building_number, postal_code, city, county, country)


def get_phone(telephone_address: OrderedDict[str, Any]) -> str:
    return telephone_address.get("Number", {}).get("FormattedNumber", "") or ""


def get_mail(electronic_address: OrderedDict[str, Any]) -> str:
    return electronic_address.get("InternetAddress", "") or ""


def create_physical_person(person_data: OrderedDict[str, Any]) -> PhysicalPerson:
    physical_person = person_data.get("PhysicalPerson", {})
    name, surname = get_physical_person_name(physical_person)
    title = get_physical_person_title(physical_person)

    address: Address = create_address(person_data.get("PhysicalAddress", {}) or {})

    phone = get_phone(person_data.get("TelephoneAddress", {}) or {})
    mail = get_mail(person_data.get("ElectronicAddress", {}) or {})

    return PhysicalPerson(title, name, surname, address, phone, mail)


def get_ICO(ID: OrderedDict[str, Any]) -> int:
    return ID.get("IdentifierValue", "")


def create_corporate(person_data: OrderedDict[str, Any]) -> Corporate:
    corporate_body: OrderedDict[str, Any] = person_data.get("CorporateBody", {})
    name = corporate_body.get("CorporateBodyFullName", "") or ""

    physical_person = corporate_body.get("Stakeholder", {}).get("PersonData", {}).get("PhysicalPerson", {}) or {}

    person_name, person_surname = get_physical_person_name(physical_person)
    title = get_physical_person_title(physical_person)

    address = create_address(person_data.get("PhysicalAddress", {}))

    phone = get_phone(person_data.get("TelephoneAddress", {}) or {})
    mail = get_mail(person_data.get("ElectronicAddress", {}) or {})

    ICO = get_ICO(person_data.get("ID", {}) or {})

    return Corporate(PhysicalPerson(title, person_name, person_surname), name, address, ICO, phone, mail)


def create_person(person: OrderedDict[str, Any], person_type: str) -> Person:
    person_data: OrderedDict[str, Any] = person.get("PersonData", {}) or {}

    if person_type == PHYSICAL_PERSON:
        return create_physical_person(person_data)
    return create_corporate(person_data)


def ensure_list(item):
    if isinstance(item, list):
        return item
    else:
        return [item]


def create_parcels(parcels: OrderedDict[str, Any]) -> Construction_parcels:
    construction_parcels = {}
    parcels = ensure_list(parcels.get("ProjectParcel", {}) or {})

    for parcel in parcels:
        cadastral_territory = get_item_name(parcel.get("CatastralAreaTitle", {}))
        register = get_item_name(parcel.get("ParcelRegister", {}))
        parcel_number = parcel.get("ParcelNumber", "") or ""

        if construction_parcels.get(cadastral_territory) is None:
            construction_parcels[cadastral_territory] = {}

        if construction_parcels[cadastral_territory].get(register) is None:
            construction_parcels[cadastral_territory][register] = [parcel_number]
        else:
            construction_parcels[cadastral_territory][register].append(parcel_number)
    
    return construction_parcels
    

def create_facility(facility: OrderedDict[str, Any]) -> Facility:
    code = facility.get("FacilityCode", "") or ""
    title = facility.get("FacilityTitle", "") or ""
    construction_class = get_item_name(facility.get("ConstructionClassID", {}) or {})

    parts = []
    facility_parts = ensure_list(facility.get("FacilityParts", {}) or {})

    for facility_part in facility_parts:
        facility_part_SOs = facility_part.get("FacilityPartSO")
        if facility_part_SOs is None:
            continue

        facility_part_SOs = ensure_list(facility_part_SOs)
        
        for facility_part_SO in facility_part_SOs:
            parts.append( FacilityPart(facility_part_SO.get("FacilityPartCode", "") or "", facility_part_SO.get("FacilityPartTitle", "") or "") )
    
    return Facility(code, title, construction_class, parts)


def create_project(project: OrderedDict[str, Any]) -> Project:
    id = project.get("ProjectCode", "") or ""
    title = project.get("ProjectTitle", "") or ""
    address = create_address(project.get("ProjectAddress", {}).get("PersonData", {}).get("PhysicalAddress", {}) or {})
    parcels = create_parcels(project.get("ConstructionParcels", {}) or {})

    facilities_in = ensure_list(project.get("Facilities", {}).get("Facility", {}) or {})
    facilites_out = []
    for facility in facilities_in:
        facilites_out.append(create_facility(facility))

    return Project(id, title, address, parcels, facilites_out)


def parse(data: OrderedDict[str, Any]) -> tuple[Applicant, ProjectOwner, Project]:
    application: OrderedDict[str, Any] = data.get("eform", {}).get("Application", {})
    
    applicant_dict: OrderedDict[str, Any] = application.get("Applicants", {}).get("Applicant", {})
    applicant: Person = create_person(applicant_dict, get_person_type(applicant_dict))

    project_owner_dict = application.get("ProjectOwners", {}).get("ProjectOwner", {})
    project_owner: Person = create_person(project_owner_dict, get_person_type(project_owner_dict))

    project_dict: OrderedDict[str, Any] = data.get("eform", {}).get("Project", {})
    project = create_project(project_dict)

    return applicant, project_owner, project