import json
import pickle
import calendar
import datetime
from datetime import date

class Calendar:

        def init(self):  
                self.notes = {}
        def save(self):
                with open("calendar.pickle", "wb") as f:
                        pickle.dump(self.notes, f)

        def load(self):
                try:
                   with open("calendar.pickle", "rb") as f:
                        self.notes = pickle.load(f)
                except FileNotFoundError:
                        self.notes = {}

        def add_note(self, date, note):
                if date not in self.notes:
                        self.notes[date] = []
                self.notes[date].append(note)

        def show_month(self, year, month):
                for date, note in self.notes.items():
                        if date.year == year and date.month == month:
                                print(f"{date.day}: {', '.join(note)}")

        def show_day(self, year, month, day):
                date = datetime.date(year, month, day)
                if date in self.notes:
                        print(f"{date.day}: {', '.join(self.notes[date])}")
                else:
                        print(f"No notes for {date}")
                print(" ")


            
def print_menu():
    print("Choose an option")
    print("1. Show month")
    print("2. Show day")
    print("3. Add note")
#     print("4. Save")
#     print("5. Load")
    print("4. Quit")

def get_choice():
    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 6:
            print("Invalid choice.")
            return get_choice()
        return choice
    except ValueError:
        print("Invalid choice.")
        return get_choice()

def show_month_choice():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print(" ")
    calendar.show_month(year, month)
    print(" ")

def show_day_choice():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    print(" ")
    calendar.show_day(year, month, day)
    print(" ")

def add_note_choice():
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    day = int(input("Enter day: "))
    note = input("Enter note: ")
    print(" ")
    calendar.add_note(date(year, month, day), note)
    print(" ")

calendar = Calendar()
calendar.load()

while True:
    print_menu()
    choice = get_choice()
    if choice == 1:
        show_month_choice()
    elif choice == 2:
        show_day_choice()
    elif choice == 3:
        add_note_choice()
    elif choice == 4:
        calendar.save()
    elif choice == 5:
        calendar.load()
    else:
        break