import random
import json
import zhipuai
from tqdm import tqdm

zhipuai.api_key = ''

majors = [
    "Business Administration",
    "Psychology",
    "Nursing",
    "Biology",
    "Computer Science",
    "Political Science",
    "English",
    "Economics",
    "Communications",
    "Education",
    "Sociology",
    "Environmental Science/Studies",
    "Engineering",
    "Pre-Medical or Pre-Health Sciences",
    "History",
    "Mathematics",
    "Art and Design",
    "Chemistry",
    "Social Work",
    "Anthropology"
]


def generate_sample(tmp):
    major = random.sample(majors, 1)[0]
    grade = random.sample(['first', 'second', 'third', 'fourth'], 1)[0]


    prompt = [
        {
            "role": "assistant",
            "content": "(Justin is interviewing Eric)"
        },
        {
            "role": "user",
            "content": "Thank you for accepting our interview. My first question for today's interview is: What do "
                       "you think liberal arts is? Please provide a detailed answer based on your personal understanding "
                       "of liberal arts. "
        },
    ]
    bot_info = f"Eric is a {grade} year student who is currently studying {major} in Harvard. "

    try:
        response = zhipuai.model_api.invoke(
            temprature=tmp,
            model="characterglm",
            meta={
                "user_info": "I'm a researcher who's currently doing a research of what liberal arts education is.",
                "bot_info": bot_info,
                "bot_name": "Eric",
                "user_name": "Justin"
            },
            prompt=prompt
        )
        a1 = response['data']['choices'][0]['content']
    except:
        a1 = ''


    prompt.append({
        "role": "assistant",
        "content": a1})

    prompt.append({
        "role": "user",
        "content": "Based on your definition for liberal arts education, what’s your experience of liberal arts? "
                   "Have you ever been enlightened by it? "
    }, )

    try:
        response = zhipuai.model_api.invoke(
            temprature=tmp,
            model="characterglm",
            meta={
                "user_info": "I'm a researcher who's currently doing a research of what liberal arts education is.",
                "bot_info": bot_info,
                "bot_name": "Eric",
                "user_name": "Justin"
            },
            prompt=prompt
        )
        a2 = response['data']['choices'][0]['content']
    except:
        a2 = ''
    info = {'major': major, 'grade': grade, 'answer1': a1, 'answer2': a2}
    return info


if __name__ == '__main__':
    samples = {f'sample{i}': generate_sample(1.5+random.random()) for i in tqdm(range(1000))}
    print(samples)
    with open('samples.json', 'w') as json_file:
        json.dump(samples, json_file)
