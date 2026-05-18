import sys

sys.stdout.reconfigure(encoding="utf-8")


def print_passenger_report(passenger_list, title):
    """Print a formatted passenger table so list changes are easy to compare."""
    print(f"\n{title}")
    print("=" * 86)
    print(f"{'Pos':<5}{'PNR':<14}{'Passenger Name':<22}{'Seat Class':<14}{'Seat No':<10}{'Ticket Price':>12}")
    print("-" * 86)

    if not passenger_list:
        print(f"{'-':<5}{'-':<14}{'No passengers':<22}{'-':<14}{'-':<10}{'-':>12}")
    else:
        for position, passenger in enumerate(passenger_list):
            print(
                f"{position:<5}"
                f"{passenger['pnr_number']:<14}"
                f"{passenger['passenger_name']:<22}"
                f"{passenger['seat_class']:<14}"
                f"{passenger['seat_number']:<10}"
                f"₹{passenger['ticket_price']:>10}"
            )

    print("=" * 86)


def demonstrate_lists():
    """Demonstrate 8 Python list methods using a railway reservation scenario."""

    # Initial confirmed bookings in the railway reservation list.
    passenger_bookings = [
        {
            "pnr_number": "PNR1001",
            "passenger_name": "Amit Verma",
            "seat_class": "Sleeper",
            "seat_number": "S1-21",
            "ticket_price": 480,
        },
        {
            "pnr_number": "PNR1002",
            "passenger_name": "Neha Singh",
            "seat_class": "3AC",
            "seat_number": "B2-11",
            "ticket_price": 1320,
        },
        {
            "pnr_number": "PNR1003",
            "passenger_name": "Ravi Kumar",
            "seat_class": "Sleeper",
            "seat_number": "S3-46",
            "ticket_price": 510,
        },
        {
            "pnr_number": "PNR1004",
            "passenger_name": "Isha Patel",
            "seat_class": "2AC",
            "seat_number": "A1-08",
            "ticket_price": 1890,
        },
    ]

    print_passenger_report(passenger_bookings, "INITIAL BOOKED PASSENGERS")

    # 1) append(): Add a new passenger booking at the end because new bookings enter after existing records.
    new_passenger_booking = {
        "pnr_number": "PNR1005",
        "passenger_name": "Farhan Ali",
        "seat_class": "Sleeper",
        "seat_number": "S4-09",
        "ticket_price": 450,
    }
    print_passenger_report(passenger_bookings, "BEFORE append() - NEW BOOKING ENTRY")
    passenger_bookings.append(new_passenger_booking)
    print_passenger_report(passenger_bookings, "AFTER append() - NEW BOOKING ADDED")

    # 2) insert(): Put a VIP passenger at position 0 so staff can process this high-priority booking first.
    vip_passenger_booking = {
        "pnr_number": "PNR1006",
        "passenger_name": "Dr. Meera Roy",
        "seat_class": "1AC",
        "seat_number": "H1-01",
        "ticket_price": 2550,
    }
    print_passenger_report(passenger_bookings, "BEFORE insert() - VIP PRIORITY ENTRY")
    passenger_bookings.insert(0, vip_passenger_booking)
    print_passenger_report(passenger_bookings, "AFTER insert() - VIP ADDED AT POSITION 0")

    # 3) remove(): Remove a passenger by name when that passenger cancels the reservation.
    cancelled_passenger_name = "Ravi Kumar"
    cancelled_booking = next(
        (
            booking
            for booking in passenger_bookings
            if booking["passenger_name"] == cancelled_passenger_name
        ),
        None,
    )
    print_passenger_report(passenger_bookings, "BEFORE remove() - CANCELLATION PROCESS")
    if cancelled_booking:
        passenger_bookings.remove(cancelled_booking)
        print(f"Cancelled booking removed for passenger: {cancelled_passenger_name}")
    else:
        print(f"No booking found for cancellation: {cancelled_passenger_name}")
    print_passenger_report(passenger_bookings, "AFTER remove() - CANCELLATION UPDATED")

    # 4) pop(): Drop the last passenger record when the final waitlist passenger is removed.
    print_passenger_report(passenger_bookings, "BEFORE pop() - WAITLIST DROP CHECK")
    dropped_waitlist_passenger = passenger_bookings.pop()
    print(
        f"Waitlist dropped passenger: {dropped_waitlist_passenger['passenger_name']} "
        f"({dropped_waitlist_passenger['pnr_number']})"
    )
    print_passenger_report(passenger_bookings, "AFTER pop() - LAST PASSENGER REMOVED")

    # 5) index(): Find the seat position for a passenger so ticket staff can quickly locate the booking.
    search_passenger_name = "Neha Singh"
    passenger_names = [booking["passenger_name"] for booking in passenger_bookings]
    print_passenger_report(passenger_bookings, "BEFORE index() - SEARCHING PASSENGER POSITION")
    if search_passenger_name in passenger_names:
        passenger_position = passenger_names.index(search_passenger_name)
        print(
            f"Passenger '{search_passenger_name}' found at list position: {passenger_position}, "
            f"Seat: {passenger_bookings[passenger_position]['seat_number']}"
        )
    else:
        print(f"Passenger '{search_passenger_name}' not found in current bookings.")
    print_passenger_report(passenger_bookings, "AFTER index() - POSITION SEARCH COMPLETE")

    # 6) sort(): Arrange bookings by ticket price from low to high for fare analysis and reporting.
    print_passenger_report(passenger_bookings, "BEFORE sort() - PRICE ORDERING")
    passenger_bookings.sort(key=lambda booking: booking["ticket_price"])
    print_passenger_report(passenger_bookings, "AFTER sort() - LOWEST TO HIGHEST PRICE")

    # 7) reverse(): Reverse the sorted list to show highest ticket price passengers first for premium review.
    print_passenger_report(passenger_bookings, "BEFORE reverse() - PREMIUM VIEW PREPARATION")
    passenger_bookings.reverse()
    print_passenger_report(passenger_bookings, "AFTER reverse() - HIGHEST TO LOWEST PRICE")

    # 8) count(): Count how many passengers are in Sleeper class for compartment planning.
    sleeper_classes = [booking["seat_class"] for booking in passenger_bookings]
    print_passenger_report(passenger_bookings, "BEFORE count() - SLEEPER PASSENGER COUNT")
    sleeper_count = sleeper_classes.count("Sleeper")
    print(f"Sleeper class passengers counted using count(): {sleeper_count}")
    print_passenger_report(passenger_bookings, "AFTER count() - LIST UNCHANGED, COUNT CAPTURED")

    # Final summary for reservation staff with key booking metrics.
    total_passengers = len(passenger_bookings)
    highest_ticket_booking = max(passenger_bookings, key=lambda booking: booking["ticket_price"])
    lowest_ticket_booking = min(passenger_bookings, key=lambda booking: booking["ticket_price"])

    print("\nFINAL BOOKED PASSENGERS SUMMARY")
    print("=" * 86)
    print(f"Total Passengers  : {total_passengers}")
    print(
        f"Highest Ticket    : {highest_ticket_booking['passenger_name']} "
        f"(₹{highest_ticket_booking['ticket_price']})"
    )
    print(
        f"Lowest Ticket     : {lowest_ticket_booking['passenger_name']} "
        f"(₹{lowest_ticket_booking['ticket_price']})"
    )
    print(f"Sleeper Count     : {sleeper_count}")
    print("=" * 86)


if __name__ == "__main__":
    demonstrate_lists()


Role:
Senior Python Developer, 20+ years experience, beginner-friendly code.

Task:
Generate 100% compilable Python program named "GHC14 - list_demo.py"
with function "demonstrate_lists".

Scenario:
A railway reservation system that uses Python lists to manage
passenger bookings — adding passengers, removing cancellations,
searching seats, sorting by ticket price, and generating
a final booked passengers report.

Conditions / Requirements:
1. Demonstrate all 8 list operations with real railway data:
     append()    → Add a new passenger booking
     insert()    → Insert VIP passenger at position 0
     remove()    → Remove a cancelled passenger by name
     pop()       → Remove last passenger (waitlist dropped)
     index()     → Find seat position of a passenger
     sort()      → Sort passengers by ticket price low to high
     reverse()   → Reverse to show highest price first
     count()     → Count passengers in sleeper class
2. Each operation must solve a real railway booking problem.
3. Every operation must have a comment explaining what
   it is doing and why this list method is used here.
4. Print the list state BEFORE and AFTER every operation
   so the change is clearly visible.
5. Use real railway variable names like passenger_name,
   ticket_price, seat_class, pnr_number and so on.
6. Use f-strings for all print statements.
7. Final summary must show:
     Total Passengers  → count
     Highest Ticket    → price with passenger name
     Lowest Ticket     → price with passenger name
     Sleeper Count     → number of sleeper class passengers

Rules:
1. Must compile and run in Python 3 without errors.
2. Add at top: import sys / sys.stdout.reconfigure(encoding='utf-8')
3. No external libraries, built-in only.
4. Clean indentation and comments on every block.
5. Main block inside if __name__ == "__main__".
6. Use = and - for table borders.
