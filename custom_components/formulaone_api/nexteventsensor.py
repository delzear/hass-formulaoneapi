
from custom_components.formulaone_api.formulaonesensor import FormulaOneSensor
from custom_components.formulaone_api.f1 import F1
from datetime import datetime as dt

class LastResultSensor(FormulaOneSensor):
    """Representation of a Formula One sensor."""

    def __init__(self, name, scan_interval, hass):
        """Initialize Formula One sensor."""
        FormulaOneSensor.__init__(self, name + " Next Event", scan_interval, hass)
        self.hass = hass
        self.basename = name

    def get_next_race(self):
        
        # Get data from races sensor
        #races = self.hass.states.get("sensor." + self.basename.replace(" ", "_").lower() + "_races")

        # # # Merge all attributes to a single dict.
        # all_attr = {
        #     'last_update': now,
        #     'data': races['MRData']['RaceTable']['Races'][0]
        # }

        return self.hass.states.get("sensor." + self.basename.replace(" ", "_").lower() + "_races").attributes['next_race']

    def set_state(self):
        """Set sensor state to race state and set polling interval."""
        next_race = self.get_race_data()

        if next_race == None:
            self._state = 'None'
        elif dt.strptime(next_race['date'], '%Y-%m-%d') == dt.today():
            self._state = 'Race'
        elif dt.strptime(next_race['Qualifying']['date'], '%Y-%m-%d') == dt.today():
            self._state = 'Qualifying'

        #TODO return first upcoming event

        return self._state