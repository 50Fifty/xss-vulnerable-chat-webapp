from expiring_dict import ExpiringDict
from typing import Union


class User():

    __users = []
    __active_users = ExpiringDict(900) # key: token, value: user, expires in 15 minutes

    def __init__(self, username: str, password: str):
        """
        Creates a new user, with the given username and password, and adds it to the list of users
        :param username: The username of the user
        :param password: The password of the user
        :return: None
        """
        self.__id = len(User.__users)
        self.__username = username
        self.__password = password

        User.__users.append(self)

    @staticmethod
    def get(user_id: int) -> Union["User", None]:
        """
        Returns the user with the given id
        :param user_id: The id of the user
        :return: The user with the given id
        """
        for user in User.__users:
            if user.username == user_id:
                return user
            
        return None
    
    @staticmethod
    def get_by_username(username: str):
        """
        Returns the user with the given username
        :param username: The username of the user
        :return: The user with the given username
        """
        for user in User.__users:
            if user.username == username:
                return user
            
        return None
    
    @staticmethod
    def get_by_token(token: Union[str, None]) -> Union["User", None]:
        """
        Returns the user with the given token
        :param token: The token of the user
        :return: The user with the given token
        """
        return User.__active_users.get(token) if token is not None else None
    
    @staticmethod
    def get_all():
        """
        Returns all users
        :return: All users
        """
        return User.__users
    
    @property
    def id(self):
        """
        Returns the id of the user
        :return: The id of the user
        """
        return self.__id
    
    @property
    def username(self):
        """
        Returns the username of the user
        :return: The username of the user
        """
        return self.__username
    
    @property
    def password(self):
        """
        Returns the password of the user
        :return: The password of the user
        """
        return self.__password

    def add_active_user(self, token: str):
        """
        Adds the user to the list of active users
        :param token: The token of the user
        :return: None
        """
        User.__active_users[token] = self

    def is_authenticated(self):
        """
        Returns true if the user is authenticated
        :return: True if the user is authenticated
        """
        return True
    
    def is_active(self):
        """
        Returns true if the user is active
        :return: True if the user is active
        """
        return True
    
    def is_anonymous(self):
        """
        Returns true if the user is anonymous
        :return: True if the user is anonymous
        """
        return False
    
    def get_id(self):
        """
        Returns the id of the user
        :return: The id of the user
        """
        return self.id
    
    def __str__(self):
        """
        Returns a string representation of the user
        :return: A string representation of the user
        """
        return "User: " + self.username
    
    def __repr__(self):
        """
        Returns a string representation of the user
        :return: A string representation of the user
        """
        return self.__str__()
    
    def __eq__(self, other):
        """
        Returns true if the user is equal to the other user
        :param other: The other user
        :return: True if the user is equal to the other user
        """
        if not isinstance(other, User):
            raise TypeError("Cannot compare User to " + str(type(other)))
        
        return self.id == other.id
    
    def __hash__(self):
        """
        Returns the hash of the user
        :return: The hash of the user
        """
        return hash(self.id)
    
    def __ne__(self, other):
        """
        Returns true if the user is not equal to the other user
        :param other: The other user
        :return: True if the user is not equal to the other user
        """
        if not isinstance(other, User):
            raise TypeError("Cannot compare User to " + str(type(other)))
        
        return not self.__eq__(other)


User("admin", "admin")
User("sean", "password123")
User("attacker", "attacker")