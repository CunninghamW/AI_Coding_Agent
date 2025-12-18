import argparse # Used to handle command line arguements
import os       # used for file path and environment operations
import shutil   # used to make backups of files
import sys      # for system related functions
from assistant.gemini_client import GeminiClient
from assistant.openai_client import OpenAIClient
from assistant.ollama_client import OllamaClient
from assistant.claude_client import ClaudeClient
from assistant.prompts import SYSTEM_PROMPT # default instructions for the AI

# Map model names to their client classes
MODEL_MAP = {
    "gemini": GeminiClient,
    "openai": OpenAIClient,
    "ollama": OllamaClient,
    "claude": ClaudeClient
}

def main():
    # Setup command line argument parsing
    parser = argparse.ArgumentParser(description="Full Code Editing Agent CLI")
    parser.add_argument("prompt", help="Ask the assistant to edit your code")
    parser.add_argument("--model", choices=MODEL_MAP.keys(), default="gemini",
                        help="Select which AI model backend to use")
    parser.add_argument("--file", help="Path to a Python file to edit")
    parser.add_argument("--yes", action="store_true",
                        help="Automatically apply suggested edits")
    parser.add_argument("--no-stream", action="store_true",
                        help="Disable streaming output")
    args = parser.parse_args()

    # Initialize assistant client
    assistant_class = MODEL_MAP[args.model]
    assistant = assistant_class()

    # Construct full prompt with system message
    full_prompt = f"{SYSTEM_PROMPT}\n{args.prompt}"

    # File editing mode
    if args.file:
        if not os.path.exists(args.file):
            print(f"File {args.file} does not exist.")
            return

        # Backup original file
        backup_path = args.file + ".bak"
        shutil.copy(args.file, backup_path)
        print(f"Backup created: {backup_path}")

        with open(args.file, "r") as f:
            code = f.read()

        full_prompt += f"\n\nCurrent code:\n{code}"

        # Use streaming if supported and enabled
        if not args.no_stream and hasattr(assistant, "stream"):
            print("\nStreaming suggested code edits:\n")
            suggested_code = ""
            for chunk in assistant.stream(full_prompt):
                print(chunk, end="", flush=True)
                suggested_code += chunk
            print()  # newline at end
        else:
            suggested_code = assistant.ask(full_prompt)
            print("\nSuggested code edits:\n")
            print(suggested_code)

        # Apply edits if --yes is specified
        if args.yes:
            with open(args.file, "w") as f:
                f.write(suggested_code)
            print(f"\nChanges applied to {args.file}")
        else:
            print("\nUse --yes to automatically apply edits.")

    # Normal CLI prompt mode (no file)
    else:
        if not args.no_stream and hasattr(assistant, "stream"):
            print("\nStreaming response:\n")
            for chunk in assistant.stream(full_prompt):
                print(chunk, end="", flush=True)
            print()
        else:
            response = assistant.ask(full_prompt)
            print("\nAssistant:\n")
            print(response)


if __name__ == "__main__":
    main()




