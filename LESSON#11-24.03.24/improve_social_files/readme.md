# Social Media Platform

## Files:

1.	`social_media.py`: Manages the core platform logic.

2.	`user.py`: Represents an individual user.

## Workflow:

1.	User Registration (social_media.py):

    o	Start by calling `register_user(username)` on a `SocialMediaPlatform` instance.

    o   username validation for both type and value.

    o   if valid a new user object is created and added to the platform's user dictionary.

2.	Following Users (user.py):

    o	Users follow others using `follow(other_user)` on a `User` instance.

    o	Validation occurs for the type.

    o   Adding the user to the following list.

3.	Posting Messages (user.py):

    o	Users post messages using `post_message(message)` on a `User` instance.

    o	A string validation occurs for the message.

    o	if valid, the message saved in posts dict.

4.	Generating Timeline (social_media.py):

    o	User timelines are retrieved using `generate_timeline(username)` on a `SocialMediaPlatform` instance.

    o	Username validation confirms it's a string.

    o	The user's object is retrieved using `get_user_by_username`. 

    o	An empty timeline is returned if the user doesn't exist.

    o	Messages from followed users are retrieved using a loop.

    o	Each message is reformatted as the code was formating it before.

