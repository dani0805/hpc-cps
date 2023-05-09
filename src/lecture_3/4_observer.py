"""
In this example, we define an abstract Observer class and an abstract Subject class.
The WeatherData class implements the Subject interface, maintaining a list of observers and providing methods to
register, remove, and notify observers.

The CurrentConditionsDisplay class is a concrete Observer class that implements the update method. When notified of a
change in the weather data, it updates its state and displays the current conditions.

The WeatherData instance is created, and then an observer, CurrentConditionsDisplay, is registered with it.
The weather data is then updated twice, which causes the registered observers to be notified and update their display
accordingly.

This pattern is useful when you have multiple objects that depend on the state of another object and need to be updated
when that object's state changes. It promotes loose coupling between the subject and its observers, making it easier to
add or modify observers without changing the subject's code.
"""
from abc import ABC, abstractmethod

# Define the abstract Observer class
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

# Define the abstract Subject class
class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Define the WeatherData class (Subject)
class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()

# Define a concrete Observer class (DisplayElement)
class CurrentConditionsDisplay(Observer):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}°F and {self.humidity}% humidity")

# Test the Observer pattern
weather_data = WeatherData()
current_conditions_display = CurrentConditionsDisplay(weather_data)

weather_data.set_measurements(80, 65, 30.4)
weather_data.set_measurements(82, 70, 29.2)
