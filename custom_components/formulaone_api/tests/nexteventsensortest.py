import json
import unittest
from unittest.mock import MagicMock
from custom_components.formulaone_api.nexteventsensor import NextEventSensor as Sut

class NextEventSensorTestMethods(unittest.TestCase):
    
    sensor = Sut()

    def test_set_state(self):
        # Arrange

        file = open('testdata/schedule.json')
        data = json.load(file)
        file.close()
        print(data['MRData']['RaceTable']['Races'][0])
        self.sensor.get_next_race = MagicMock(return_value=data['MRData']['RaceTable']['Races'][0])

        # Act
        self.sensor.set_state()

        # Assert

# run the test
if __name__ == '__main__':
    unittest.main()