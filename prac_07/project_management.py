"""
Project Management Program
Estimate: 60 minutes
Actual:   1400
"""

from prac_07.project import Project
import datetime

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
    """"""
    print("Welcome to Pythonic Project Management")
    filename = FILENAME
    projects = load_projects(filename)
    print(MENU)
    selection = input(">>> ").upper()
    while selection != "Q":
        for project in projects:
            print(project)
        selection = input(">>> ").upper()
    confirm_save = input(f"Would you like to save to {filename}? ").upper()
    save_projects(confirm_save, filename, projects)


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


def save_projects(confirm_save, filename, projects):
    """Write list of Project objects to file."""
    if confirm_save == "Y" or confirm_save == "YES":
        with open(filename, "w") as out_file:
            print("Name Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
            for project in projects:
                print(
                    f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}",
                    file=out_file)


main()
