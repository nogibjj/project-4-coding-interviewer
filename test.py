import openai

APIKEY = "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"


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


questionLink = "https://leetcode.com/problems/two-sum/"
samplecode = "class Solution: def twoSum(self, nums: List[int], target: int) -> List[int]: d = {} for i, num in enumerate(nums): if target - num not in d: d[num] = i else: return[i, d[target-num]]"

# prompt = generatePrompt(questionLink, samplecode)
# print(prompt)

# response = generate_response(prompt)
# print(response)