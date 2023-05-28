# Google Calendar Integration

This project implements a Django REST API for integrating with Google Calendar using OAuth2. It allows users to authorize the application to access their calendar and retrieve a list of events.

## API Endpoints

### /rest/v1/calendar/init/
- View: GoogleCalendarInitView
- Description: This endpoint starts step 1 of the OAuth2 flow, prompting the user for their credentials.

### /rest/v1/calendar/redirect/
- View: GoogleCalendarRedirectView
- Description: This endpoint handles the redirect request sent by Google after the user authorizes the application. It performs the following tasks:
    1. Retrieves the access token from the provided authorization code.
    2. Retrieves a list of events in the user's calendar using the obtained access token.

## Prerequisites

Before running the project, make sure you have the following:

1. Google Cloud Console project with the Calendar API enabled.
2. OAuth 2.0 client credentials (client ID and client secret) obtained from the Google Cloud Console.
3. Django and required dependencies installed.

## Configuration

To configure the project, follow these steps:

1. Clone the repository from GitHub: [repository-link]
2. Install the project dependencies using the provided requirements.txt file.
3. Set the necessary environment variables:
4. Start the Django development server.

## Usage

1. Access the /rest/v1/calendar/init/ endpoint to initiate the OAuth2 flow.
2. Authenticate with your Google account and authorize the application to access your calendar.
3. After the authorization, you will be redirected to the /rest/v1/calendar/redirect/ endpoint.
4. The endpoint will retrieve the access token and fetch the list of events from your calendar.
5. The events will be displayed in the response.

## Error Handling

The application includes basic error handling for common exceptions that may occur during the OAuth2 flow or when retrieving events from the calendar. Error messages will be returned to the client in case of any exceptions.


Feel free to explore the code, make improvements, and provide any feedback.

