"""
ShadowFox Python Development Internship
Task 1 (Beginner) - Topic 5: For Loop
Author: Shaik Sadiya Kousar
"""

import random

# ---------------------------------------------------------
# 1. Simulate rolling a six-sided die at least 20 times.
#    Count: how many 6s, how many 1s, how many times two 6s
#    were rolled back-to-back.
# ---------------------------------------------------------
def dice_simulation():
    rolls = [random.randint(1, 6) for _ in range(25)]
    print("Rolls:", rolls)

    count_six = 0
    count_one = 0
    consecutive_sixes = 0
    previous_roll = None

    for roll in rolls:
        if roll == 6:
            count_six += 1
            if previous_roll == 6:
                consecutive_sixes += 1
        if roll == 1:
            count_one += 1
        previous_roll = roll

    print(f"Number of 6s rolled: {count_six}")
    print(f"Number of 1s rolled: {count_one}")
    print(f"Number of times two 6s appeared in a row: {consecutive_sixes}")


# ---------------------------------------------------------
# 2. Jumping Jacks Workout (100 total, 10 per set)
# ---------------------------------------------------------
def jumping_jacks_workout():
    total_required = 100
    per_set = 10
    completed = 0

    while completed < total_required:
        input(f"Perform {per_set} jumping jacks, then press Enter...")
        completed += per_set

        tired = input("Are you tired? (yes/no): ").strip().lower()

        if tired in ("yes", "y"):
            skip = input("Do you want to skip the remaining sets? (yes/no): ").strip().lower()
            if skip in ("yes", "y"):
                print(f"You completed a total of {completed} jumping jacks.")
                break

        remaining = total_required - completed
        if remaining > 0:
            print(f"{remaining} jumping jacks remaining.")
        else:
            print("Congratulations! You completed the workout")


if __name__ == "__main__":
    print("--- 1. Dice Simulation ---")
    dice_simulation()
    print("\n--- 2. Jumping Jacks Workout ---")
    jumping_jacks_workout()
