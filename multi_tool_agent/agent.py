import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def is_allowed_animal(animal_type: str) -> dict:
    """Check if an animal is allowed or not.

    Args:
        animal_type (str): The type of the animal. For example, "cat" or "dog".

    Returns:
        dict: status and result or error msg.
    """
   
    if "cat" in animal_type.lower():
        return {
            "status": "success",
            "result": "This animal is allowed."
        }
    else:
        return {
            "status": "error",
            "error_message": "This animal is not allowed."
        }



root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to extract the animal type from an image and check if it is allowed or not."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about if an animal is allowed or not. "
    ),
    tools=[is_allowed_animal],
)