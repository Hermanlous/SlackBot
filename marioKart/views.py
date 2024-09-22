from django.http import JsonResponse
from marioKart.bot import notify_user_on_slack

# View for å teste Slackbot
def test_slackbot_view(request):
    email = request.GET.get('email', 'herman.lous@startntnu.no')  
    message = request.GET.get('message', 'Hei fra Slackbot!')
    
    # Kall funksjonen som sender meldinger til Slack
    notify_user_on_slack(email, message)
    
    # Returner en bekreftelse til nettleseren
    return JsonResponse({'message': f'Slack-melding sendt til {email} med innhold: {message}'})