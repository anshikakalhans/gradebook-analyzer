# ----------------------------------------------------------
# Name: Anshika Kalhans
# Date: 22-11-2025
# Project: GradeBook Analyzer - Mini Assignment
# ----------------------------------------------------------

import csv
import os

# ----------------------------------------------------------
# TASK 3: Statistical Functions
# ----------------------------------------------------------

def calculate_average(marks):
    return sum(marks.values()) / len(marks)

def calculate_median(marks):
    arr = sorted(marks.values())
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2

def find_max_score(marks):
    return max(marks.values())

def find_min_score(marks):
    return min(marks.values())


# ----------------------------------------------------------
# TASK 4: Grade Assignment Function
# ----------------------------------------------------------

def assign_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "F"


# ----------------------------------------------------------
# TASK 2: Input Methods
# ----------------------------------------------------------

def manual_input():
    marks = {}
    n = int(input("Enter number of students: "))
    
    for _ in range(n):
        name = input("Student Name: ")
        score = int(input("Marks: "))
        marks[name] = score
    
    return marks


def import_csv():
    marks = {}
    file_name = input("Enter CSV file name (with .csv): ").strip()

    # FIX: show working dir
    print(f"Searching in: {os.getcwd()}")

    try:
        # FIX: Remove BOM automatically for VS Code CSV
        with open(file_name, "r", encoding="utf-8-sig") as file:
            reader = csv.reader(file)
            next(reader)  # skip header row

            for row in reader:
                if len(row) < 2:
                    continue
                name = row[0].strip()
                score = int(row[1].strip())
                marks[name] = score

        print("CSV file loaded successfully!")

    except FileNotFoundError:
        print("FILE NOT FOUND! Try using full path.")
    except ValueError:
        print("CSV contains invalid numbers.")
    except Exception as e:
        print("Error loading CSV:", e)

    return marks


# ----------------------------------------------------------
# TASK 6: Display Table
# ----------------------------------------------------------

def display_results(marks, grades):
    print("\n-------------------------------------")
    print("Name\t\tMarks\tGrade")
    print("-------------------------------------")

    for name in marks:
        print(f"{name:10}\t{marks[name]:3}\t{grades[name]}")

    print("-------------------------------------")


# ----------------------------------------------------------
# WELCOME MESSAGE
# ----------------------------------------------------------

def welcome_message():
    print("\n==============================")
    print("   WELCOME TO GRADEBOOK ANALYZER")
    print("==============================\n")


# ----------------------------------------------------------
# MAIN PROGRAM LOOP
# ----------------------------------------------------------

welcome_message()  # Show welcome message at start

while True:

    print("\nChoose Input Method:")
    print("1. Manual Entry")
    print("2. Import from CSV")
    print("3. Exit")

    option = input("Enter option: ")

    if option == "1":
        marks = manual_input()

    elif option == "2":
        marks = import_csv()

    elif option == "3":
        print("Exiting program…")
        break

    else:
        print("Invalid choice!")
        continue

    if not marks:
        print("No data to analyze. Try again.")
        continue

    # ---------- Compute Grades ----------
    grades = {name: assign_grade(score) for name, score in marks.items()}

    # ---------- Grade Distribution ----------
    distribution = {"A":0, "B":0, "C":0, "D":0, "F":0}
    for g in grades.values():
        distribution[g] += 1

    # ---------- Pass/Fail ----------
    passed = [name for name, m in marks.items() if m >= 40]
    failed = [name for name, m in marks.items() if m < 40]

    # ---------- Statistics ----------
    avg = calculate_average(marks)
    median = calculate_median(marks)
    max_score = find_max_score(marks)
    min_score = find_min_score(marks)

    # ---------- Output ----------
    print("\n==== ANALYSIS SUMMARY ====")
    print(f"Average Marks : {avg:.2f}")
    print(f"Median Marks  : {median}")
    print(f"Highest Score : {max_score}")
    print(f"Lowest Score  : {min_score}")

    print("\nGrade Distribution:", distribution)
    print("\nPassed Students:", passed)
    print("Failed Students:", failed)

    display_results(marks, grades)

    # ---------- Loop again ----------
    choice = input("\nDo you want to analyze again? (y/n): ").strip().lower()
    if choice not in ("y", "yes"):
        print("\nThank you for using GradeBook Analyzer!")
        break
