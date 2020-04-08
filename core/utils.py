"""
Useful function across the project.
Can be some str transformation, common regex, etc
"""


def slug(s: str):
    """
    Slugify a string s

    Replace spaces by minuses and lower the string
    """
    return s.replace(" ", "-").lower()
