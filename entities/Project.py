from entities.Address import Address
from entities.Facility import Facility

Cadastral_territory = str
Register = str
Parcel = str
Code = str
Title = str

Construction_parcels = dict[Cadastral_territory, dict[Register, Parcel]]

class Project:
    def __init__(self, id: str, title: str, adress: Address,
                 construction_parcels: Construction_parcels,
                 facilities: list[Facility]):
        self.id = id
        self.title = title
        self.address = adress
        self.construction_parcels = construction_parcels
        self.facilities = facilities
    

    def format_parcels(self) -> str:
        result = ""

        for area, parcels in self.construction_parcels.items():
            result += f"Katastrálne územie: {area}\n"

            for register, parcel_nums in parcels.items():
                result += f"    Register: {register}, Čísla parciel: \n"
                for i, parcel_num in enumerate(parcel_nums):
                    prefix = ""
                    suffix = ", "
                    
                    if i == 0:
                        prefix = "          "
                    
                    if i == len(parcel_nums) - 1:
                        suffix = "\n"

                    result += f"{prefix}{parcel_num}{suffix}"

        return result
    

    def format_facilities(self) -> str:
        result = ""
        for facility in self.facilities:
            result += facility.format()
            result += "\n"
        
        return result