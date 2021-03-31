# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import pathlib
import json
from typing import Any, Text, Dict, List, Union
from rasa_sdk.types import DomainDict
from rasa_sdk import Tracker, Action, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ActionExecuted


path = '/Users/juan.valencia/Documents/workspace/gorilla/wwc/ml/chatbot/project/actions/bookings.txt'
def save(data: Dict[Text, Any]) -> None:
    data = json.dumps(data) + '\n'
    with open(path, "r") as f:
        file_data = f.read()
    data = file_data + data
    with open(path, "w") as f:
        f.write(data)


class MakeReservationAction(Action):
    def name(self):
        return 'action_make_reservation'

    async def run(
        self,
        distpacher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict]:
        
        date = tracker.get_slot('reservation_date')
        time = tracker.get_slot('reservation_time')
        people = tracker.get_slot('reservation_people')
        save({'date': date, 'time': time, 'people': people})
        return [ActionExecuted(self.name())]


class ValidateReservationForm(FormValidationAction):
    def name(self):
        return "validate_restaurant_form"

    def validate_reservation_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate reservation date value"""
        pass

    def validate_reservation_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate reservation time value"""
        pass

    def validate_reservation_people(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate reservation people value"""
        slot_pieces = slot_value.split()
        for piece in slot_pieces:
            try:
                num_people = int(piece)
            except ValueError as e:
                num_people = None
        if not num_people:
            dispatcher.utter_message(text=f"It would be better for me if you just say how many people wil be sited in the table")
            return {'reservation_people': None}
        return {'reservation_people': num_people}