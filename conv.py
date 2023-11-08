import openai

# to get proper authentication, make sure to use a valid key that's listed in
# the --api-keys flag. if no flag value is provided, the `api_key` will be ignored.
openai.api_key = "EMPTY"
openai.api_base = "http://localhost:8000/v1"

model = "vicuna-13b-v1.5"
prompt = "Once upon a time"

# create a completion
# completion = openai.Completion.create(model=model, prompt=prompt, max_tokens=64)
# print the completion
# print(prompt + completion.choices[0].text)

major = 'computer science'
grade = 'first grade'

identity_prompt = f'You are a {grade} student who is currently studying {major} in Harvard. Your are now being ' \
                  f'interviewed by the user with a topic of your understanding of liberal arts education.' \
                  f'Your answer should based on personal opinions that is independent of any dictionaries ' \
                  f'encyclopedia, or other books. Make sure ' \
                  f'all your answer is a personalized answer form the perspective of a college student.'

print(identity_prompt)
# create a chat completion
completion = openai.ChatCompletion.create(
    model=model,
    temperature=1.3,
    messages=[{"role": "system", "content": identity_prompt}, {"role": "user", "content": "Hi! My first "
                                                                                          "question is: What "
                                                                                          "does liberal arts education mean to you?"}]
)
# print the completion
print(completion.choices[0].message.content)