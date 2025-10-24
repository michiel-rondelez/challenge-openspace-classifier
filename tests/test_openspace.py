import os
import json
import tempfile
import csv
import pytest
import sys

# Add src/ to path so Python can find utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from utils.table import Seat, Table
from utils.openspace import OpenSpace
from utils.file_utils import get_names_from_csv


# ------------------ Seat tests ------------------ #

def test_set_and_remove_occupant():
    seat = Seat()
    assert seat.set_occupant("Alice") is True
    assert seat.get_occupant() == "Alice"
    assert seat.set_occupant("Bob") is False  # already occupied
    assert seat.remove_occupant() is True
    assert seat.get_occupant() is None
    assert seat.remove_occupant() is False  # already free

def test_str_and_display():
    seat = Seat()
    assert str(seat) == "Seat: free"
    seat.set_occupant("Alice")
    assert str(seat) == "Seat: occupied by Alice"
    assert seat.display_occupant() == "Seat from: Alice"

# ------------------ Table tests ------------------ #

def test_assign_seat_and_capacity():
    table = Table(capacity=2)
    bobSeat = Seat()
    charlieSeat = Seat()
    aliceSeat = Seat()

    bobSeat.set_occupant("Bob")
    charlieSeat.set_occupant("Charlie")
    aliceSeat.set_occupant("Alice")

    assert table.assign_seat(aliceSeat) is True
    assert table.assign_seat(bobSeat) is True
    assert table.assign_seat(charlieSeat) is False  # table full
    assert table.left_capacity() == 0
    assert len(table.get_seats()) == 2

def test_to_dict_and_str():
    table = Table(capacity=2)
    seat = Seat()
    seat.set_occupant("Alice")
    table.assign_seat(seat)
    table_dict = table.to_dict()
    assert table_dict["capacity"] == 2
    assert table_dict["seats"][0]["occupant"] == "Alice"
    assert "Seat: occupied by Alice" in str(table)

# ------------------ OpenSpace tests ------------------ #

def test_organize_and_display():
    names = ["Alice", "Bob", "Charlie", "David"]
    open_space = OpenSpace(max_number_of_tables=2)
    open_space.organize(names)
    tables = open_space.to_dict()["tables"]
    assert len(tables) == 2
    total_assigned = sum(len(table["seats"]) for table in tables)
    assert total_assigned == len(names)
    display_text = open_space.display()
    assert "Table" in display_text
    assert any(name in display_text for name in names)

def test_store_and_json():
    names = ["Alice", "Bob"]
    open_space = OpenSpace(max_number_of_tables=1)
    open_space.organize(names)
    filename = "test_seating.json"
    open_space.store(filename)
    assert os.path.isfile(filename)
    with open(filename) as f:
        data = json.load(f)
    assert len(data["tables"]) == 1
    os.remove(filename)  # cleanup

# ------------------ CSV tests ------------------ #

def test_get_names_from_csv():
    # Create a temporary CSV file
    with tempfile.NamedTemporaryFile(mode='w+', newline='', delete=False) as temp_file:
        writer = csv.writer(temp_file)
        writer.writerow(["Alice"])
        writer.writerow(["Bob"])
        temp_file_path = temp_file.name

    names = get_names_from_csv(os.path.basename(temp_file_path))
    assert isinstance(names, list)
    # Clean up
    os.remove(temp_file_path)
