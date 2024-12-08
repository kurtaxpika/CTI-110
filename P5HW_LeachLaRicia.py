
# LaRicia Leach

# 12/3/24

# P5HW

# To make a fashion game

import random

def create_character():
    """
    Prompts the user to create a character by inputting its attributes.
    Returns a dictionary containing the character's details.
    """
    print("𝜗𝜚⋆₊˚ Welcome to the character creation screen! Let's design your character to start their journey as a model.\n")

    # Collect character basic details
    name = input(" ꒰ᐢ. .ᐢ꒱ Enter your character's name: ").strip()
    gender = input("⪩. .⪨ Enter your character's gender (e.g., male, female, non-binary): ").strip()

    # Collect physical attributes
    race = input("ㅤ♡ྀི ₊ Enter your character's race (e.g., human, elf, alien): ").strip()
    ethnicity = input("˚ ༘ ೀ⋆｡˚ Enter your character's ethnicity: ").strip()
    try:
        age = int(input("⋅˚₊‧ ୨୧ ‧₊˚ ⋅ Enter your character's age: "))
        height = float(input("⋅˚₊‧ ୨୧ ‧₊˚ ⋅ Enter your character's height in feet (e.g., 5.8): "))
    except ValueError:
        print("\n⭑⚝ Invalid! Invalid input for age or height! Please restart the game and enter numbers.")
        exit()

    # Check eligibility
    if age < 18:
        print("\n𐙚🧸ྀི Sorry, your character is too young to compete.")
        exit()
    elif height < 5.0:
        print("\n𐙚🧸ྀི Sorry, your character's height doesn't meet the requirements to compete.")
        exit()
    else:
        print("Are you eligible? ദ്ദി ˉ͈̀꒳ˉ͈́ )✧ ")
    

    body_type = input("˚୨୧⋆.˚ Enter your character's body type (e.g., athletic, slim, curvy, muscular): ").strip()

    # Collect style details
    outfit = input("୭˚. ᵎᵎ Choose your character's outfit (e.g., formal wear, casual wear, high fashion): ").strip()
    hairstyle = input(" ⋅˚₊‧ ଳ ‧₊˚ ⋅ Choose your character's hairstyle (e.g., short, long, ponytail): ").strip()
    accessory = input(" ୧ ‧₊˚ 🍮 ⋅ ☆ Choose an accessory for your character (e.g., hat, necklace, glasses): ").strip()

    # Create a dictionary to store the character details
    character = {
        "⤿ Name ༄.°": name,
        "⤿ Gender ༄.°": gender,
        "⤿ Race ༄.°": race,
        "⤿ Ethnicity": ethnicity,
        "⤿ Age ༄.°": age,
        "⤿ Height ༄.°": height,
        "⤿ Body Type ༄.°": body_type,
        "⤿ Outfit ༄.°": outfit,
        "⤿ Hairstyle ༄.°": hairstyle,
        "⤿ Accessory ༄.°": accessory,
    }
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

    print("\n✶⋆.˚ Your character is ready to start their journey as a model!\n")
    return character


def model_game(character):
    """
    Main game logic for the fashion show.
    """
    # Data setup
    locations = ["Paris, France", "Tokyo, Japan", "New York City, USA", "Milan, Italy"]
    themes = ["Elegant Evening", "Beach Party", "Streetwear Chic", "Gothic Glam", "Business Casual"]

    # Define clothing, accessories, makeup, and hairstyles for themes
    shirts = {
        "Elegant Evening": ["Silk Blouse", "Sequined Top"],
        "Beach Party": ["Tank Top", "Crop Top"],
        "Streetwear Chic": ["Graphic Tee", "Oversized Hoodie"],
        "Gothic Glam": ["Black Lace Shirt", "Velvet Blouse"],
        "Business Casual": ["Button-Up Shirt", "Blazer"]
    }
    bottoms = {
        "Elegant Evening": ["Maxi Skirt", "Dress Pants"],
        "Beach Party": ["Shorts", "Sarong"],
        "Streetwear Chic": ["Cargo Pants", "Ripped Jeans"],
        "Gothic Glam": ["Leather Skirt", "Black Jeans"],
        "Business Casual": ["Chinos", "Pencil Skirt"]
    }
    shoes = {
        "Elegant Evening": ["Heels", "Loafers"],
        "Beach Party": ["Sandals", "Flip-Flops"],
        "Streetwear Chic": ["Sneakers", "Combat Boots"],
        "Gothic Glam": ["Platform Boots", "Heels"],
        "Business Casual": ["Oxford Shoes", "Ballet Flats"]
    }
    makeup = {
        "Elegant Evening": ["Smokey Eyes", "Red Lipstick", "Highlight"],
        "Beach Party": ["Natural Look", "Sun-kissed Glow", "Tinted Lip Balm"],
        "Streetwear Chic": ["Graphic Eyeliner", "Neutral Lip", "Bold Brows"],
        "Gothic Glam": ["Dark Lipstick", "Winged Eyeliner", "Heavy Contour"],
        "Business Casual": ["Light Foundation", "Neutral Eyeshadow", "Glossy Lip"]
    }
    hairstyles = {
        "Elegant Evening": ["Updo", "Soft Waves", "Classic Bun"],
        "Beach Party": ["Messy Bun", "Beach Waves", "Braids"],
        "Streetwear Chic": ["High Ponytail", "Undercut", "Messy Hair"],
        "Gothic Glam": ["Straight Black Hair", "Tousled Hair", "Mohawk"],
        "Business Casual": ["Low Bun", "Straight Hair", "French Twist"]
    }

    # Randomize competition
    location = random.choice(locations)
    theme = random.choice(themes)
    num_models = random.randint(3, 6)
    competitors = [
        {
            "name": random.choice(["Alex", "Jordan", "Taylor", "Casey", "Morgan", "Jamie", "Charlie", "Dakota", "Riley", "Skyler"]),
            "ethnicity": random.choice(["Asian", "African", "Caucasian", "Hispanic", "Mixed"]),
            "height": round(random.uniform(5.2, 6.5), 2)
        }
        for _ in range(num_models)
    ]

    print(f"\nWelcome to the Fashion Show in {location}!")
    print(f"The theme for this show is: {theme}\n")

    print(f"You are competing against {num_models} other models.")
    print("Here are your competitors:")
    for model in competitors:
        print(f" - {model['name']} ({model['ethnicity']}), {model['height']} ft\n")

    points = 20000

    # Helper function for selecting items
    def choose_items(category_name, items):
        nonlocal points
        print(f"\nChoose {category_name}:")
        correct_items = items
        wrong_items = ["Banana Suit", "Clown Shoes", "Flamingo Hat", "Trash Bag"]
        options = random.sample(correct_items + wrong_items, len(correct_items) + len(wrong_items))
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        while True:
            try:
                choice = int(input(f"Which {category_name.lower()} will you choose? Enter the number: "))
                if 1 <= choice <= len(options):
                    chosen_item = options[choice - 1]
                    if chosen_item in correct_items:
                        print(f"Great choice! ✨ {chosen_item} matches the theme!")
                        points += 1000
                    else:
                        print(f"Oops! {chosen_item} doesn't fit the theme.")
                        points -= 500
                    break
                else:
                    print("Invalid choice! Please pick a valid option.")
            except ValueError:
                print("Please enter a number.")

    # Play rounds for shirts, bottoms, shoes, makeup, and hairstyles
    choose_items("Shirt", shirts[theme])
    choose_items("Bottom", bottoms[theme])
    choose_items("Shoes", shoes[theme])
    choose_items("Makeup", makeup[theme])
    choose_items("Hairstyle", hairstyles[theme])

    # Final score and result
    print(f"\nFinal Score: {points}")
    if points >= 22000:
        print("✨ Congratulations! You nailed the fashion show! ✨")
    else:
        print("Better luck next time. Keep practicing!")

    # Generate scores for competitors
    competitor_scores = [random.randint(19000, 24000) for _ in competitors]
    print("\nCompetitor Results:")
    for competitor, score in zip(competitors, competitor_scores):
        print(f" - {competitor['name']} scored {score} points.")

    # Check if the player won
    if points > max(competitor_scores):
        print("\n🌟 YOU WON THE FASHION SHOW! 🌟")
    else:
        print("\nYou didn't win this time, but keep trying!")

# Main program
if __name__ == "__main__":
    character = create_character()
    model_game(character)


