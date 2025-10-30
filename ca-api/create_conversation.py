import os
from google.cloud import geminidataanalytics

from google.api_core import exceptions

location = "global"
billing_project = os.environ.get('DEVSHELL_PROJECT_ID')
data_agent_id = "google_trends_analytics_agent"


def setup_conversation(conversation_id: str):
    data_chat_client = geminidataanalytics.DataChatServiceClient()
    conversation = geminidataanalytics.Conversation(
        agents=[data_chat_client.data_agent_path(
            billing_project, location, data_agent_id)],
    )
    request = geminidataanalytics.CreateConversationRequest(
        parent=f"projects/{billing_project}/locations/{location}",
        conversation_id=conversation_id,
        conversation=conversation,
    )
    try:
        data_chat_client.get_conversation(name=data_chat_client.conversation_path(
            billing_project, location, conversation_id))
        print(f"Conversation '{conversation_id}' already exists.")
    except Exception:
        response = data_chat_client.create_conversation(request=request)
        print("Conversation created successfully:")
        print(response)


conversation_id = "my_second_conversation"
setup_conversation(conversation_id=conversation_id)