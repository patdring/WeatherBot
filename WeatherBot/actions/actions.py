from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from actions.weather import Weather

"""Code ist based on https://rasa.com/docs/rasa/action-server/sdk-actions"""

"""Global Weather object which enables the retrieval of weather data"""
w = Weather();

class ActionGetTemperature(Action):
    """
    Subclass of the Rasa SDK Action class.
    Overwrites the two required methods, name and run. 
    The action server will call an action according to the return value of 
    its name method when it receives a request to run an action.
    Uses Weather class to query temperature data.

    Methods
    -------
    name(): str
        Returns the action's name.
    run(dispatcher, tracker, domain): List[Dict[str, Any]]
        Executes the side effects of the action.
    """

    def name(self):
        """
        Returns the action's name. 
        The name returned by this method is the one used in your bot's domain

        Returns
        -------
        str: name of the action
        """

        return "action_get_temperature"

    def run(self, dispatcher, tracker, domain):
        """
        Executes the side effects of the action
        and queries temperature data.

        Parameters
        ----------
        dispatcher : Any
            Used to send messages back to the user
        tracker: Any
            Contains information about the conversation
        domain: Any
            The bot's domain

        Returns
        -------
        List[Dict[str, Any]]: rasa_sdk.events.Event instances
        """

        loc = tracker.get_slot("location")

        if tracker.latest_message['entities']:
            loc = tracker.latest_message['entities'][0]['value']
            data = w.getTemperature(loc)
            dispatcher.utter_message(text=f"It is {data}°C in {loc}.")          
        elif not loc: 
            loc = w.getRegion()
            data = w.getTemperature()
            dispatcher.utter_message(text=f"It is {data}°C in {loc} (location based on your IP address).")
        else:
            data = w.getTemperature(loc)
            dispatcher.utter_message(text=f"It is {data}°C in {loc}.")

        return [SlotSet("location", loc)]

class ActionGetDescription(Action):
    """
    Subclass of the Rasa SDK Action class.
    Overwrites the two required methods, name and run. 
    The action server will call an action according to the return value of 
    its name method when it receives a request to run an action.
    Uses Weather class to query tweather description data.

    Methods
    -------
    name(): str
        Returns the action's name.
    run(dispatcher, tracker, domain): List[Dict[str, Any]]
        Executes the side effects of the action.
    """    

    def name(self):
        """
        Returns the action's name. 
        The name returned by this method is the one used in your bot's domain

        Returns
        -------
        str: name of the action
        """

        return "action_get_description"

    def run(self, dispatcher, tracker, domain):
        """
        Executes the side effects of the action
        and queries weather description data.

        Parameters
        ----------
        dispatcher : Any
            Used to send messages back to the user
        tracker: Any
            Contains information about the conversation
        domain: Any
            The bot's domain

        Returns
        -------
        List[Dict[str, Any]]: rasa_sdk.events.Event instances
        """

        loc = tracker.get_slot("location")

        if tracker.latest_message['entities']:
            loc = tracker.latest_message['entities'][0]['value']
            data = w.getDescription(loc).lower()
            dispatcher.utter_message(text=f"It is {data} in {loc}.")          
        elif not loc: 
            loc = w.getRegion()
            data = w.getDescription().lower()
            dispatcher.utter_message(text=f"It is {data}  in {loc} (location based on your IP address).")
        else:
            data = w.getDescription(loc).lower() 
            dispatcher.utter_message(text=f"It is {data} in {loc}.")

        return [SlotSet("location", loc)]

class ActionGetPrecipitation(Action):
    """
    Subclass of the Rasa SDK Action class.
    Overwrites the two required methods, name and run. 
    The action server will call an action according to the return value of 
    its name method when it receives a request to run an action.
    Uses Weather class to query percipitation data.

    Methods
    -------
    name(): str
        Returns the action's name.
    run(dispatcher, tracker, domain): List[Dict[str, Any]]
        Executes the side effects of the action.
    """

    def name(self):
        """
        Returns the action's name. 
        The name returned by this method is the one used in your bot's domain

        Returns
        -------
        str: name of the action
        """

        return "action_get_precipitation"

    def run(self, dispatcher, tracker, domain):
        """
        Executes the side effects of the action
        and queries precipitation data.

        Parameters
        ----------
        dispatcher : Any
            Used to send messages back to the user
        tracker: Any
            Contains information about the conversation
        domain: Any
            The bot's domain

        Returns
        -------
        List[Dict[str, Any]]: rasa_sdk.events.Event instances
        """

        loc = tracker.get_slot("location")

        if tracker.latest_message['entities']:
            loc = tracker.latest_message['entities'][0]['value']
            data = w.getPrecipitation(loc)
            dispatcher.utter_message(text=f"Perciptitation is {data} in {loc}.")          
        elif not loc: 
            loc = w.getRegion()
            data = w.getPrecipitation()
            dispatcher.utter_message(text=f"Perciptitation is {data} in {loc} (location based on your IP address).")
        else:
            data = w.getPrecipitation(loc)
            dispatcher.utter_message(text=f"Perciptitation is {data} in {loc}.")

        return [SlotSet("location", loc)]

class ActionGetHumidity(Action):
    """
    Subclass of the Rasa SDK Action class.
    Overwrites the two required methods, name and run. 
    The action server will call an action according to the return value of 
    its name method when it receives a request to run an action.
    Uses Weather class to query humidity data.

    Methods
    -------
    name(): str
        Returns the action's name.
    run(dispatcher, tracker, domain): List[Dict[str, Any]]
        Executes the side effects of the action.
    """

    def name(self):
        """
        Returns the action's name. 
        The name returned by this method is the one used in your bot's domain

        Returns
        -------
        str: name of the action
        """

        return "action_get_humidity"

    def run(self, dispatcher, tracker, domain):
        """
        Executes the side effects of the action
        and queries humidity data.

        Parameters
        ----------
        dispatcher : Any
            Used to send messages back to the user
        tracker: Any
            Contains information about the conversation
        domain: Any
            The bot's domain

        Returns
        -------
        List[Dict[str, Any]]: rasa_sdk.events.Event instances
        """

        loc = tracker.get_slot("location")

        if tracker.latest_message['entities']:
            loc = tracker.latest_message['entities'][0]['value']
            data = w.getHumidity(loc)
            dispatcher.utter_message(text=f"Humidity is {data} in {loc}.")          
        elif not loc: 
            loc = w.getRegion()
            data = w.getHumidity()
            dispatcher.utter_message(text=f"Humidity is {data} in {loc} (location based on your IP address).")
        else:
            data = w.getHumidity(loc)
            dispatcher.utter_message(text=f"Humidity is {data} in {loc}.")

        return [SlotSet("location", loc)]

class ActionGetWind(Action):
    """
    Subclass of the Rasa SDK Action class.
    Overwrites the two required methods, name and run. 
    The action server will call an action according to the return value of 
    its name method when it receives a request to run an action.
    Uses Weather class to query wind speed data.

    Methods
    -------
    name(): str
        Returns the action's name.
    run(dispatcher, tracker, domain): List[Dict[str, Any]]
        Executes the side effects of the action.
    """

    def name(self):
        """
        Returns the action's name. 
        The name returned by this method is the one used in your bot's domain

        Returns
        -------
        str: name of the action
        """

        return "action_get_wind"

    def run(self, dispatcher, tracker, domain):
        """
        Executes the side effects of the action
        and queries wind speed data.

        Parameters
        ----------
        dispatcher : Any
            Used to send messages back to the user
        tracker: Any
            Contains information about the conversation
        domain: Any
            The bot's domain

        Returns
        -------
        List[Dict[str, Any]]: rasa_sdk.events.Event instances
        """

        loc = tracker.get_slot("location")

        if tracker.latest_message['entities']:
            loc = tracker.latest_message['entities'][0]['value']
            data = w.getWind(loc)
            dispatcher.utter_message(text=f"Wind speed is {data} in {loc}.")          
        elif not loc: 
            loc = w.getRegion()
            data = w.getWind()
            dispatcher.utter_message(text=f"Wind speed is {data} in {loc} (location based on your IP address).")
        else:
            data = w.getWind(loc)
            dispatcher.utter_message(text=f"Wind speed is {data} in {loc}.")

        return [SlotSet("location", loc)]

class ActionGetForecast(Action):
    """
    Subclass of the Rasa SDK Action class.
    Overwrites the two required methods, name and run. 
    The action server will call an action according to the return value of 
    its name method when it receives a request to run an action.
    Uses Weather class to query tweather forecast data.

    Methods
    -------
    name(): str
        Returns the action's name.
    run(dispatcher, tracker, domain): List[Dict[str, Any]]
        Executes the side effects of the action.
    """

    def name(self):
        """
        Returns the action's name. 
        The name returned by this method is the one used in your bot's domain

        Returns
        -------
        str: name of the action
        """

        return "action_get_forecast"

    def run(self, dispatcher, tracker, domain):
        """
        Executes the side effects of the action
        and queries forecast data.

        Parameters
        ----------
        dispatcher : Any
            Used to send messages back to the user
        tracker: Any
            Contains information about the conversation
        domain: Any
            The bot's domain

        Returns
        -------
        List[Dict[str, Any]]: rasa_sdk.events.Event instances
        """

        loc = tracker.get_slot("location")

        if tracker.latest_message['entities']:
            loc = tracker.latest_message['entities'][0]['value']
            data = w.getForecast(loc)
        elif not loc: 
            loc = w.getRegion()
            data = w.getForecast()
        else:
            data = w.getForecast(loc)

        s=''
        for dayweather in data:    
            s +=f" {dayweather['weather']}"
            s +=f" on {dayweather['name']}"
            s +=f" with max. {dayweather['max_temp']}°C"
            s +=f" and min. {dayweather['min_temp']}°C.\n"

        dispatcher.utter_message(text=f"Weather forecast for {loc} is:\n{s}")

        return [SlotSet("location", loc)]