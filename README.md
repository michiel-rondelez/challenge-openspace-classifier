# OpenSpace Seating Randomizer

A Python program that automatically assigns colleagues to different seats every day in a shared open office. This tool supports dynamic CSV file input, random seat allocation, and exporting seating results to JSON.

---

## The Mission

The company moved into a new open space with 6 tables containing 4 seats each. To encourage team bonding, everyone changes seats daily. This program reassigns all colleagues to new seats at random.

---

## Features

### ✅ Must-have requirements
- Default configuration: 6 tables × 4 seats = 24 seats
- Reads a list of colleagues from a CSV file
- Randomly places each person in a free seat
- Displays number of free seats left
- Handles overflow if more than 24 participants
- User interaction in the terminal
- Start program with:

```bash
python src/main.py
