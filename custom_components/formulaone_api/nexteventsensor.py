
from custom_components.formulaone_api.const import FIRST_PRACTICE, QUALIFYING, RACE, SECOND_PRACTICE, SPRINT, THIRD_PRACTICE
from custom_components.formulaone_api.formulaonesensor import FormulaOneSensor
from custom_components.formulaone_api.f1 import F1
from datetime import datetime as dt

class NextEventSensor(FormulaOneSensor):
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
        next_race = self.get_next_race()

        first_practice_date = dt.strptime(next_race[FIRST_PRACTICE]['date'] + " " + next_race[FIRST_PRACTICE]['time'], '%Y-%m-%d %H:%M')
        second_practice_date = dt.strptime(next_race[SECOND_PRACTICE]['date']+ " " + next_race[SECOND_PRACTICE]['time'], '%Y-%m-%d %H:%M')
        third_practice_date = dt.strptime(next_race[THIRD_PRACTICE]['date']+ " " + next_race[THIRD_PRACTICE]['time'], '%Y-%m-%d %H:%M')
        qualifying_date = dt.strptime(next_race[QUALIFYING]['date']+ " " + next_race[QUALIFYING]['time'], '%Y-%m-%d %H:%M')
        #sprint_date = dt.strptime(next_race[SPRINT]['date']+ " " + next_race[SPRINT]['time'], '%Y-%m-%d %H:%M')
        race_date = dt.strptime(next_race['date']+ " " + next_race['time'], '%Y-%m-%d %H:%M')

        dates = {FIRST_PRACTICE : first_practice_date, SECOND_PRACTICE: second_practice_date, THIRD_PRACTICE: third_practice_date, 
        QUALIFYING : qualifying_date,  RACE:  race_date} #SPRINT : sprint_date,

        for key in dates:
            if dates[key] > dt.now():
                self.state = key
                break
        
        #nearest_event = self.nearest(dates, dt.now())

        #self.state = nearest_event.key

        # if next_race == None:
        #     self._state = 'None'
        # elif dt.strptime(next_race['date'], '%Y-%m-%d') == dt.today():
        #     self._state = 'Race'
        # elif dt.strptime(next_race['Qualifying']['date'], '%Y-%m-%d') == dt.today():
        #     self._state = 'Qualifying'

        #TODO return first upcoming event

        return self._state

    def nearest(items, pivot):
        return min(items, key=lambda x: abs(x.key - pivot))