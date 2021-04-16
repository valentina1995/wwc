# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import logging

logger = logging.getLogger(__name__)

import datetime
import json
import pathlib
import uuid

from typing import Any, Text, Dict, List, Union
from rasa_sdk.types import DomainDict
from rasa_sdk import Tracker, Action, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import ActionExecuted


from db import (
    db_connect, create_table, get_cursor,
    create_reservation, table_exists,
    reservation_config)

con = db_connect()
cur = get_cursor(con)

def save(data: tuple) -> None:
    if not table_exists(cur, 'reservations'):
        create_table(cur, 'reservations', reservation_config)
    try:
        create_reservation(cur, data)
        con.commit()
    except Exception as e:
        con.rollback()
        logger.warning(f"Rolling back: {str(e)}")
    else:
        logger.info('Transaction saved')


class MakeReservationAction(Action):
    def name(self):
        return 'action_make_reservation'

    async def run(
        self,
        distpacher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict]:
        
        user = tracker.get_slot('user_name')
        identification = tracker.get_slot('identification')
        number = tracker.get_slot('phone_number')
        date = tracker.get_slot('reservation_date')
        time = tracker.get_slot('reservation_time')
        people = tracker.get_slot('reservation_people')
        save((str(uuid.uuid1()), user, identification, number, date, time, people))
        return [ActionExecuted(self.name())]


class ValidateReservationForm(FormValidationAction):
    def name(self):
        return "validate_restaurant_form"

    def validate_user_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate reservation user name value"""
        if len(slot_value) < 3:
            dispatcher.utter_message(text=f"That is a very short name, i think you misspell it ")
            return {'user_name': None}
        return {'user_name': slot_value}

    def validate_identification(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate reservation identification value"""
        if len(slot_value) <= 6:
            dispatcher.utter_message(text=f"That is a short ID :(")
            return {'identification': None}
        elif '.' not in slot_value:
            dispatcher.utter_message(text=f"You should send your ID number with dot separator")
        return {'identification': slot_value}

    def validate_phone_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate phone_number value"""
        if len(slot_value) <= 5:
            dispatcher.utter_message(text=f"That is a short phone number :(")
            return {'identification': None}

        if '.' in slot_value:
            dispatcher.utter_message(text=f"Could you please send the phone number withot dots please?")
            return {'identification': None}      
        return {'phone_number': slot_value}

    def validate_reservation_date(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate reservation date value"""
        return {'reservation_date': slot_value}

    def validate_reservation_time(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate reservation time value"""
        return {'reservation_time': slot_value}

    def validate_reservation_people(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate reservation people value"""
        #if not num_people:
        #    dispatcher.utter_message(text=f"It would be better for me if you just say how many people wil be sited in the table")
        #    return {'reservation_people': None}
        return {'reservation_people': slot_value}