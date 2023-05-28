from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.conf import settings
from django.urls import reverse


class GoogleCalendarInitView(View):
    def get(self, request):
        try:
            # Initialize the OAuth flow using client secrets file
            flow = InstalledAppFlow.from_client_secrets_file(
                settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
                scopes=['https://www.googleapis.com/auth/calendar.readonly'],
                redirect_uri=request.build_absolute_uri(reverse('google-calendar-redirect'))
            )

            # Get the authorization URL and state
            authorization_url, state = flow.authorization_url(
                access_type='offline',
                include_granted_scopes='true'
            )

            # Redirect the user to the authorization URL
            return HttpResponseRedirect(authorization_url)
        except Exception as e:
            # Handle the exception, e.g., log the error or show an error message to the user
            return HttpResponse(f'An error occurred during authorization: {e}')


class GoogleCalendarRedirectView(View):
    def get(self, request):
        try:
            # Get the authorization code from the request parameters
            code = request.GET.get('code')

            # Initialize the OAuth flow using client secrets file
            flow = InstalledAppFlow.from_client_secrets_file(
                settings.GOOGLE_OAUTH2_CLIENT_SECRETS_JSON,
                scopes=['https://www.googleapis.com/auth/calendar.readonly'],
                redirect_uri=request.build_absolute_uri(reverse('google-calendar-redirect'))
            )

            # Fetch the token using the authorization code
            flow.fetch_token(code=code)

            # Build the Google Calendar API service using the obtained credentials
            service = build('calendar', 'v3', credentials=flow.credentials, static_discovery=False)

            # Retrieve the list of events from the primary calendar
            events_result = service.events().list(calendarId='primary').execute()
            events = events_result.get('items', [])

            output = ''
            for event in events:
                event_name = event.get('summary', 'No event name')
                start = event.get('start', {}).get('dateTime', 'No start time')
                end = event.get('end', {}).get('dateTime', 'No end time')
                output += f"Event Name: {event_name}\nStart: {start}\nEnd: {end}\n\n"

            # Return the formatted event details to the client
            return HttpResponse(output, content_type='text/plain')
        except Exception as e:
            # Handle the exception, e.g., log the error or show an error message to the user
            return HttpResponse(f'An error occurred while retrieving calendar events: {e}')
