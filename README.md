<h1>Smash Tournament Sorter Micro-Service</h1>

<h2>Requesting Data</h2>
To programmatically request data, you will be sending an array of JSON objects representing a particular SmashBro tournament being hosted to the ZeroMQ server that will be hosting the micro-service. The last JSON           bject in the array should hold the user selected filters based on the start date, end date, and game type. As seen below:
  
```
tours = [
  {
      "game" : "melee",
      "startDate": "12-01-2024",
      "endDate": "12-04-2024",
      "name": "Summit 2024"
  },
  {
      "game": "ultimate",
      "startDate": "11-01-2024",
      "endDate": "11-03-2024",
      "name": "Vibes Smash 2024"
  },
  {
      "game": "both",
      "startDate": "09-01-2024",
      "endDate": "09-03-2024",
      "name": "Viva Smash 2024"
  },
  {
      "startFilter": None,
      "endFilter": None,
      "gameFilter": None,
  }
]
socket.send_json(tours)
```

<h2>Recieving Data</h2>
To programmatically receive data from the micro-service, you will simply utilize the ZeroMQ receive JSON method. As seen below:

```
sorted_tours = socket.recv_json()
```
<h2>ULM Diagram</h2>
<img width="468" alt="image" src="https://github.com/user-attachments/assets/f6e26470-85d9-4894-8eef-15a8fb2021a9">

<h2>Mitigation Plan</h2>
<ol>
  <li>Elijah Davis</li>
  <li>This Micro-service is completed</li>
  <li>N/a, this microservice is completed</li>
  <li>My teammate should run this locally on their computer </li>
  <li>If my teammate is unable to access my microservice, they should contact me via the Discord channel we set up for their personal project. I work 4x10’s Mon-Fri with my day off being Wednesday. I am available most workdays after 5:30 PM CT with being pretty flexible my day off and the weekends.</li>
  <li>If my teammate is unable to access the service, I would prefer my teammate to contact my no later than the following weekday this microservice is upload and a confirmation message has been relayed.</li>
  <li>The only thing I would relay is, as of now there is no way to quit the program by sending a particular message to the ZeroMQ server. We can discuss if that is something you want to be added. Additionally, this program is written in Python. Lastly, it is import you send the JSON object with the respected key value pairs as seen below. The date should be formatted as such, MM-DD-YYYY.  The last JSON object in the array should also hold the filters set by a user with their respective key value pair:</li>
</ol>

```
variable = [
    {
        "game": "both, melee, or ultimate",
        "startDate": "MM-DD-YYYY",
        "endDate": "MM-DD-YYYY",
        "name": "Tournament Name"
    },
    {
        "startFilter": "filter or None",
        "endFilter": "filter or None",
        "gameFilter": "filter or None",
    }
]
```




