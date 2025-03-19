from utils.api_client import OpenAIClient
from utils.prompt_utils import format_prompt


def instruction_based_analysis(prompt: str):
    """Performs instruction-based analysis on the given prompt."""
    client = OpenAIClient()

    instructions = """
    Use a structured format:
    1. Vulnerability name
    2. Description
    3. Possible Exploits
    4. Suggested Fix 
    """

    prompt = format_prompt(prompt)
    full_prompt = f"Identify vulnerabilities in the following Solidity contract based on the instructions:\nInstructions:{instructions}\nCode:{prompt}"

    return client.generate_response(full_prompt)

# Example usage:
if __name__ == "__main__":
    user_prompt = input("Enter your solidity code: ")
    print("Instruction-Based Analysis:\n", instruction_based_analysis(user_prompt))