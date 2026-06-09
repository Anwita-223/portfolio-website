from openai import OpenAI

client = OpenAI()

  
response = client.chat.completions.create(
    model="gpt-4o",
    input = "Explain gravity in simple words."
)

print(response.output_text)


