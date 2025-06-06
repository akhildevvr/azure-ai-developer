import asyncio
import logging
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureTextToImage, AzureChatPromptExecutionSettings
from semantic_kernel.connectors.memory.azure_ai_search import AzureAISearchStore
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.openapi_plugin import OpenAPIFunctionExecutionParameters
from semantic_kernel.connectors.ai.open_ai import AzureTextEmbedding
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions import KernelArguments
import os
from pathlib import Path

from plugins.ai_search_plugin import AiSearchPlugin
from plugins.geo_coding_plugin import GeoPlugin
from plugins.image_plugin import ImagePlugin
from plugins.time_plugin import TimePlugin
from plugins.weather_plugin import WeatherPlugin


# Add Logger
logger = logging.getLogger(__name__)

# Find and load the .env file from the src directory
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path, override=True)

# Direct console output that will always be visible
print("============ ENVIRONMENT VARIABLES ============")
print(f"Using .env from: {env_path}")
print(f"File exists: {env_path.exists()}")
print(f"AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: {os.environ.get('AZURE_OPENAI_CHAT_DEPLOYMENT_NAME')}")
print(f"AZURE_OPENAI_ENDPOINT: {os.environ.get('AZURE_OPENAI_ENDPOINT')}")
print(f"AZURE_OPENAI_API_KEY: {'*****' if os.environ.get('AZURE_OPENAI_API_KEY') else 'Not found'}")
print(f"GEOCODING_API_KEY: {'*****' if os.environ.get('GEOCODING_API_KEY') else 'Not found'}")
print(f"AZURE_OPENAI_API_VERSION: {os.environ.get('AZURE_OPENAI_API_VERSION')}")
print(f"AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME: {os.environ.get('AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME')}")
print(f"AZURE_AI_SEARCH_ENDPOINT: {os.environ.get('AZURE_AI_SEARCH_ENDPOINT')}")
print(f"AZURE_AI_SEARCH_API_KEY: {'*****' if os.environ.get('AZURE_AI_SEARCH_API_KEY') else 'Not found'}")
print(f"AZURE_AI_SEARCH_INDEX_NAME: {os.environ.get('AZURE_AI_SEARCH_INDEX_NAME')}")
print(f"AZURE_OPENAI_TEXT_TO_IMAGE_DEPLOYMENT_NAME: {os.environ.get('AZURE_OPENAI_TEXT_TO_IMAGE_DEPLOYMENT_NAME')}")
print("==============================================")

chat_history = ChatHistory()

def initialize_kernel():
    #Challenge 02 - Chat Completion Service
    load_dotenv()  # Loads environment variables from .env

    deployment_name = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")

    kernel = Kernel()

    chat_service = AzureChatCompletion(
        deployment_name=deployment_name,
        endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
        service_id="AzureChatCompletionService"
    )


    

    #Challenge 02 - Chat Completion Service
    #Challenge 02- Add kernel to the chat completion service
    kernel.add_service(chat_service)

    # Challenge 05 - Add Text Embedding Service
    embedding_service = AzureTextEmbedding(
    deployment_name=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"),
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    )
    kernel.add_service(embedding_service)

    # Challenge 07 - Add Text to Image Service
    text_to_image_service = AzureTextToImage(
        deployment_name=os.getenv("AZURE_OPENAI_TEXT_TO_IMAGE_DEPLOYMENT_NAME"),
        endpoint=os.getenv("AZURE_OPENAI_DALLE_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_DALLE_API_KEY"),
        service_id="AzureTextToImageService"
    )
    kernel.add_service(text_to_image_service)


    return kernel


async def process_message(user_input):
    kernel = initialize_kernel()

    # Challenge 03 - Add Time Plugin
    time_plugin = TimePlugin()
    # Add the plugin to the kernel
    kernel.add_plugin(time_plugin)


    # Challenge 03 - Add Geo Plugin
    geo_plugin = GeoPlugin()
    # Add the plugin to the kernel
    kernel.add_plugin(geo_plugin)



    # CHallenge 03 - Add Weather Plugin
    weather_plugin = WeatherPlugin()
    kernel.add_plugin(weather_plugin)
        


    # Challenge 04 - Import OpenAPI Spec
    kernel.add_plugin_from_openapi(
        plugin_name="work_items",
        openapi_document_path="http://127.0.0.1:8000/openapi.json",
        execution_settings=OpenAPIFunctionExecutionParameters(
                # Determines whether payload parameter names are augmented with namespaces.
                # Namespaces prevent naming conflicts by adding the parent parameter name
                # as a prefix, separated by dots
                enable_payload_namespacing=True,
        ),
        )


    # Challenge 05 - Add Search Plugin
    search_plugin = AiSearchPlugin(kernel)
    # Add the plugin to the kernel
    kernel.add_plugin(search_plugin)


    # Challenge 07 - Text To Image Plugin
    image_plugin = ImagePlugin(kernel)
    # Add the plugin to the kernel
    kernel.add_plugin(image_plugin)



    # Start Challenge 02

    # Get the chat completion service from the kernel
    chat_service = kernel.get_service(service_id="AzureChatCompletionService")

    global chat_history  # Use the global chat history variable

    # Add the user's message to chat history
    chat_history.add_user_message(user_input)

    # Create settings for the chat request
    settings = AzureChatPromptExecutionSettings(
        max_tokens=1024,
        temperature=0.7,
        top_p=0.8,
    )
    settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    # Send the chat history to the AI and get a response
    settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    # Use streaming response
    response = chat_service.get_streaming_chat_message_content(
        chat_history=chat_history,
        settings=settings,
        kernel=kernel,
        arguments=KernelArguments(),
    )

    message_text = ""
    async for chunk in response:
        print(chunk, end="", flush=True)
        message_text += str(chunk)

    # Add the AI's response to chat history
    chat_history.add_assistant_message(message_text)

    return message_text

def reset_chat_history():
    global chat_history
    chat_history = ChatHistory()
