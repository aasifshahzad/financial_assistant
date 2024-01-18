
from openai import OpenAI
from functions import available_functions, tools
import time
import json
import os



def initialize_openai_client(entered_api_key) -> OpenAI:
    """
    Initialize the OpenAI client.

    :return: Initialized OpenAI client.
    """
    # load_dotenv(find_dotenv("E:/Python/.env"))
    # openai_key = os.environ.get("OPENAI_API_KEY")
    openai_key = entered_api_key
    client = OpenAI(api_key=openai_key)
    return client

def show_json(obj: object) -> None:
    """
    Show JSON representation of the object.

    :param obj: Object to display in JSON format.
    """
    print(json.dumps(json.loads(obj.model_dump_json()), indent=4))

#thread = client.beta.threads.create()

def submit_message( thread: object, user_message: str,assistant_id) -> dict:
    """
    Submit a message to the Financial Analyst.

    :param assistant_id: The ID of the Financial Analyst.
    :param thread: The ID of the thread to send the message to.
    :param user_message: The message to send.
    :return: The response from the Financial Analyst.
    """
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message)
    run = client.beta.threads.runs.create(
        assistant_id=assistant_id,
        thread_id=thread.id
    )
    return run

def wait_on_run(run: dict, thread: object, available_functions: dict) -> dict:
    """
    Wait for the completion of a run and handle the response.

    :param run: Run details.
    :param thread: The ID of the thread to wait on.
    :param available_functions: Available functions for processing tool calls.
    :return: The updated run.
    """
    while True:
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

        if run.status == "requires_action" and run.required_action is not None:
            tool_calls = run.required_action.submit_tool_outputs.tool_calls
            tool_outputs = []

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)

                if function_name in available_functions:
                    function_to_call = available_functions[function_name]
                    output = function_to_call(**function_args)
                    tool_outputs.append({
                        "tool_call_id": tool_call.id,
                        "output": output,
                    })

            client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=tool_outputs
            )

        elif run.status == "completed":
            print("Run Completed")
            break

        elif run.status == "failed":
            print("Run Failed.")
            break

        elif run.status in ["in_progress", "queued"]:
            print(f"Run is {run.status}. Waiting...")
            time.sleep(5)

        else:
            print(f"Unexpected status: {run.status}")
            break
    return run

# # def get_response(thread: object, run: object) -> str:
#     """
#     Retrieve messages from a thread.

#     :param thread: The ID of the thread to retrieve messages from.
#     :return: Messages retrieved from the thread.
#     """
#     messages = client.beta.threads.messages.list(
#         thread_id = thread.id,
#         order = "asc"
#     )
#     if messages:
#         for message in messages.data:
#             role_label = "User" if message.role == "user" else "Assistant"
#             message_content = message.content[0].text.value
#             print(f"{role_label}:   {message_content}\n")


#         return role_label, message_content 
#     else:
#         return "Unable to get Response from Assistant"

# # def pretty_print(messages: list) -> str:
#     """
#     Generate a readable representation of messages.

#     :param messages: List of messages to be formatted.
#     :return: Formatted string containing user and assistant messages.
#     """
#     responses = []
#     for message in messages:
#         if message.role == "user":
#             responses.append("You: " + message.content[0].text.value)
#         elif message.role == "assistant":
#             responses.append("Bot: " + message.content[0].text.value)

#     return "\n".join(responses)

def process_completed_run(run, client, st_session_state):
    # if run.status == "completed":
    # List the messages to get the response
    messages = client.beta.threads.messages.list(thread_id=st_session_state.thread_id) # type: ignore
    for message in messages.data:
        role_label = "User" if message.role == "user" else "Assistant"
        message_content = message.content[0].text.value
        print(f"{role_label}:   {message_content}\n")

    # Process and return assistant messages
    assistant_messages_for_run = [
        message for message in messages.data 
        if message.run_id == run.id and message.role == "assistant"
    ]

    return assistant_messages_for_run

client: OpenAI = initialize_openai_client(entered_api_key=os.environ.get("OPENAI_API_KEY"))

assistant = client.beta.assistants.create(
    name="Financial Analyst",
    instructions="Act as a financial analyst by accessing detailed financial data through the Financial Modeling Prep API. Your capabilities include analyzing key metrics, comprehensive financial statements, vital financial ratios, and tracking financial growth trends.",
    tools=tools,
    model="gpt-3.5-turbo-1106"
)

# assistant_id = "asst_eBpda9pIxOsh7PCI15JBZlZN"
assistant_id  = assistant.id
available_functions = available_functions



