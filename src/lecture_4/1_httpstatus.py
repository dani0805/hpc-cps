class HttpStatus:
    OK = 200
    BAD_REQUEST = 400
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500

    @classmethod
    def __class_getitem__(cls, key):
        if not isinstance(key, int):
            raise TypeError("Index must be an integer")
        for attr in dir(cls):
            value = getattr(cls, attr)
            if value == key:
                return attr
        raise IndexError("HTTP status code not found")

# Usage
status1 = HttpStatus[200]
print(status1)  # Output: OK

status2 = HttpStatus[404]
print(status2)  # Output: NOT_FOUND

status3 = HttpStatus[500]
print(status3)  # Output: INTERNAL_SERVER_ERROR
