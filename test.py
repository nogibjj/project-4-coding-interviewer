import openai

from key import APIKEY


openai.api_key = APIKEY

def generatePrompt(questionLink, userCode):
    
    preset = "You now act as an coding interviewer. You will be given a leetcode link and a code snippet. \
              You ned to analyze the code and ask questions to the candidate. \n"

    required = "You need to return following information as a dictionary: \
                {'time complexity': 'you add', \
                'space complexity': 'you add', \
                'why time complexity': 'you add', \
                'why space complexity': 'you add', \
                'follow-up questions' : 'you add', \
                'rate users code': 'you add'}, please make sure it's complete dictionary and what you add is string type. \n"

    prompt = preset + f"Leetcode Link: {questionLink} \n" + f"Code Snippet: {userCode} \n" + required

    return prompt

def generate_response(prompt, model="text-davinci-003", max_tokens=2000):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message


def identifyKeyInfo(phase, userInput, model="text-davinci-003", max_tokens=2000):
    prompt = f"You now act as an coding interviewer. Now you need substract the key information from the prompt. \
              For example, if your are in the phase of asking for leetcode link, you need to identify the link from the prompt and return the link string. \
              If you are in the phase of asking for code snippet, you need to identify the code snippet from the prompt and return the code snippet string. \
              If you are in the phase of asking for time and complexity, you need to identify the complexity formatted as O(N) from the prompt and return the complexity string. \
              If you think user input can not match current phase, pls return '400' as a string. Thank you.  \
              Now you are in phare of {phase}, please substract the key info from user input {userInput}!"
    
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message


def GiveOverallScore(history, model="text-davinci-003", max_tokens=2000):
    prompt = f"You now act as an coding interviewer. Now you need to give overall score to the user. \
              You will be given the history of the conversation \n \
             '{history}'. Please analyze user's code for the leetcode problem (efficient, readibility), \
              user's answers for time complexity and space complexity, user's follow-up questions. \n \
              Your need to return a dictionary with following keys: \
              'overall score out of 100': 'you add', 'feedbacks': 'you add'. \
              Please use double quotes for the keys and values when you output the dictionary. \
              Or you need to aviod use quotes in your values strings. \
              Also, if your score is not generous, please include the improvement points for users. Thank you."
    
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message