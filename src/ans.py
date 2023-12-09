""" 
Question 2: Event Management

Description:

Create a class called EventManager. It should have the following attributes and methods:

Attributes: event_name (string) and participants (list of participant names).

Methods:

add_participant(name): Adds a new participant.

remove_participant(name): Removes a participant.

get_participant_list(): Returns a list of all participants.
"""

class EventManager:
    def __init__(self, typeOfEvent):
        self.typeOfEvent = typeOfEvent
        self.participants = []
    
    def add_participant(self, personToAdd):
        self.participants.append(personToAdd)
    
    def remove_participant(self, personToRemove):
        self.participants.remove(personToRemove)
    
    def get_participant_list(self):
        return self.participants
