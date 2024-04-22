# Task #1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


# Task #2: Venue Selection

attendees = int(input("Enter number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
need_projector = "You will need a projector." if attendees > 10 else "You will not need a projector."
audio_system = "You will need a microphone." if attendees > 25 else "You will not need a microphone."

print(f"The event should be held in a {venue}. {need_projector} {audio_system}")


# Task #3: Catering Choices

food_preference = (input("Do you want vegetarian food? (yes/no) "))

caterer = "Veggie Delight Caterers" if food_preference == "yes" else "Gourmet Meal Caterers"

print(f"You should use {caterer} to cater your event." )
