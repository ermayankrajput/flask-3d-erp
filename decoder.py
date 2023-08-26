from functools import wraps

# Example roles
USER_ROLE = 'User'
ADMIN_ROLE = 'Admin'

def role_accepted(user,accepted_roles):
    if user.role_id in accepted_roles:
        return True
    return False

    # def decorator(func):
    #     @wraps(func)
    #     def wrapper(*args, **kwargs):  
    #         if user.role_id in accepted_roles:
    #             return func(*args, **kwargs)
    #         else:
    #             return "false" 
    #     return wrapper
    # return decorator
