class InvalidAgeError(Exception):
    """
    Raised when the provided age does not meet the minimum age requirement.
    """
    pass

def check_age(age):
    try:
        if age < 20:
            raise InvalidAgeError(f"Age {age} is below the required minimum.")
        
        print(f"Age {age} meets the eligibility criteria.")
    except InvalidAgeError as e:
        print("InvalidAgeError:", e)

check_age(30)

 
