[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
# Home Assistant Formula One API
Formula One API will be down for the remaining of the season while I work on a solution to update the data and prevent polling the API. The terms and condition of the API prevent polling.

Formula One API Integration Into Home Assistant: Bring live information the current season!

2022-10-05 - This sensor was seperated into 4 new sensors. Please check the frontend.md to correct the visuals

# 2023-01-11 - I will be shutting down the project on February 15th if nobody takes over. The cost of the server and the strain on it are too much.

<a href="https://www.buymeacoffee.com/delzear"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=delzear&button_colour=FFDD00&font_colour=000000&font_family=Arial&outline_colour=000000&coffee_colour=ffffff" /></a>

## Installation: Manual
1. Copy the `formulaone_api` folder to the `custom_components` folder in your Home Assistant configuration directory.
2. Restart Home Assistant to allow the required packages to be installed.
3. Add the following minimum code in your `configuration.yaml` file. See Configuration for more advanced options:
```
sensor:
  - platform: formulaone_api
```
4. Restart Home Assistant one final time.
## Installation: HACS
This method assumes you have HACS already installed.

Use this button:
 [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=delzear&repository=hass-formulaoneapi&category=integration)

_OR_ Manually
1. In the HACS Store, click `Custom Repository` from the top right menu.
2. Enter `delzear/hass-formulaoneapi` in the `URL` textbox and Integration in the `Category`.
3. Click `Install`
4. Restart Home Assistant to allow the required packages to be installed.
5. Add the following code in your `configuration.yaml` file. See Configuration for more advanced options:
```
sensor:
  - platform: formulaone_api
```
5. Restart Home Assistant one final time.
## Configuration
| key      | required | type    | usage                                                                                                                               |
|----------|----------|---------|-------------------------------------------------------------------------------------------------------------------------------------|
| platform | true     | string  | `formulaone_api`                                                                                                                    |

## Exposed Information
The sensor will expose 3 state attributes:

| state                  | description                                                                               |
|------------------------|-------------------------------------------------------------------------------------------|
| next_race              | The Next race of the current championship season                                          |
| races                  | Array of all the races of the current championship season                                 |
| drivers                | Sorted array of all drivers of the current championship season ordered by descending points |
| constructors           | Sorted array of all constructors of the current championship season ordered by descending points |
| last_result            | Sorted array of the last race result                                                      |

The sensor will return the following state attributes whether or not a game is in progress:

## Examples
Use the [FormulaOne-Card](https://github.com/marcokreeft87/formulaone-card) for displaying the information OR
use the markdown card: [frontend.md](https://github.com/delzear/hass-formulaoneapi/blob/master/frontend.md)

## Objectives Checklist
- [x] Consume Formula One Stats API locally with the least amount of resources possible.
- [ ] Pass information to Home Assistant as sensor data. (ex. Next game scheduled, live scores, goal description, etc.)
- [ ] Create a "live" event platform to use as a trigger for automations.
- [x] Display the information in the front-end in its own [Lovelace card](https://github.com/marcokreeft87/formulaone-card).
- [ ] Add support for `HACS`.
- [ ] Add notification service for qualifying, sprint and race

## Resources
[The Home Assistant NHL API](https://github.com/JayBlackedOut/hass-nhlapi)
