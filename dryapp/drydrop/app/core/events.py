import logging
from drydrop.app.models import Event
from google.appengine.api import users

def log_event(action, code = 0, email = None, info = None):
    if email is None:
        user = users.get_current_user()
        if user is None:
            email = None
        else:
            email = user.email()
    
    event = Event(author=email, action = action, code = code, info = info)
    event.save()