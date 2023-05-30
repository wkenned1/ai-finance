import creds
import openai

openai.api_key = creds.openai_api_key
openai.organization = creds.organization
print(openai.Model.list())

