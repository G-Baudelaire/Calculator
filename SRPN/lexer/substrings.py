class Substring():
    def __str__(self):
        return self._string

    def __int__(self):
        return self._string_type

    def __init__(self, string, string_type):
        self._string = string
        self._string_type = string_type

    def get_string(self):
        return self._string

    def get_string_type(self):
        return self._string_type
