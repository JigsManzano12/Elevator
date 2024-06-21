import time

class Elevator:
    def __init__(self, total_floors):
        self.total_floors = total_floors
        self.current_floor = 0
        self.requests = []

    def request_floor(self, floor):
        if 0 <= floor < self.total_floors:
            self.requests.append(floor)
            self.requests = sorted(set(self.requests))  # Remove duplicates and sort
            print(f"Floor {floor} requested.")
        else:
            print(f"Floor {floor} is out of range.")

    def move(self):
        if not self.requests:
            print("No requests to process.")
            return

        next_floor = self.requests.pop(0)
        if next_floor > self.current_floor:
            self.move_up(next_floor)
        elif next_floor < self.current_floor:
            self.move_down(next_floor)

    def move_up(self, floor):
        for f in range(self.current_floor + 1, floor + 1):
            self.current_floor = f
            print(f"Moving up... Current floor: {self.current_floor}")
            time.sleep(2)  # Wait for 2 seconds to simulate the elevator moving up
        print(f"Arrived at floor {floor}")

    def move_down(self, floor):
        for f in range(self.current_floor - 1, floor - 1, -1):
            self.current_floor = f
            print(f"Moving down... Current floor: {self.current_floor}")
            time.sleep(2)  # Wait for 2 seconds to simulate the elevator moving down
        print(f"Arrived at floor {floor}")

    def status(self):
        print(f"Current floor: {self.current_floor}")
        print(f"Pending requests: {self.requests}")

# Create an instance of the Elevator class
elevator = Elevator(total_floors=10)

# Main loop for user input
while True:
    user_input = input("Enter the floor number to request the elevator (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    try:
        floor = int(user_input)
        elevator.request_floor(floor)
    except ValueError:
        print("Invalid input. Please enter a valid floor number.")

    elevator.move()
    elevator.status()
