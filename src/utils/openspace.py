from .table import Table, Seat
import random
import json

class OpenSpace:
    """
    Class for open space
    """
    def __init__(self, max_number_of_tables=6) -> None:
        self.__tables = []
        self.__max_number_of_tables = max_number_of_tables
          
    def organize(self, names):
        random.shuffle(names)
        for table in range(1, self.__max_number_of_tables + 1):
            self.__tables.append(Table())
        for name in names:
            assigned = False
            for table in self.__tables:
                if table.has_free_spot() and not assigned:
                    seat = Seat()
                    seat.set_occupant(name)
                    table.assign_seat(seat)
                    assigned = True
    
    def display(self) -> str:
        text = ""

        for table in self.__tables:
            text += f"{table}\n"       
        return text
    
    def to_dict(self) -> dict:
        return {
            "max_number_of_tables" : self.__max_number_of_tables,
            "tables": [table.to_dict() for table in self.__tables]
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=4)

    def store(self, filename):
        if not filename:
            raise ValueError("Invalid input")
        with open(filename, 'w') as file:
            file.write(self.to_json())
