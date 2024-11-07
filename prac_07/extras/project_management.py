"""Project Management Program"""

import datetime
from operator import attrgetter
from prac_07.project import Project

FILENAME = "projects.txt"
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""


def main():
    """Load, View, Update, and Save project list using pickling."""
    print("Welcome to Pythonic Project Management")
    filename = FILENAME
    projects = load_projects(filename)
    print(MENU)
    selection = input(">>> ").upper()
    while selection != "Q":
        if selection == "L":
            filename, projects = change_file(filename, projects)
        elif selection == "S":
            confirm_save = input(f"Would you like to save to {filename}? ").upper()
            save_projects(confirm_save, filename, projects)
        elif selection == "D":
            display_projects(projects)
        elif selection == "F":
            filter_by_date(projects)
        elif selection == "A":
            add_project(projects)
        elif selection == "U":
            update_project(projects)
        else:
            print("Invalid selection.")
        print(MENU)
        selection = input(">>> ").upper()
    confirm_save = input(f"Would you like to save to {filename}? ").upper()
    save_projects(confirm_save, filename, projects)
    print("Thank you for using custom-built project management software.")


def update_project(projects):
    """Update project completion percentage and priority."""
    for i, project in enumerate(projects):
        print(i, project)
    try:
        choice = int(input("Project Choice: "))
        print(projects[choice])
        try:
            new_percentage = int(input("New Percentage: "))
            new_priority = int(input("New Priority: "))
            projects[choice].completion_percentage = new_percentage
            projects[choice].priority = new_priority
        except ValueError:
            print("Invalid input.")
    except ValueError:
        print("Invalid choice.")


def load_projects(filename):
    """Return list of Project objects read from file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date().strftime("%d/%m/%Y")
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = float(parts[4])
            new_project = Project(name, date, priority, cost_estimate, completion)
            projects.append(new_project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


def change_file(filename, projects):
    """Set active filename from user input."""
    try:
        filename = input("Projects File: ")
        projects = load_projects(filename)
    except FileNotFoundError:
        print(f"Invalid filename: {filename}\n"
              f"Reverting to default: {FILENAME}")
        filename = FILENAME
    return filename, projects


def save_projects(confirm_save, filename, projects):
    """Write list of Project objects to file."""
    if confirm_save == "Y" or confirm_save == "YES":
        with open(filename, "w") as out_file:
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
            for project in projects:
                print(
                    f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                    file=out_file)


def display_projects(projects):
    """Print projects sorted by priority and completion."""
    print("Incomplete projects: ")
    for project in sorted(projects):
        if project.completion_percentage != 100.0:
            print(project)
    print("Completed projects: ")
    for project in sorted(projects):
        if project.completion_percentage == 100.0:
            print(project)


def filter_by_date(projects):
    """Print projects sorted by date, occurring after user defined date."""
    date = get_valid_date("Show projects that start after date")
    for project in sorted(projects, key=attrgetter("start_date")):
        if project.start_date >= date:
            print(project)


def add_project(projects):
    """Add new project to projects."""
    print("Let's add a new project!")
    try:
        name = input("Name: ")
        date = get_valid_date("Start date")
        priority = int(input("Priority: "))
        cost = float(input("Estimated Cost: "))
        completion = float(input("Percent Complete: "))
        new_project = Project(name, date, priority, cost, completion)
        projects.append(new_project)
    except ValueError:
        print("Invalid input, please try again.")


def get_valid_date(prompt):
    """Get date from user input matching format dd/mm/yyyy."""
    while True:
        try:
            date = input(f"{prompt} (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date, "%d/%m/%Y").date().strftime("%d/%m/%Y")
            return date
        except ValueError:
            print("Invalid date.")


main()
