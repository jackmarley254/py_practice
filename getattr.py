class NestedAccessor:
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        # Allow dict-style access
        return self._data[key]

    def __getattr__(self, name):
        # Allow attribute-style access
        try:
            value = self._data[name]
            # If the value is a dict, wrap it for further nested access
            if isinstance(value, dict):
                return NestedAccessor(value)
            return value
        except KeyError:
            raise AttributeError(f"'NestedAccessor' object has no attribute '{name}'")


# Example usage:
data = {
    'user': {
        'name': 'Alice',
        'details': {
            'age': 30,
            'city': 'Wonderland'
        }
    }
}

nested = NestedAccessor(data)

# Access using __getitem__
print(nested['user']['details']['city'])  # Output: Wonderland

# Access using __getattr__
print(nested.user.details.city) # Output: Wonderland
