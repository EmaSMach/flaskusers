# --*-- encoding: utf-8 --*--
from __future__ import unicode_literals, print_function
from utils.validators import validate_email, validate_length


class BaseUser(object):
    """
    A base class for User.
    """
    users = {}
    fields = ('user_id', 'first_name', 'last_name', 'email', 'active', 'username', 
              'age', 'country', 'state', 'city', 'address', 'zip_code')

    def __init__(self, user_id, first_name, last_name, email, active, username, age=None, country=None,
                 state=None, city=None, address=None, zip_code=None, *args, **kwargs):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.active = active
        self.age = age
        self.username = username
        self.country = country
        self.state = state
        self.city = city
        self.address = address
        self.zip_code = zip_code

    def validate_fields(self):
        """
        Validates all the fields.
        """
        pass

    def save(self):
        """
        Saves the user.
        """
        pass

    def get_user(self, user_id):
        """
        Get the user with the given user_id.
        """
        pass

    def to_dict(self):
        """
        Put the data of the user into a dict and return it.
        """
        pass

    @classmethod
    def from_dict(cls, dictionary):
        """
        Creates a user object with the passed dictionary.
        """
        pass
    
    def to_users(self):
        """
        Adds the current user to the dict of users.
        """
        pass


class User(BaseUser):
    """
    A class to represent a User.
    """
    
    def validate(self):
        """
        Validates the type of the fields.
        """
        try:
            assert type(self.user_id) == int
            assert type(self.first_name) in (str, unicode)
            assert type(self.last_name) in (str, unicode)
            assert validate_email(self.email) is True
            assert self.active in (True, False)
            assert type(self.username) in (str, unicode)
            if self.country:
                assert type(self.country) in (str, unicode)
            if self.state:
                assert type(self.state) in (str, unicode)
            if self.city:
                assert type(self.city) in (str, unicode)
            if self.address:
                assert type(self.address) in (str, unicode)
            if self.zip_code:
                assert type(self.zip_code) == int
            return True
        except AssertionError:
            return False
        
    @classmethod
    def from_dict(cls, dictionary):
        try:
            return cls(user_id=dictionary['user_id'],
                       first_name=dictionary['first_name'],
                       last_name=dictionary['last_name'],
                       email=dictionary['email'],
                       active=dictionary['active'],
                       username=dictionary['username'],
                       country=dictionary['country'],
                       state=dictionary['state'],
                       city=dictionary['city'],
                       address=dictionary['address'],
                       zip_code=dictionary['zip_code'])
        except AssertionError:
            return None
        except AttributeError:
            return None
        except KeyError:
            return None
    
    def to_dict(self):
        return self.__dict__
    
    def to_users(self):
        """
        Adds the current user to the dict of users.
        """
        self.users[self.user_id] = self.to_dict()

