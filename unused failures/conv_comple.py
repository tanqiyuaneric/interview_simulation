import openai

# to get proper authentication, make sure to use a valid key that's listed in
# the --api-keys flag. if no flag value is provided, the `api_key` will be ignored.
openai.api_key = "EMPTY"
openai.api_base = "http://localhost:8000/v1"

model = "vicuna-13b-v1.5"
with open('prompt.txt', 'r', encoding='utf-8') as file:
    # 2. 读取文件内容
    prompt = file.read()

# create a completion
completion = openai.Completion.create(model=model, prompt=prompt, max_tokens=200, temprature=1.5)
# print the completion
print(completion.choices[0].text)
