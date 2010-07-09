from __future__ import absolute_import

__version__ = '1.0'

from .client import StorymarketClient

class Storymarket(object):
    """
    Access to the Storymarket API.
    
    To use, first create an instance with your creds::
    
        >>> storymarket = Storymarket(API_KEY)
        
    Then call methods::
        
        >>> storymarket.categories.all()
        [...]
                
    """
    
    def __init__(self, key):
        self.client = StorymarketClient(key)