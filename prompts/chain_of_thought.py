from utils.api_client import OpenAIClient
from utils.prompt_utils import format_prompt


def chain_of_thought_analysis(prompt: str):
    """Performs chain-of-thought analysis on the given prompt."""

    prompt = format_prompt(prompt)
    full_prompt = f"Analyze this smart contract step by step and identify vulnerabilities:\n{prompt}"
    client = OpenAIClient()
    return client.generate_response(full_prompt)

# Example usage:
if __name__ == "__main__":
    user_prompt = input("Enter your solidity code: ")
    print("Chain-of-Thought Analysis:\n", chain_of_thought_analysis(user_prompt))