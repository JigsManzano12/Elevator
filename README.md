# Simple Elevator Simulation

This is a simple elevator simulation implemented in Python. The simulation allows users to request floors, and the elevator moves up or down to serve the requests with a simulated delay.

## Features

- Move the elevator up and down between floors.
- Accept and process floor requests from users.
- Simulate a delay of 2 seconds for each floor the elevator moves.
- Display the current status of the elevator, including the current floor and pending requests.

## How to Use

1. **Clone the repository** (or copy the code into a Python file on your local machine):
    ```bash
    git clone https://github.com/your-username/elevator-simulation.git
    cd elevator-simulation
    ```

2. **Run the simulation**:
    ```bash
    python elevator.py
    ```

3. **Enter floor requests**:
    - When prompted, enter the floor number you want to request.
    - To quit the simulation, enter `q`.

## Example

```plaintext
Enter the floor number to request the elevator (or 'q' to quit): 5
Floor 5 requested.
Moving up... Current floor: 1
Moving up... Current floor: 2
Moving up... Current floor: 3
Moving up... Current floor: 4
Moving up... Current floor: 5
Arrived at floor 5
Current floor: 5
Pending requests: []

Enter the floor number to request the elevator (or 'q' to quit): 2
Floor 2 requested.
Moving down... Current floor: 4
Moving down... Current floor: 3
Moving down... Current floor: 2
Arrived at floor 2
Current floor: 2
Pending requests: []
