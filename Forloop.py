import random
# 1. Rolling a six-sided die
rolls = 20
count_6 = 0
count_1 = 0
two_sixes_in_row = 0
previous_roll = None
print("Rolling the die...\n")
for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1
    if roll == 6 and previous_roll == 6:
        two_sixes_in_row += 1
    previous_roll = roll
print("\n--- Dice Statistics ---")
print("Number of times rolled 6:", count_6)
print("Number of times rolled 1:", count_1)
print("Number of times rolled two 6s in a row:", two_sixes_in_row)

# 2. Jumping Jacks Workout

total_jumping_jacks = 100
completed = 0
print("\nWorkout Started!\n")
while completed < total_jumping_jacks:
    completed += 10
    print(f"You completed {completed} jumping jacks.")
    if completed == total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break
    tired = input("Are you tired? (yes/y or no/n): ").lower()
    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip == "yes" or skip == "y":
            print(f"You completed a total of {completed} jumping jacks.")
            break
    remaining = total_jumping_jacks - completed
    print(f"{remaining} jumping jacks remaining.\n")