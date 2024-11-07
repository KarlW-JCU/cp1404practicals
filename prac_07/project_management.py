"""
Project Management Program
Estimate: 60 minutes
Actual:   1400
"""

from prac_07.project import Project
import datetime

FILENAME = "projects.txt"
MENU = """
"""


def main():
    """"""
    print("Welcome to Pythonic Project Management")
    filename = FILENAME
    projects = load_projects(filename)
    for project in projects:
        print(project)


def load_projects(filename):
    """Return list of Project objects read from file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # skip header
        for line in in_file:
            parts = line.strip().split("\t")
            name = parts[0]
            date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = float(parts[4])
            new_project = Project(name, date, priority, cost_estimate, completion)
            projects.append(new_project)
    print(f"Loaded {len(projects)} projects from {filename}")
    return projects


main()
