def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Your First Name', 'Your Last Name',
                             location='Your Location',
                             occupation='Your Occupation',
                             hobbies='Your Hobbies')
print(user_profile)
