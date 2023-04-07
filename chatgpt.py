import openai

openai.api_key = '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'

while True:

    prompt = input("\n Make a question: ")
    if prompt == "exit":
        break
    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          max_tokens=2048)
    print(completion.choices[0].text)
