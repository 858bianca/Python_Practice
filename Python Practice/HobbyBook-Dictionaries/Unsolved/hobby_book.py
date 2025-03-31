## Create a dictionary to hold the actor's names.
myself = {"name": "Bianca",
          "occupation": "Credit Specialist",
          "age": 25,
          "hobbies":["working out", "walking my weenie dogs", "cooking", "sleeping and eating"],
          "schedule":{"Monday through Friday": 7, "Saturday thru Sunday": 10}}

# Print out results are stored in the dictionary
print(f'Hello I am {myself["name"]} and I am a {myself["occupation"]}')
print(f'I have {len(myself["hobbies"])} hobbies!')
print(f'On the weekend I get up at {myself["wake-up"]["Saturday"]}')
