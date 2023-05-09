import time
import random


def retry_decorator(max_retries):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    result = function(*args, **kwargs)
                    return result
                except Exception as e:
                    if attempt == max_retries:
                        print(f"Failed after {max_retries} retries.")
                        raise e
                    else:
                        print(f"Attempt {attempt} failed, retrying...")
                        time.sleep(1)  # Wait before retrying
        return wrapper
    return decorator


@retry_decorator(max_retries=3)
def unreliable_function():
    if random.random() < 0.7:
        raise ValueError("Temporary issue occurred")
    else:
        return "Success"


result = unreliable_function()
print("Result:", result)
