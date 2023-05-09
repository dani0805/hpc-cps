"""
In this example, we create an EventMeta metaclass that registers event handlers in the _event_handlers dictionary.
The EventSystem class uses the EventMeta metaclass, which provides the on method for registering event handlers and
a trigger_event method for triggering events.

The create_event_handler_closure function creates closures with the event_name parameter, which will be printed when
the event handler is called. In the main function, we create two closures for different event names, register them
as event handlers, and then trigger the events to demonstrate how the event-driven system works with closures.

This example demonstrates the use of metaclasses for dynamically registering event handlers, dunder methods for
creating the metaclass and managing the event handlers dictionary, and closures for providing context when
events are triggered.

"""


class EventMeta(type):
    def __new__(cls, name, bases, dct):
        dct["_event_handlers"] = {"event_1": []}
        return super().__new__(cls, name, bases, dct)

    def on(cls, event_name, handler):
        cls._event_handlers.setdefault(event_name, []).append(handler)


class EventSystem(metaclass=EventMeta):
    @classmethod
    def trigger_event(cls, event_name, *args, **kwargs):
        handlers = cls._event_handlers.get(event_name, [])
        for handler in handlers:
            handler(*args, **kwargs)


def create_event_handler_closure(event_name):
    def event_handler(*args, **kwargs):
        print(f"Event '{event_name}' triggered with args: {args}, kwargs: {kwargs}")

    return event_handler


def main():
    # Register event handlers using closures
    event_handler_1 = create_event_handler_closure("event_1")
    event_handler_2 = create_event_handler_closure("event_2")

    EventSystem.on("event_1", event_handler_1)
    EventSystem.on("event_2", event_handler_2)

    # Trigger events
    EventSystem.trigger_event("event_1", 1, 2, 3, key="value")
    EventSystem.trigger_event("event_2", 4, 5, 6, another_key="another_value")


if __name__ == "__main__":
    main()
