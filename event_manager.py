from storage import load_events, save_events


def add_event(name, category, location, event_date, event_time,
              guest_count, budget, actual_cost, status, notes):

    events = load_events()

    event_id = max(
        [event["id"] for event in events],
        default=0
    ) + 1

    event = {
        "id": event_id,
        "name": name,
        "category": category,
        "location": location,
        "event_date": event_date,
        "event_time": event_time,
        "guest_count": guest_count,
        "budget": budget,
        "actual_cost": actual_cost,
        "status": status,
        "notes": notes
    }

    events.append(event)
    save_events(events)

    print("\nEvent added successfully!")
    print(f"Event ID: {event_id}")


def view_events():
    events = load_events()

    if not events:
        print("\nNo events found.")
        return

    print("\n" + "-" * 115)
    print(
        f"{'ID':<5} {'Event Name':<22} {'Date':<13} "
        f"{'Time':<9} {'Guests':<9} {'Budget':<14} {'Status':<13}"
    )
    print("-" * 115)

    for event in events:
        print(
            f"{event['id']:<5} "
            f"{event['name'][:21]:<22} "
            f"{event['event_date']:<13} "
            f"{event['event_time']:<9} "
            f"{event['guest_count']:<9} "
            f"₹{event['budget']:<13.2f} "
            f"{event['status']:<13}"
        )

    print("-" * 115)


def display_event_details(events):
    if not events:
        print("\nNo matching events found.")
        return

    for event in events:
        print("\n" + "=" * 45)
        print(f"Event ID: {event['id']}")
        print(f"Event Name: {event['name']}")
        print(f"Category: {event['category']}")
        print(f"Location: {event['location']}")
        print(f"Date: {event['event_date']}")
        print(f"Time: {event['event_time']}")
        print(f"Guest Count: {event['guest_count']}")
        print(f"Budget: ₹{event['budget']:.2f}")
        print(f"Actual Cost: ₹{event['actual_cost']:.2f}")
        print(f"Status: {event['status']}")
        print(f"Notes: {event['notes'] or 'N/A'}")
        print("=" * 45)


def search_events(keyword):
    events = load_events()
    keyword = keyword.lower()

    results = [
        event for event in events
        if keyword in event["name"].lower()
        or keyword in event["location"].lower()
        or keyword in event["category"].lower()
    ]

    display_event_details(results)


def filter_events_by_status(status):
    events = load_events()

    results = [
        event for event in events
        if event["status"] == status
    ]

    display_event_details(results)


def update_event(event_id, name, category, location, event_date,
                 event_time, guest_count, budget, actual_cost,
                 status, notes):

    events = load_events()

    for event in events:
        if event["id"] == event_id:
            event["name"] = name
            event["category"] = category
            event["location"] = location
            event["event_date"] = event_date
            event["event_time"] = event_time
            event["guest_count"] = guest_count
            event["budget"] = budget
            event["actual_cost"] = actual_cost
            event["status"] = status
            event["notes"] = notes

            save_events(events)
            print("\nEvent updated successfully!")
            return

    print("\nEvent ID not found.")


def delete_event(event_id):
    events = load_events()

    updated_events = [
        event for event in events
        if event["id"] != event_id
    ]

    if len(updated_events) == len(events):
        print("\nEvent ID not found.")
        return

    save_events(updated_events)
    print("\nEvent deleted successfully!")


def show_statistics():
    events = load_events()

    if not events:
        print("\nNo event statistics available.")
        return

    total_events = len(events)

    planned = sum(
        1 for event in events
        if event["status"] == "Planned"
    )

    ongoing = sum(
        1 for event in events
        if event["status"] == "Ongoing"
    )

    completed = sum(
        1 for event in events
        if event["status"] == "Completed"
    )

    cancelled = sum(
        1 for event in events
        if event["status"] == "Cancelled"
    )

    total_guests = sum(
        event["guest_count"] for event in events
    )

    total_budget = sum(
        event["budget"] for event in events
    )

    total_expenses = sum(
        event["actual_cost"] for event in events
    )

    difference = total_budget - total_expenses

    print("\n========== EVENT STATISTICS ==========")
    print(f"Total Events: {total_events}")
    print(f"Planned Events: {planned}")
    print(f"Ongoing Events: {ongoing}")
    print(f"Completed Events: {completed}")
    print(f"Cancelled Events: {cancelled}")
    print(f"Total Guests: {total_guests}")
    print(f"Total Budget: ₹{total_budget:.2f}")
    print(f"Total Expenses: ₹{total_expenses:.2f}")
    print(f"Budget Remaining: ₹{difference:.2f}")
    print("======================================")
