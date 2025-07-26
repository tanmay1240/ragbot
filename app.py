from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")  # ✅ Explicitly load .env from project root

from dotenv import load_dotenv  # ✅ To load .env
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()  # ✅ Loads environment variables like OPENAI_API_KEY

embeddings = OpenAIEmbeddings()
vec = embeddings.embed_query("Hello world")
print(vec[:5])
