# project_management.py

"""
Project Management Script
Time Estimate: ~5 hours
"""

from project import Project
import datetime


def main():
    FILENAME = "projects.txt"
    projects = load_projects(FILENAME)  # Load initial projects from file
    if not projects:
        print(f"No projects loaded from {FILENAME}.")
    else:
        print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {FILENAME}")

    running = True
    while running:
        display_menu()  # Show menu options
        choice = input(">>> ").lower()  # Get user choice
        if choice == 'l':
            filename = input("Filename: ")
            projects = load_projects(filename)  # Load projects from specified file
        elif choice == 's':
            filename = input("Filename: ")
            save_projects(filename, projects)  # Save projects to specified file
        elif choice == 'd':
            display_projects(projects)  # Display current projects
        elif choice == 'f':
            date_str = input("Show projects that start after date (dd/mm/yyyy): ")
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()  # Parse date
            filter_projects_by_date(projects, date)  # Filter projects by date
        elif choice == 'a':
            projects.append(add_new_project())  # Add new project
        elif choice == 'u':
            update_project(projects)  # Update existing project
        elif choice == 'q':
            save = input(f"Would you like to save to {FILENAME}? ").lower()
            if save == 'yes':
                save_projects(FILENAME, projects)  # Save projects before quitting
            print("Thank you for using custom-built project management software.")
            running = False  # Exit loop
        else:
            print("Invalid choice, please try again.")  # Handle invalid input


def display_menu():
    """Display menu options for the user."""
    print("\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- "
          "(A)dd new project\n- (U)pdate project\n- (Q)uit")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()  # Skip header line
            for line in file:
                # Read project details and create Project objects
                name, start_date, priority, cost_estimate, completion = line.strip().split('\t')
                projects.append(Project(name, start_date, priority, cost_estimate, completion))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")  # Handle file not found error
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")  # Write header
        for project in projects:
            # Write each project to the file
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion}\n")


def display_projects(projects):
    """Display all projects, separated into incomplete and completed."""
    incomplete_projects = [p for p in projects if p.completion < 100]
    completed_projects = [p for p in projects if p.completion == 100]
    incomplete_projects.sort()  # Sort by default, using Project's __lt__ method
    completed_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    """Filter and display projects that start after a given date."""
    def sort_by_start_date(project):
        return project.start_date

    filtered_projects = [p for p in projects if p.start_date >= date]  # Filter projects by start date
    filtered_projects.sort(key=sort_by_start_date)  # Sort filtered projects by start date
    for project in filtered_projects:
        print(project)


def add_new_project():
    """Add a new project by getting details from the user."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = get_valid_int("Priority: ", min_value=1)
    cost_estimate = float(input("Cost estimate: $"))
    completion = get_valid_int("Percent complete: ", min_value=0, max_value=100)
    return Project(name, start_date, priority, cost_estimate, completion)  # Create and return new Project object


def get_valid_int(prompt, min_value=None, max_value=None):
    """Get a valid integer from the user, with optional bounds."""
    valid = False
    while not valid:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                raise ValueError
            valid = True
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid integer{f' between {min_value} and {max_value}' if min_value is not None and max_value is not None else ''}.")


def update_project(projects):
    """Update an existing project."""
    for i in range(len(projects)):
        print(f"{i} {projects[i]}")  # Display all projects with indices

    index = get_valid_int("Project choice: ", min_value=0, max_value=len(projects) - 1)  # Get project index from user
    project = projects[index]
    print(f"{project}")  # Print the selected project

    new_completion = input(f"New Percentage: ")
    if new_completion:
        project.completion = int(new_completion)  # Update completion percentage

    new_priority = input(f"New Priority: ")
    if new_priority.strip():  # Only update priority if the input is not empty
        project.priority = int(new_priority)  # Update priority


if __name__ == "__main__":
    main()  # Run the main function when the script is executed
