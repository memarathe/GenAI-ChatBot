import dotenv
dotenv.load_dotenv()
from openai import OpenAI
client = OpenAI()
print(client.models.list())