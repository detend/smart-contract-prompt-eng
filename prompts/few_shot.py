from utils.api_client import OpenAIClient
from utils.prompt_utils import format_prompt


def few_shot_analysis(prompt: str):
    """Performs few-shot analysis on the given prompt, adding predefined vulnerability examples."""
    client = OpenAIClient()
    vulnerability_examples = """
    Example 1:
    Code:
    ```solidity
    contract Proxy {
      address owner;
      constructor() public {
        owner = msg.sender;
      }
    
      function forward(address callee, bytes _data) public {
        // <yes> <report> ACCESS_CONTROL
        require(callee.delegatecall(_data)); //Use delegatecall with caution and make sure to never call into untrusted contracts
      }
    
    }
    ```
    Vulnerability: access control

    Example 2:
    Code:
    ```solidity
    
    contract EtherBank{
        mapping (address => uint) userBalances;
        function getBalance(address user) constant returns(uint) {  
            return userBalances[user];
        }
    
        function addToBalance() {  
            userBalances[msg.sender] += msg.value;
        }
    
        function withdrawBalance() {  
            uint amountToWithdraw = userBalances[msg.sender];
            // <yes> <report> REENTRANCY
            if (!(msg.sender.call.value(amountToWithdraw)())) { throw; }
            userBalances[msg.sender] = 0;
        }    
    }
    ```
    Vulnerability: reentrancy
    
    Example 3:
    Code:
    ```solidity
    
    contract Overflow_Add {
        uint public balance = 1;
    
        function add(uint256 deposit) public {
            // <yes> <report> ARITHMETIC
            balance += deposit;
        }
    }
    ```
    Vulnerability: overflow
    """

    prompt = format_prompt(prompt)
    full_prompt = f"Identify vulnerabilities in the following Solidity contract based on past examples:\nExamples:{vulnerability_examples}\nCode:{prompt}"
    return client.generate_response(full_prompt)

# Example usage:
if __name__ == "__main__":
    user_prompt = input("Enter your Solidity contract: ")
    print("Few-Shot Analysis:\n", few_shot_analysis(user_prompt))