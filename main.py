from storage import initialize_storage
from config import EVENT_STATUSES

from event_manager import (
    add_event,
    view_events,
    search_events,
    filter_events_by_status,
    update_event,
    delete_event,
    show_statistics
)

from utils import (
    get_valid_date,
    get_valid_time,
    get_valid_amount,
    get_valid_integer,
    get_valid_id,
    get_event_status
)


def display_menu():
    print("\n========== PERSONAL EVENT PLANNER ==========")
    print("1. Add Event")
    print("2. View All Events")
    print("3. Search Event")
    print("4. Filter Events by Status")
    print("5. Update Event")
    print("6. Delete Event")
    print("7. Event Statistics")
    print("8. Exit")
    print("============================================")


def get_event_details():
    name = input("Enter event name: ").strip()
    category = input("Enter event category: ").strip()
    location = input("Enter event location: ").strip()

    event_date = get_valid_date(
        "Enter event date (YYYY-MM-DD): "
    )

    event_time = get_valid_time(
        "Enter event time (HH:MM): "
    )

    guest_count = get_valid_integer(
        "Enter expected guest count: "
    )

    budget = get_valid_amount(
        "Enter event budget (₹): "
    )

    actual_cost = get_valid_amount(
        "Enter actual expenses (₹): "
    )

    status = get_event_status(EVENT_STATUSES)

    notes = input("Enter additional notes: ").strip()

    if not name or not category or not location:
        print("Event name, category, and location are required.")
        return None

    return (
        name,
        category,
        location,
        event_date,
        event_time,
        guest_count,
        budget,
        actual_cost,
        status,
        notes
    )


def main():
    initialize_storage()

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            details = get_event_details()

            if details:
                add_event(*details)

        elif choice == "2":
            view_events()

        elif choice == "3":
            keyword = input(
                "Enter event name, category, or location: "
            ).strip()

            search_events(keyword)

        elif choice == "4":
            status = get_event_status(EVENT_STATUSES)
            filter_events_by_status(status)

        elif choice == "5":
            event_id = get_valid_id(
                "Enter event ID to update: "
            )

            details = get_event_details()

            if details:
                update_event(event_id, *details)

        elif choice == "6":
            event_id = get_valid_id(
                "Enter event ID to delete: "
            )

            delete_event(event_id)

        elif choice == "7":
            show_statistics()

        elif choice == "8":
            print("Thank you for using Personal Event Planner!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
