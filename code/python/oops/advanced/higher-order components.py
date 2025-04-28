def with_logging(component):
    def logged_component(*args, **kwargs):
        print(f"Calling : {component.__name__}")
        result = component(*args, **kwargs)
        print(f"component {component.__name__} completed. Result: {result}")
        return result
    return logged_component

@with_logging
def user_profile(user_id):
    return f"User profile for ID: {user_id}"

@with_logging
def calculate_sum(a, b):
    return a + b

print(user_profile(123))
# Calling : user_profile
# component user_profile completed. Result: User profile for ID: 123
# User profile for ID: 123
print(calculate_sum(5,3))
# Calling : calculate_sum
# component calculate_sum completed. Result: 8
# 8