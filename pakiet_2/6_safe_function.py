def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            result =func(*args, **kwargs)
            return result
        except Exception as e:
            print(f'An error occured: {e}')
            return None
    return wrapper

@safe_function
def dzielenie(x, y):
    return x//y

print(dzielenie(2,2))
print(dzielenie(10,0))