from typing import Optional

class Seat:
    """
    Class for seat
    """
    def __init__(self) -> None:
        self.__free: bool = True
        self.__occupant: Optional[str] = None
    
    def set_occupant(self, name) -> bool:
        if self.__free:
            self.__occupant = name
            self.__free = False
            return True
        else:
            return False
    def get_occupant(self) -> str:
        return self.__occupant
    def remove_occupant(self) -> bool:
        if not self.__free:
            self.__occupant = None
            self.__free = True
            return True
        else:
            self.__free = False
            return False
    def display_occupant(self):
        result = f"Seat from: {self.__occupant}"
        return result
    def to_dict(self):
        return {
            "free": self.__free,
            "occupant": self.__occupant
        }
    def __str__(self) -> str:
        if self.__free:
            return "Seat: free"
        return f"Seat: occupied by {self.__occupant}"


class Table:
    """
    Class for table
    """
    def __init__(self, capacity=4):
        self.__capacity = capacity
        self.__seats = []
    def has_free_spot(self) -> bool:
        if self.left_capacity() > 0:
            return True
        else:
            return False
    def assign_seat(self, seat:Seat) -> bool:
        if self.has_free_spot():
            self.__seats.append(seat)
            return True
        else:
            return False
    def left_capacity(self) -> int:
        return self.__capacity - len(self.__seats)
    def get_seats(self) -> []:
        return self.__seats
    def to_dict(self):
        return {
            "capacity": self.__capacity,
            "seats": [seat.to_dict() for seat in self.__seats]
        }
    
    def __str__(self) -> str:
        if not self.__seats:
            return f"Table with capacity {self.__capacity}, no occupied seats"

        seat_info = ", ".join(str(seat) for seat in self.__seats)
        occupied_count = len(self.__seats)

        return (
            f"Table with capacity {self.__capacity}, "
            f"{occupied_count} occupied seat(s): {seat_info}"
        )


