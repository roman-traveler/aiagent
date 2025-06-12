import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not set in environment.")
    sys.exit(1)

# Handle --verbose flag and prompt argument
verbose = False
args = sys.argv[1:]
if "--verbose" in args:
    verbose = True
    args.remove("--verbose")

if len(args) < 1:
    print(f"Usage: {sys.argv[0]} <prompt> [--verbose]")
    sys.exit(1)

user_prompt = args[0]

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

# Access the first candidate's content
content = response.candidates[0].content
for part in content.parts:
    print(part.text, end='')
print()  # Ensure a newline after the response
if verbose:
    print(f"User prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")