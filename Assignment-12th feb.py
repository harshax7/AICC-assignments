
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your favorite hobby: ")
if age < 13:
    category = "a Child"
elif age < 20:
    category = "a Teenager"
elif age < 60:
    category = "an Adult"
else:
    category = "a Senior Citizen"
print("\n--- Personalized Message ---")
print(f"Hello {name}! 👋")
print(f"You are {category}.")
print(f"It's great that you enjoy {hobby}! Keep it up! 🎯")

#Sample output
# Enter your name: Sneha
# Enter your age: 20
# Enter your favorite hobby: Dancing

# --- Personalized Message ---
# Hello Sneha! 👋
# You are an Adult.
# It's great that you enjoy Dancing! Keep it up! 🎯