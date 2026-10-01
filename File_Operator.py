from datetime import datetime

file_name = "journal.txt"


def add_entry():
    print("\n--- Add a New Entry ---")

    entry = input("\nEnter your journal entry:\n")

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file = open(file_name, "a")

    file.write("[" + date + "]\n")
    file.write(entry + "\n")

    file.close()

    print("\nEntry added successfully!")


def view_entries():
    print("\n--- View All Entries ---")

    try:
        file = open(file_name, "r")

        data = file.read()

        if data == "":
            print("No journal entries found. Start by adding a new entry!")

        else:
            print("\nYour Journal Entries:")
            print("--------------------------------")
            print(data)

        file.close()

    except FileNotFoundError:
        print("Error: The journal file does not exist. Please add a new entry first.")


def search_entry():
    print("\n--- Search for an Entry ---")

    keyword = input("\nEnter a keyword or date to search: ")

    try:
        file = open(file_name, "r")

        data = file.read()

        if keyword.lower() in data.lower():
            print("\nMatching Entries:")
            print("--------------------------------")
            print(data)

        else:
            print("\nNo entries were found for the keyword:", keyword)

        file.close()

    except FileNotFoundError:
        print("Error: The journal file does not exist. Please add a new entry first.")


def delete_entries():
    print("\n--- Delete All Entries ---")

    try:
        file = open(file_name, "r")

        data = file.read()

        file.close()

        if data == "":
            print("No journal entries to delete.")
            return

        choice = input(
            "\nAre you sure you want to delete all entries? (yes/no): "
        )

        if choice.lower() == "yes":

            file = open(file_name, "w")
            file.close()

            print("\nAll journal entries have been deleted.")

        else:
            print("\nDelete operation cancelled.")

    except FileNotFoundError:
        print("No journal entries to delete.")


print("Welcome to Personal Journal Manager!")
print("Please select an option:")

while True:

    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_entry()

    elif choice == "2":
        view_entries()

    elif choice == "3":
        search_entry()

    elif choice == "4":
        delete_entries()

    elif choice == "5":
        print("\nThank you for using Personal Journal Manager. Goodbye!")
        break

    else:
        print("\nInvalid option. Please select a valid option from the menu.")