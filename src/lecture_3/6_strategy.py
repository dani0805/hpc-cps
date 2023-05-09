"""
In this example, we define a TransportationStrategy interface with an abstract method calculate_cost.
We then implement three concrete strategies (CarStrategy, TrainStrategy, and BicycleStrategy) that calculate the cost
of a trip using different modes of transportation.

The TravelPlanner class serves as the context, and it delegates the cost calculation to the strategy object it holds.
The strategy can be changed at runtime using the set_strategy method.

In the client code, we create a TravelPlanner instance with an initial strategy, and then change the strategy using
set_strategy to demonstrate how the strategy pattern allows for interchangeable behavior without modifying the
TravelPlanner class.

"""

from abc import ABC, abstractmethod

# Define the strategy interface
class TransportationStrategy(ABC):

    @abstractmethod
    def calculate_cost(self, distance: float) -> float:
        pass

# Implement concrete strategies
class CarStrategy(TransportationStrategy):

    def calculate_cost(self, distance: float) -> float:
        cost_per_mile = 0.50  # Example cost per mile
        return distance * cost_per_mile

class TrainStrategy(TransportationStrategy):

    def calculate_cost(self, distance: float) -> float:
        flat_rate = 30  # Example flat rate
        return flat_rate

class BicycleStrategy(TransportationStrategy):

    def calculate_cost(self, distance: float) -> float:
        return 0  # Free!

# Context class
class TravelPlanner:

    def __init__(self, strategy: TransportationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: TransportationStrategy):
        self._strategy = strategy

    def calculate_trip_cost(self, distance: float) -> float:
        return self._strategy.calculate_cost(distance)

# Client code
trip_distance = 50  # miles

planner = TravelPlanner(CarStrategy())
print(f"Car: ${planner.calculate_trip_cost(trip_distance):.2f}")

planner.set_strategy(TrainStrategy())
print(f"Train: ${planner.calculate_trip_cost(trip_distance):.2f}")

planner.set_strategy(BicycleStrategy())
print(f"Bicycle: ${planner.calculate_trip_cost(trip_distance):.2f}")
