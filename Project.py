from Address import Address

Cadastral_territory = str
Register = str
Parcel = str
Code = str
Title = str
Construction_object = tuple[Code, Title]
Construction_parcels = dict[Cadastral_territory, dict[Register, Parcel]]

class Project:
    def __init__(self, id: str, title: str, adress: Address,
                 construction_parcels: Construction_parcels,
                 construction_objects: list[Construction_object]):
        self.id = id
        self.title = title
        self.address = adress
        self.construction_parcels = construction_parcels
        self.construction_objects = construction_objects
    

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
    

    def format_objects(self) -> str:
        result = ""
        header_1 = "Kód stavebného objektu"
        header_2 = "Názov stavebného objektu"
        len_1 = len(header_1) + 5
        len_2 = len(header_2) + 5

        for code, title in self.construction_objects:
            result += f"{code:<{len_1}} | {title:<{len_2}} \n"

        return result




