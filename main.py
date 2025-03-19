from prompts.zero_shot import zero_shot_analysis
from prompts.few_shot import few_shot_analysis
from prompts.chain_of_thought import chain_of_thought_analysis
from prompts.instruction_based import instruction_based_analysis

def main():
    print("Select a prompt engineering technique:")
    print("1: Zero-Shot Analysis")
    print("2: Few-Shot Analysis")
    print("3: Chain-of-Thought Analysis")
    print("4: Instruction-Based Analysis")
    choice = input("Enter your choice (1-4): ")

    user_prompt = input("Enter your prompt or contract code: ")

    if choice == "1":
        print("Zero-Shot Analysis:\n", zero_shot_analysis(user_prompt))
    elif choice == "2":
        print("Few-Shot Analysis:\n", few_shot_analysis(user_prompt))
    elif choice == "3":
        print("Chain-of-Thought Analysis:\n", chain_of_thought_analysis(user_prompt))
    elif choice == "4":
        print("Instruction-Based Analysis:\n", instruction_based_analysis(user_prompt))
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()