# Frontend Example
The goal is to eventually have a custom lovelace card to display the sensor's information. In the meantime, a makeshift display can be created using template Markdowns.  The font is the Official Formula One and is not the default. Follow the steps below to get a result similar to this:

To display the next race:

![Next Race](./next-race.png) 
```
type: markdown
content: >-
  {% set nr = states.sensor.formula_one_sensor.attributes.next_race  %} {% if
  not(nr == None) %}  <h2><img height="25"
  src="https://www.countries-ofthe-world.com/flags-normal/flag-of-{{nr.Circuit.Location.country | replace(" ","-")}}.png">&nbsp; 
  {{ nr.round }} :  {{ nr.raceName }}</h2>

  <small>Local time : {{ as_timestamp(nr.date + ' ' + nr.time) |
  timestamp_custom("%H:%M on %y-%m-%D ") }}</small>

  <a target="_new" href="{{nr.Circuit.url}}">
    <img width="100%" src="https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/{{nr.Circuit.Location.country | replace(" ","_")}}_Circuit.png.transform/7col/image.png">
  </a> <br> 

  Season: {{nr.season}}<br>

  Race: {{nr.round}}<br>

  Race name : {{nr.raceName}}<br>

  Circuit name : {{nr.Circuit.circuitName}}<br>

  Location: {{nr.Circuit.Location.country}}<br>

  Date : {{nr.date}}<br>

  Time : {{nr.time}}<br>  {% endif %}
title: Next race
card_mod:
  style:
    ha-markdown$: |
      * {
        font-family: FormulaOne, "Titillium Web";
      }
```

To display the Driver standings:

![Driver standings](./driver_standings.png)
```
type: markdown
content: |-
  <table>
    <thead>
      <tr>
        <th>&nbsp;</th>
        <th colspan="2">Drivers</th>
      <th class="center"> Car nr</th>
       <th class="center">Pts</th>
      <th class="center">Wins</th>
      </tr>
    </thead>
    <tbody>
  {% for driver in states.sensor.formula_one_sensor.attributes.drivers %} <tr>
          <td>{{driver.position}}</td>
          <td>{{driver.Driver.code}}</td>
          <td>{{driver.Driver.givenName }} {{driver.Driver.familyName}}</td>
         <td> {{driver.Driver.permanentNumber}}</td>
         <td>{{driver.points}}</td>
        <td><center>{{driver.wins}}</center></td>
      </tr>
  {% endfor %}
    </tbody>
  </table>
card_mod:
  style:
    ha-markdown$: |
      table {
        width: 100%;
        border-spacing: 0;
        border-collapse: separate;
      }
      th {
        color: white;
        background: black;
      }
      tr:nth-child(even) {
        background-color: #dddddd;
        color: rgb(33,33,33);
      }
      td:nth-child(1) {
        width: 50px;
        text-align: center;
      }
      td:nth-child(2) {
        width: 50px;
        text-align: center;
      }
      td:nth-child(4) {
        width: 60px;
        text-align: center;
      }

```

To display the Constructor standings:

![Constructor standings](./constructor_standings.png)
```
type: markdown
content: >-
  <table>
    <thead>
      <tr>
        <th>&nbsp;</th>
        <th>Constructor</th>
        <th class="center">Pts</th>
        <th class="center">Wins</th>
      </tr>
    </thead>
    <tbody>
  {% for driver in states.sensor.formula_one_sensor.attributes.constructors %}
  <tr>
          <td>{{driver.position}}</td>
          <td>{{driver.Constructor.name }}</td>
          <td>{{driver.points}}</td>
          <td><center>{{driver.wins}}</center></td>
      </tr>
  {% endfor %}
    </tbody>
  </table>
card_mod:
  style:
    ha-markdown$: |
      table {
        width: 100%;
        border-spacing: 0;
        border-collapse: separate;
      }
      th {
        color: white;
        background: black;
      }
      tr:nth-child(even) {
        background-color: #dddddd;;
        color: rgb(33,33,33);
      }
      td:nth-child(1) {
        width: 50px;
        text-align: center;
      }
      td:nth-child(2) {
        text-align: left;
      }
      td:nth-child(3) {
        width: 60px;
        text-align: center;
      }

```
To display the Race agenda:

![race agenda](./race-agenda.png)


```
type: markdown
content: |-
  <table>
    <thead>
      <tr>
        <th>&nbsp;</th>
        <th>Race</th>
        <th class="center">Date</th>
       <th class="center">Time</th>
      </tr>
    </thead>
    <tbody>
  {% for races in states.sensor.formula_one_sensor.attributes.races %} <tr>
          <td>{{races.round}}</td>
          <td>{{races.raceName}}</td>
          <td>{{races.date}}</td>
          <td>{{races.time}}</td>
      </tr>
  {% endfor %}
    </tbody>
  </table>
card_mod:
  style:
    ha-markdown$: |
      table {
        width: 100%;
        border-spacing: 0;
        border-collapse: separate;
      }
      th {
        color: white;
        background: black;
      }
      tr:nth-child(even) {
        background-color: #dddddd;;
        color: rgb(33,33,33);
      }
      td:nth-child(1) {
        width: 50px;
        text-align: center;
      }
      td:nth-child(2) {
        text-align: left;
      }
      td:nth-child(3) {
        width: 60px;
        text-align: center;
      }

```
