# LaRicia Leach

# 12/3/24

# P5HW

# Brief description of program


import random

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

    def model_game():
        print("Are YOU a model??\n")

        # Randomize height, weight, and eligibility
        height = round(random.uniform(5.0, 6.5), 2)  # Height in feet (5'0" to 6'6")
        weight = random.randint(100, 250)  # Weight in pounds (100 to 250 lbs)
        eligible = random.choice([True, False])  # Randomly determine eligibility
        print()
        print()
        print()

        # Display randomized details
        print(f"⭑⚝ Your height: {height} ft")
        print(f"⭑⚝ Your weight: {weight} lbs")

        # Check eligibility
        if eligible:
            print("Are you eligible? ദ്ദി ˉ͈̀꒳ˉ͈́ )✧ ")
        else:
            print("Are you eligible? ✘")
            print("｡ ﾟ ꒰ঌ ✦໒꒱ ༘*.ﾟ Sorry! Just Kidding! Everyone is able to be a model.")
            print()
            print()
            print()

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

    # Run the game
    model_game()

    # Data for randomization
    locations = ["Paris, France", "Tokyo, Japan", "New York City, USA", "Milan, Italy", "Cape Town, South Africa", "Auckland, New Zealand", "Istanbul, Turkey"]
    themes = ["Elegant Evening", "Beach Party", "Streetwear Chic", "Gothic Glam", "Business Casual"]
    

    ethnicities = ["Asian", "African", "Caucasian", "Hispanic", "Mixed"]
    names = ["Alex", "Jordan", "Taylor", "Casey", "Morgan", "Jamie", "Charlie", "Dakota", "Riley", "Skyler"]

    hairstyles = {
        "Elegant Evening": ["Updo", "Soft Waves", "Classic Bun"],
        "Beach Party": ["Messy Bun", "Beach Waves", "Braids"],
        "Streetwear Chic": ["High Ponytail", "Undercut", "Messy Hair"],
        "Gothic Glam": ["Straight Black Hair", "Tousled Hair", "Mohawk"],
        "Business Casual": ["Low Bun", "Straight Hair", "French Twist"]
    }
    makeup = {
        "Elegant Evening": ["Smokey Eyes", "Red Lipstick", "Highlight"],
        "Beach Party": ["Natural Look", "Sun-kissed Glow", "Tinted Lip Balm"],
        "Streetwear Chic": ["Graphic Eyeliner", "Neutral Lip", "Bold Brows"],
        "Gothic Glam": ["Dark Lipstick", "Winged Eyeliner", "Heavy Contour"],
        "Business Casual": ["Light Foundation", "Neutral Eyeshadow", "Glossy Lip"]
    }

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

    # Game logic
    def model_game():
        print()
        print(f"⋆˚✿˖° Welcome to the Fashion Show in {location}!")
        print()
        print(f"Today's theme is: {theme}")
        print()
        print(f"You are competing against {num_models} other models.")
        print("Here are your competitors:")
        for model in competitors:
            print(f" - {model['name']} ({model['ethnicity']}), {model['height']} ft")

        print("\nLet's get started!")
        print("˚₊‧꒰ა ☆ ໒꒱ ‧₊˚ Choose the appropriate clothing for the theme.")

        points = 20000
        correct_items = shirts[theme]

        for _ in range(len(correct_items)):
            print("\nAvailable shirts:")

            # Ensure at least one correct item is included in the options
            options = random.sample(correct_items, 1) + random.sample([item for sublist in shirts.values() for item in sublist], 3)

            # Display shirt options
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")

            choice = int(input("Which shirt would you like to wear? Enter the number: "))

            # Check if the player's choice is correct
            if options[choice - 1] in correct_items:
                print("Correct choice ♡ଘ(੭ˊᵕˋ)੭* !")
                points += 1000
            else:
                print("Wrong choice! You lose 500 points (˚ ˃̣̣̥⌓˂̣̣̥ ).")
                points -= 500


        print("˚₊‧꒰ა ☆ ໒꒱ ‧₊˚ Choose the appropriate clothing for the theme.")

        points = 20000
        correct_items = bottoms[theme]

        for _ in range(len(correct_items)):
            print("\nAvailable pants/skirts:")

            # Ensure at least one correct item is included in the options
            options = random.sample(correct_items, 1) + random.sample([item for sublist in bottoms.values() for item in sublist], 3)

            # Display bottom options
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")

            choice = int(input("Which pants would you like to wear? Enter the number: "))

            # Check if the player's choice is correct
            if options[choice - 1] in correct_items:
                print("Good choice! You've earned points!")
                points += 1000
            else:
                print("Wrong choice! You lose 500 points (˚ ˃̣̣̥⌓˂̣̣̥ ).")
                points -= 500


        print("\nNext!")
        print("˚₊‧꒰ა ☆ ໒꒱ ‧₊˚ Choose the appropriate clothing for the theme.")

        points = 20000
        correct_items = shoes[theme]

        for _ in range(len(correct_items)):
            print("\nAvailable shoes:")

            # Ensure at least one correct item is included in the options
            options = random.sample(correct_items, 1) + random.sample([item for sublist in shoes.values() for item in sublist], 3)

            # Display shirt options
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")

            choice = int(input("Which shirt would you like to wear? Enter the number: "))

            # Check if the player's choice is correct
            if options[choice - 1] in correct_items:
                print("Correct choice ♡ଘ(੭ˊᵕˋ)੭* !")
                points += 1000
            else:
                print("Wrong choice! You lose 500 points (˚ ˃̣̣̥⌓˂̣̣̥ ).")
                points -= 500



        print("˚₊‧꒰ა ☆ ໒꒱ ‧₊˚ Choose the appropriate makeup for the theme.")

        points = 20000
        correct_items = makeup[theme]

        for _ in range(len(correct_items)):
            print("\nAvailable makeup:")

            # Ensure at least one correct item is included in the options
            options = random.sample(correct_items, 1) + random.sample([item for sublist in shirts.values() for item in sublist], 3)

            # Display shirt options
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")

            choice = int(input("Which makeup would you like to wear? Enter the number: "))

            # Check if the player's choice is correct
            if options[choice - 1] in correct_items:
                print("Good choice! You've earned points!")
                points += 1000
            else:
                print("Wrong choice! You lose 500 points (˚ ˃̣̣̥⌓˂̣̣̥ ).")
                points -= 500

        print("\nNext!")
        print("˚₊‧꒰ა ☆ ໒꒱ ‧₊˚ Choose the appropriate hairstyle for the theme.")

        points = 20000
        correct_items = hairstyles[theme]

        for _ in range(len(correct_items)):
            print("\nAvailable hairstyle:")

            # Ensure at least one correct item is included in the options
            options = random.sample(correct_items, 1) + random.sample([item for sublist in hairstyles.values() for item in sublist], 3)

            # Display shirt options
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")

            choice = int(input("Choose a hairstyle: "))

            # Check if the player's choice is correct
            if options[choice - 1] in correct_items:
                print("Great hairstyle choice! ✨")
                points += 1000
            else:
                print("Invalid hairstyle choice, but you still look fabulous! 💁")
                points -= 500


        print(f"Your final points: {points}")
        print("⋆ ˚ . ᵕ˛ᵕ .˚")
        if points >= 20000:
        print("Congratulations! You nailed the fashion show! ( ˶ˆᗜˆ˵ )!")
    else:
        print("Better luck next time ૮₍˶Ó﹏Ò ⑅₎ა!")



    model_game()






