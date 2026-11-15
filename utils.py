from datetime import datetime


def get_valid_date(prompt):
    while True:
        value = input(prompt).strip()

        try:
            parsed_date = datetime.strptime(value, "%Y-%m-%d")
            return parsed_date.strftime("%Y-%m-%d")

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD format.")


def get_valid_time(prompt):
    while True:
        value = input(prompt).strip()

        try:
            parsed_time = datetime.strptime(value, "%H:%M")
            return parsed_time.strftime("%H:%M")

        except ValueError:
            print("Invalid time. Use 24-hour format HH:MM.")


def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Please enter a valid amount.")


def get_valid_integer(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))

            if value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue

            return value

        except ValueError:
            print("Please enter a valid whole number.")


def get_valid_id(prompt):
    return get_valid_integer(prompt, minimum=1)


def get_event_status(statuses):
    print("\nEvent Status:")

    for index, status in enumerate(statuses, start=1):
        print(f"{index}. {status}")

    while True:
        try:
            choice = int(input("Select status: "))

            if 1 <= choice <= len(statuses):
                return statuses[choice - 1]

            print("Invalid status choice.")

        except ValueError:
            print("Please enter a valid number.")
