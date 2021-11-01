[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
# Home Assistant Formula One API
Formula One API will be down for the remaining of the season while I work on a solution to update the data and prevent polling the API. The terms and condition of the API prevent polling.

Formula One API Integration Into Home Assistant: Bring live information the current season!

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

The sensor will return the following state attributes whether or not a game is in progress:

## Examples
Display info in the front end: [frontend.md](https://github.com/delzear/hass-formulaoneapi/blob/master/frontend.md)  

## Objectives Checklist
- [x] Consume Formula One Stats API locally with the least amount of resources possible.
- [ ] Pass information to Home Assistant as sensor data. (ex. Next game scheduled, live scores, goal description, etc.)
- [ ] Create a "live" event platform to use as a trigger for automations.
- [ ] Display the information in the front-end in its own Lovelace card.
- [ ] Add support for `HACS`.
## Resources
[The Home Assistant NHL API](https://github.com/JayBlackedOut/hass-nhlapi)
