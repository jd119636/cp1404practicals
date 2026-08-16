from prac_07.project import Project

FILE_NAME = "projects.txt"
import datetime
projects = []

def main():
    load_file(FILE_NAME)
    print("Welcome to Pythonic Project Management")
    print_menu()
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            new_file_name = input("Filename: ")
            load_file(new_file_name)
        elif choice == "S":
            save_file_name = input("File to save to: ")
            save_file(save_file_name)
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_by_date()
        elif choice == "A":
            add_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid option")
        choice = input(">>>").upper()
    print("Finished")


def load_file(name):
    with open(name, "r") as file:
        file.readline()  # skip header
        count = 0
        for line in file:
            parts = line.strip().split("\t")
            project_name, date_string, priority, cost_estimate, completion = parts
            start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            projects.append(Project(project_name, start_date, int(priority), float(cost_estimate), int(completion)))
            count += 1
        print(f"Loaded {count} projects from {name}")


def save_file(name):
    with open(name, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            date_string = project.start_date.strftime("%d/%m/%Y")
            file.write(f"{project.name}\t{date_string}\t{project.priority}\t{project.cost_estimate}\t{project.completion}\n")
    print(f"Saved {len(projects)} projects to {name}")


def add_project():
    name = input("Name: ")
    date_string = input("Start date (DD/MM/YYYY): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion = int(input("Completion %: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))
    print(f"{name} added.")


def display_projects():
    incomplete = sorted((p for p in projects if not p.is_complete()))
    complete = sorted((p for p in projects if p.is_complete()))

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def get_start_date(project):
    return project.start_date


def filter_by_date():
    date_string = input("Show projects starting after (YYYY-MM-DD): ")
    cutoff = datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

    matches = sorted((p for p in projects if p.start_date > cutoff), key=get_start_date)
    for project in matches:
        print(project)



def update_project():
    for i, project in enumerate(projects, 1):
        print(f"{i}: {project}")
    index = int(input("Choose a project: ")) - 1
    project = projects[index]

    new_completion = input("New completion % (leave blank to keep current): ")
    if new_completion != "":
        project.completion = int(new_completion)

    new_priority = input("New priority (leave blank to keep current): ")
    if new_priority != "":
        project.priority = int(new_priority)

    print(f"Updated: {project}")


def print_menu():
    print(
        " - (L)oad projects\n - (S)ave projects\n - (D)isplay projects\n - (F)ilter projects by date\n - (A)dd new project\n - (U)pdate project\n - (Q)uit")


main()