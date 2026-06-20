print("================================")
print("      FARMER BABA CHATBOT")
print("================================")
print("Type 'help' to see what you can ask, or 'bye' to exit.")

while True:
    question = input("\nAsk something about my Baba: ").lower()

    if "help" in question:
        print("You can ask about: name, job, crops, experience, education, routine, animals, advice, family, tea, strength, future!")

    elif "name" in question:
        print("My Baba's name is Muhammad Ahmed.")

    elif "job" in question or "work" in question:
        print("He is a hardworking farmer.")

    elif "crops" in question or "wheat" in question:
        print("He grows different crops such as wheat, cotton, and vegetables.")

    elif "experience" in question or "years" in question:
        print("He has many years of farming experience.")

    elif "education" in question:
        print("He has basic education, but he has a lot of practical farming knowledge.")

    elif "routine" in question or "morning" in question:
        print("He wakes up early in the morning and goes to the fields.")

    elif "animals" in question or "livestock" in question:
        print("He takes care of farm animals and ensures they are healthy.")

    elif "advice" in question:
        print("He always says: 'Hard work and patience bring success.'")

    elif "family" in question or "home" in question:
        print("He loves his family and works hard for their future.")

    elif "tea" in question:
        print("He enjoys drinking tea after working in the fields.")

    elif "strength" in question:
        print("His biggest strength is his dedication and honesty.")

    elif "future" in question or "goal" in question:
        print("He wants his children to be successful and educated.")

    elif "weather" in question:
        print("He always keeps an eye on the weather because it affects farming.")

    elif "favorite" in question:
        print("His favorite thing is seeing healthy crops growing in the fields.")

    elif "water" in question or "irrigation" in question:
        print("He carefully manages irrigation to make sure crops get enough water.")

    elif "tractor" in question:
        print("He uses a tractor and other farming tools to work efficiently in the fields.")

    elif "harvest" in question:
        print("Harvest season is his favorite time because he can see the results of his hard work.")

    elif "challenge" in question or "problem" in question:
        print("Weather changes, pests, and rising costs are some of the challenges he faces.")

    elif "success" in question:
        print("For him, success means healthy crops, a happy family, and satisfied customers.")
