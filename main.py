import openai
from apikey import API_KEY

openai.api_key = API_KEY
openai.Model.list()

openai.Model.retrieve("text-davinci-003")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Say this is a test",
    max_tokens=7,
    temperature=0
)

generated_answer = response.choices[0].text.strip()
print(generated_answer)
