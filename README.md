# Distance calculator API

## 🔧 Installation
Create a virtual environment and install the dependencies
```
poetry shell
```

Build the Docker Image
```
docker build -t distance_calculator_app .
```

## 🔌 Run (local)
Run the Docker container
```
docker run -p 8080:8080 distance_calculator_app
```

Then check [Local docs](http://127.0.0.1:8080/docs)

## 🧪 Tests
Run tests with coverage
```
python -m pytest -vx --cov=services --cov-report term-missing --cov-fail-under=95
```

## 🧩 Testing the functionalities
To test, we can go to the /docs page and enter the source and destination addresses, the mode of transport and the units of measurement in the fields. 

Examples of origin and destination could be:

* Origin: 1600 Amphitheatre Parkway, Mountain View, CA
* Destination: 1 Infinite Loop, Cupertino, CA


* Origin: Eiffel Tower, Paris, France
* Destination: Colosseum, Rome, Italy


* Origin: Madrid, Spain
* Destination: Barcelona, Spain

We can also indicate these parameters through coordinates.

As we can see, for the parameters mode and units there is a drop-down combo with the options to choose from. 
In the case of units we have two options:
* Metric: This will return the distance in kilometres and metres.
* Imperial: This will return the distance in miles and feet.
