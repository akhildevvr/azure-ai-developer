import os
import asyncio
import logging
from pathlib import Path
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.agents import AgentGroupChat, ChatCompletionAgent
from semantic_kernel.agents.strategies import (
    KernelFunctionSelectionStrategy,
    KernelFunctionTerminationStrategy,
)
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents import ChatHistoryTruncationReducer
from semantic_kernel.functions import KernelFunctionFromPrompt

# Add Logger
logger = logging.getLogger(__name__)

# Find and load the .env file from the src directory
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path, override=True)

def create_kernel():
    """Creates a Kernel instance with an Azure OpenAI ChatCompletion service."""
    kernel = Kernel()
    kernel.add_service(service=AzureChatCompletion())
    return kernel

async def run_multi_agent(user_input: str):
    """
    Run a multi-agent collaboration with Business Analyst, Software Engineer, and Product Owner.
    
    Args:
        user_input (str): The user's request for application development
    """
    # Create a single kernel instance for all agents
    kernel = create_kernel()
    
    # Define agent names as constants
    # IMPORTANT: These names must match the ones used in the selection function
    # as they are used in the UI to help change how the agents are displayed
    BUSINESS_ANALYST_NAME = "BusinessAnalyst"
    SOFTWARE_ENGINEER_NAME = "SoftwareEngineer" 
    PRODUCT_OWNER_NAME = "ProductOwner"

    # Step 1 - Create ChatCompletionAgents
    # Define instructions/personas for each agent
    business_analyst_instructions = (
        "You are a skilled Business Analyst. "
        "Your job is to clarify requirements, ask questions, and ensure the business needs are well understood."
    )
    software_engineer_instructions = (
        "You are a talented Software Engineer. "
        "Your job is to propose technical solutions, estimate effort, and identify implementation challenges."
    )
    product_owner_instructions = (
        "You are the Product Owner. "
        "Your job is to approve or reject solutions, prioritize features, and ensure the product meets business goals. "
        "When you approve the work, respond with '%APPR%'."
    )

    # Create ChatCompletionAgent instances
    business_analyst = ChatCompletionAgent(
        kernel=kernel,
        name=BUSINESS_ANALYST_NAME,
        instructions=business_analyst_instructions
    )
    software_engineer = ChatCompletionAgent(
        kernel=kernel,
        name=SOFTWARE_ENGINEER_NAME,
        instructions=software_engineer_instructions
    )
    product_owner = ChatCompletionAgent(
        kernel=kernel,
        name=PRODUCT_OWNER_NAME,
        instructions=product_owner_instructions
    )
    
    # TODO: Step 2 - Define a selection function to determine which agent should take the next turn

    
    # TODO: Step 3 - Define a termination function
    # Create a KernelFunctionFromPrompt that checks if the Product Owner has approved the work
    # The termination keyword is "%APPR%"
    # The function should respond with the termination keyword when the Product Owner approves
    
    
    # TODO: Step 4 - Create history reducer to save tokens
    # Create a ChatHistoryTruncationReducer with target_count=3 to limit conversation history
    
    
    # TODO: Step 5 - Create the AgentGroupChat
    
    
    # TODO: Step 6 - Add the user's initial request to the chat
    
    
    responses = []
    
    # TODO: Step 7 - Invoke the group chat and collect agent responses
    # Use an async for loop to iterate through group_chat.invoke()
    # Collect responses in the format: {"role": response.name, "message": response.content}
    
    logger.info("Multi-agent conversation complete.")
    return responses
