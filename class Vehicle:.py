class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

# Demonstration
if __name__ == "__main__":
    # Create instances of Vehicle
    vehicle1 = Vehicle("ABC123", "Car", "Alice")
    vehicle2 = Vehicle("XYZ789", "Truck", "Bob")

    # Display initial owner
    print("Initial Owners:")
    print("Vehicle 1 Owner:", vehicle1.owner)
    print("Vehicle 2 Owner:", vehicle2.owner)

    # Update owner
    vehicle1.update_owner("Charlie")
    vehicle2.update_owner("David")

    # Display updated owner
    print("\nUpdated Owners:")
    print("Vehicle 1 Owner:", vehicle1.owner)
    print("Vehicle 2 Owner:", vehicle2.owner)

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count attribute
    
    def add_participant(self):
        self.participant_count += 1
    
    def get_participant_count(self):
        return self.participant_count

# Demonstration
if __name__ == "__main__":
    # Create an instance of Event
    event = Event("Conference", "2024-05-25")
    
    # Display initial participant count
    print("Initial Participant Count:", event.get_participant_count())
    
    # Add participants
    event.add_participant()
    event.add_participant()
    
    # Display updated participant count
    print("Updated Participant Count:", event.get_participant_count())