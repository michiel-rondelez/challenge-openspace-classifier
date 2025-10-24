from utils.openspace import OpenSpace
from utils.file_utils import get_names_from_csv

def main():
    file_path = input("Enter CSV file name: ").strip()
    names = get_names_from_csv(file_path)
    open_space = OpenSpace(max_number_of_tables=6)
    print(names)
    open_space.organize(names)
    print(open_space.display())
    open_space.store("organized_seating.json")

if __name__ == "__main__":
    main()
