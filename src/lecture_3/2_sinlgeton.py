"""
In this example, the Logger class implements the Singleton pattern by overriding the __new__ method.
When a new Logger object is created, it checks if the _instance attribute is None. If it is, the object is
created and assigned to the _instance attribute. If an instance already exists, the __new__ method returns
the existing instance instead of creating a new one.

The Logger class provides two methods: log to add log messages to the internal logs list, and show_logs to display
all the log messages. The example demonstrates that when creating two Logger objects, logger1 and logger2,
they both refer to the same instance of the Logger class, ensuring that log messages are managed centrally
by a single object.

"""
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def log(self, message):
        self.logs.append(message)

    def show_logs(self):
        for log in self.logs:
            print(log)


# Test the Logger Singleton
logger1 = Logger()
logger1.log("This is the first log message.")

logger2 = Logger()
logger2.log("This is the second log message.")

# Both logger1 and logger2 refer to the same Logger instance
logger1.show_logs()  # Outputs both log messages

# Check if both loggers are the same instance
print(logger1 is logger2)  # Output: True
