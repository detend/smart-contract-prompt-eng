from utils.api_client import OpenAIClient
from utils.prompt_utils import format_prompt


def zero_shot_analysis(prompt: str):
    """Performs zero-shot analysis on the given prompt."""

    """A prompt example:
            ```solidity
            contract VulnerableContract {
            mapping(address =&gt; uint) public balances;
            
            function withdraw() public {
            require(balances[msg.sender] &gt; 0, &quot;No balance&quot;);
            (bool success, ) = msg.sender.call{value: balances[msg.sender]}(&quot;&quot;);
            require(success, &quot;Transfer failed&quot;);
            balances[msg.sender] = 0;
            }
            }
            ```
    """
    prompt = format_prompt(prompt)
    full_prompt = f"Analyze the following Solidity smart contract and list any security vulnerabilities:\n{prompt}"
    client = OpenAIClient()
    return client.generate_response(full_prompt)

# Example usage:
if __name__ == "__main__":
    user_prompt = input("Enter your solidity code: ")
    print("Zero-Shot Analysis:\n", zero_shot_analysis(user_prompt))