import re
from django.core.exceptions import ValidationError

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs) # noqa
        return cls._instance


class CustomPasswordValidator(Singleton):
    def __init__(self, regex=None, message=None):
        self.regex = regex or r'^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{6,})\S$'
        self.message = message or 'Password must contain at least 6 characters, including one uppercase letter, one lowercase letter, and one number.'

    def validate(self, password):
        if not re.match(self.regex, password):
            raise ValidationError(self.message)

    def get_help_text(self):
        return self.message
