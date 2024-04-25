# Inside your Django app directory, create a new folder called 'management' if it doesn't exist.
# Inside 'management', create another folder called 'commands'.
# Inside 'commands', create a Python file named 'custom_command.py'.

# custom_command.py

from django.core.management.base import BaseCommand
# from myapp.models import MyModel  # Import your models here
from django.utils import timezone
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Sending notification to connected users . There are 4 users connected right now which are 

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **options):
        # Your logic goes here
        # For example, let's say you want to print all instances of MyModel
        # my_model_instances = MyModel.objects.all()
        channel_layer = get_channel_layer()
        # for instance in my_model_instances:
        #     self.stdout.write(self.style.SUCCESS(instance.__str__()))  # Print each instance
        print("hello")
        async_to_sync(
            channel_layer.group_send)("chat_lobby",{
                "type": "chat_message",
                "message": "Demo notification"
            }
        )