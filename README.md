# Interview Simulation
Using CharactorGLM to construct a simulation on interviewing students on their attitudes towards liberal arts education.

# File Overview
## conv_zhipu.py
Uses CharactorGLM to generate samples and store it in samples.json

## keywords_extra.ipynb
Uses the N-gram algorithm implemented by NLTK to count the keywords in the generated samples. Most part of this file was
written by ChatGPT.

## classification.ipynb
The approach used in keywords_extra.ipynb is not suitable for this task, the algorithm was unable to notice different 
tenses and parts of speech of the same keyword. This new approach counts the keywords by using manually written patterns
to find common keywords found in keywords_extra.ipynb.