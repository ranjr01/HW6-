# main.py
from velocity_calculator import calculate_velocity_core_logic

def get_previous_sprints_points_user_input():
    try:
        points_str = input("Enter previous sprint points (comma-separated): ")
        return list(map(int, points_str.split(',')))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return get_previous_sprints_points_user_input()

def main_velocity_user_input():
    print("Welcome to Velocity Calculator!")

    # Feature: Calculate a sprint team’s velocity (User Input)
    previous_sprints_points = get_previous_sprints_points_user_input()
    velocity = calculate_velocity_core_logic(previous_sprints_points)
    print(f"Sprint Velocity: {velocity}")

if __name__ == "__main__":
    main_velocity_user_input()
