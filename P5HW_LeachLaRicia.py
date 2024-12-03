# LaRicia Leach

# 12/3/24

# P5HW

# Brief description of program


def create_character():
    """
    Prompts the user to create a character by inputting its attributes.
    Returns a dictionary containing the character's details.
    """
    print("𝜗𝜚⋆₊˚ Welcome to the character creation screen! Let's design your character to start their journey as a model.")

    # Collect character basic details
    name = input(" ꒰ᐢ. .ᐢ꒱ Enter your character's name: ")
    gender = input("⪩. .⪨ Enter your character's gender (e.g., male, female, non-binary): ")

    # Collect physical attributes
    race = input("ㅤ♡ྀི ₊ Enter your character's race (e.g., human, elf, alien): ")
    ethnicity = input("˚ ༘ ೀ⋆｡˚ Enter your character's ethnicity: ")
    age = input("⋅˚₊‧ ୨୧ ‧₊˚ ⋅ Enter your character's age: ")
    body_type = input("˚୨୧⋆.˚  Enter your character's body type (e.g., athletic, slim, curvy, muscular): ")

    # Collect style details
    outfit = input("୭˚. ᵎᵎ Choose your character's outfit (e.g., formal wear, casual wear, high fashion): ")
    hairstyle = input(" ⋅˚₊‧ ଳ ‧₊˚ ⋅ Choose your character's hairstyle (e.g., short, long, ponytail): ")
    accessory = input(" ୧ ‧₊˚ 🍮 ⋅ ☆ Choose an accessory for your character (e.g., hat, necklace, glasses): ")

    # Create a dictionary to store the character details
    character = {
        "⤿ Name ༄.°": name,
        "⤿ Gender ༄.°": gender,
        "⤿ Race ༄.°": race,
        "⤿ Ethnicity": ethnicity,
        "⤿ Age ༄.°": age,
        "⤿ Body Type ༄.°": body_type,
        "⤿ Outfit ༄.°": outfit,
        "⤿ Hairstyle ༄.°": hairstyle,
        "⤿ Accessory ༄.°": accessory,
    }

    print("\n✶⋆.˚ Your character is ready to start their journey as a model!")
    return character

# Example usage:
if __name__ == "__main__":
    character = create_character()
    print("\nCharacter details:")
    for key, value in character.items():
        print(f"{key}: {value}")
print()
print()
print()
print()
import random

def model_game():
    print("Are YOU a model??\n")

    # Randomize height, weight, and eligibility
    height = round(random.uniform(5.0, 6.5), 2)  # Height in feet (5'0" to 6'6")
    weight = random.randint(100, 250)  # Weight in pounds (100 to 250 lbs)
    eligible = random.choice([True, False])  # Randomly determine eligibility

    # Display randomized details
    print(f"⭑⚝ Your height: {height} ft")
    print(f"⭑⚝ Your weight: {weight} lbs")
    
    # Check eligibility
    if eligible:
        print("Are you eligible? ദ്ദി ˉ͈̀꒳ˉ͈́ )✧ ")
        # Randomize model company and ranking
        companies = [
            "Elite Model Management", 
            "Ford Models", 
            "IMG Models", 
            "Wilhelmina Models", 
            "Next Management"
        ]
        company = random.choice(companies)
        ranking = random.randint(1, 2000)  # Ranking from 1 to 2000

        # Display company and ranking
        print(f"⋆.˚ Model company: {company}")
        print(f"⋆.˚ Model company ranking: #{ranking}")
    else:
        print("Are you eligible? ✘")
        print("Sorry!")
    
# Run the game
model_game()

import random

# Data for randomization
locations = ["Paris, France", "Tokyo, Japan", "New York City, USA", "Milan, Italy", "Cape Town, South Africa", "Auckland, New Zealand", "Istanbul, Turkey"]
themes = ["Elegant Evening", "Beach Party", "Streetwear Chic", "Gothic Glam", "Business Casual"]
clothing_items = {
    "Elegant Evening": ["Ball Gown", "Tuxedo", "Heels", "Jewelry"],
    "Beach Party": ["Swimsuit", "Sunglasses", "Flip-flops", "Sarong"],
    "Streetwear Chic": ["Hoodie", "Sneakers", "Baggy Jeans", "Cap"],
    "Gothic Glam": ["Black Dress", "Leather Jacket", "Chokers", "Combat Boots"],
    "Business Casual": ["Blazer", "Dress Shirt", "Loafers", "Pencil Skirt"]
}
ethnicities = ["Asian", "African", "Caucasian", "Hispanic", "Mixed"]
names = ["Alex", "Jordan", "Taylor", "Casey", "Morgan", "Jamie", "Charlie", "Dakota", "Riley", "Skyler"]

# Randomize the competition setup
location = random.choice(locations)
theme = random.choice(themes)
num_models = random.randint(3, 10)
competitors = [
    {
        "name": random.choice(names),
        "ethnicity": random.choice(ethnicities),
        "height": round(random.uniform(5.2, 6.5), 2)
    }
    for _ in range(num_models)
]

# Fashion show !!
def play_fashion_game():
    print(f"Welcome to the Fashion Show in {location}!")
    print(f"Today's theme is: {theme}")
    print(f"You are competing against {num_models} other models.")
    print("Here are your competitors:")
    for model in competitors:
        print(f" - {model['name']} ({model['ethnicity']}), {model['height']} ft")

    print("\nLet's get started!")
    print("Choose the appropriate clothing for the theme.")

    points = 20000
    correct_items = clothing_items[theme]

    for _ in range(len(correct_items)):
        print("\nAvailable clothing items:")
        options = random.sample(
            list(set(sum(clothing_items.values(), []))), 4
        )  # Randomize from all items
        print(", ".join(options))
        choice = input("Select an item: ").strip()

        if choice in correct_items:
            print("Correct choice!")
        else:
            print(f"Wrong choice! You lose 500 points.")
            points -= 500

    print(f"\nYour final score: {points}")
    if points >= 20000:
        print("Congratulations! You nailed the fashion show!")
    else:
        print("Better luck next time!")

# Start the game
if __name__ == "__main__":
    play_fashion_game()







