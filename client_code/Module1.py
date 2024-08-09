import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
# This is a module.
# You can define variables and functions here, and use them from any form. For example, in a top-level form:
#
#    from . import Module1
#
#    Module1.say_hello(
@anvil.server.callable
def add_feedback(Name, Email, Feedback):
  app.tables.feedback.add_row(
    name=Name,
    email=Email,
    feedback=Feedback,
    created_on= datetime.now()
  
  )