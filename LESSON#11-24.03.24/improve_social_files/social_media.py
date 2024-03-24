from user import User

class SocialMediaPlatform:
    """
        ~ Represents the core of the social media platform (managing the users).
        Attributes:
            users (dict): A dictionary of users in the platform.
    """
    def __init__(self):
        #O(1)
        """
            Initializes a new platform object.
            Args:
                users (dict): A dictionary of users in the platform.
        """
        self.users = {}

    def register_user(self, username):
        #O(1)
        """
            Registers a new user.
            Args:
                username (str): The username of the user.
        """
        
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        if not self._is_username_taken(username):
            user = User(username)
            self.users[username] = user
        else:
            raise ValueError("username is already taken")

    def _is_username_taken(self, username):
        #PREV: O(n)
        #NEW:  O(1)
        """
            Checks if a username is already taken.
            Args:
                username (str): The username to check.
            Returns:
                bool: True if the username is taken, False otherwise.
        """
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        if self.users[username]:
            return True
        return False

    def get_user_by_username(self, username):
        #PREV: O(n)
        #NEW:  O(1)
        """
            Gets a user by their username.
            Args:
                username (str): The username.
            Returns:
                User: The user instance.
        """
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        return self.users[username]

    def generate_timeline(self, username):
        #PREV: O(n*m)
        #NEW:  O(n)
        """
            Generates a timeline for a user.
            Args:
                username (str): The username of the user.
            Returns:
                list: A list of messages in the user's timeline.
        """
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        user = self.get_user_by_username(username)
        if not user:
            return []

        timeline = []
        for followed_user in user.following:
            post={'username': followed_user, 'message': user.posts[followed_user]}
            timeline.append(post)
        return timeline
