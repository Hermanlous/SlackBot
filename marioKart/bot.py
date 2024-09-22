import os
import django
import sys

#legger til rotmappen til prosjektet i sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marioKart.settings')
django.setup()

from models import Users

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from decouple import config


SLACK_BOT_TOKEN = config('SLACK_BOT_TOKEN')

client = WebClient(token=SLACK_BOT_TOKEN)

def send_dm(user_id, message):
    try: 
        response = client.chat_postMessage(
            channel=user_id,
            text=message)
        print(response)
    except SlackApiError as e:
        print(f"Error: {e}")

def get_user_by_email(email):
    try:
        user = Users.objects.get(email = email)
        return user
    except Users.DoesNotExist:
        print("User not found")
        return None

def get_slack_user_id_by_email(email):
    try:
        response = client.users_lookupByEmail(email=email)
        return response['user']['id']
    except:
        print("User not found")
        return None

def notify_user_on_slack(email, message):
    user = get_user_by_email(email)
    if user:
        slack_id = get_slack_user_id_by_email(user.email)
        if slack_id:
            send_dm(slack_id, message)
        else:
            print("User not found in Slack")
    else:
        print("User not found in database")

    
   