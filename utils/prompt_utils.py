"""
Utility functions for handling prompt formatting.
"""
def format_prompt(contract_code: str) -> str:
    return f"```solidity\n{contract_code}\n```"