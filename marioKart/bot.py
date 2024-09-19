import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from decouple import config
from models import Users

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
        user = Users.objects.get(mail = email)
        return user
    except Users.DoesNotExist:
        print("User not found")
        return None

def get_slack_user_id_by_email(email):
    user = get_user_by_email(email)
    try:
        response = client.users.lookupByEmail(user.email)
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

    
   