class User:
    """
        ~ Represents a user in the social media app.
        Attributes:
            username (str): The username of the user.
            following (list): A list of other users that this user is following.
    """
    def __init__(self, username):
        #O(1)
        """
            Initializes a new User object.
            Args:
                username (str): The username of the user.
        """
        self.username = username
        self.following = []

    def follow(self, other_user):
        #PREV: O(n)
        #NEW:  O(1)
        """
            Follows another user.
            Args:
                other_user (User): The user to follow.
        """
        if not isinstance(other_user, User):
            raise TypeError("other_user is not a User object")
        if other_user not in self.following:
            self.following.append(other_user)

    def post_message(self, message):
        #O(1)
        """
            Posts a message to the social media app.
            Args:
                message (str): The message to post.
        """
        if not isinstance(message, str):
            raise TypeError("message must be a string")
        if self.username not in posts:
            posts[self.username] = []
        posts[self.username].append(message)


# Assume posts are stored in a global list
posts = {}