import yaml
import openai

# Load API configuration
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

API_KEY = config["api"]["key"]
API_ENDPOINT = config["api"]["endpoint"]
MODEL = config["api"]["model"]
PROVIDER = config["api"]["provider"]

# OpenAI API client
class OpenAIClient:
    def __init__(self):
        self.client = openai.AzureOpenAI(
            api_key=API_KEY, base_url=API_ENDPOINT
        )

    def generate_response(self, prompt, max_tokens=500):
        response = self.client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()