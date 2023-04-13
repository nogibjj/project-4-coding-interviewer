import gradio as gr
import openai

from test import generatePrompt, generate_response, identifyKeyInfo, GiveOverallScore, APIKEY 

openai.api_key = APIKEY

def analyze(questionLink, userCode):
    prompt = generatePrompt(questionLink, userCode)
    response = generate_response(prompt)    
    return eval(response)

infoStore = {}

phases = ['Ask For Leetcode Link', 'Ask For User Code', 'Ask For Time Complexity', 'Ask For Space Complexity', 
          'Ask FollowUp', 'Rate User for the Interview']

def add_text(history, text):
    history = history + [(text, None)]
    return history, ""

currentPhase = 0

def bot(history):

    global phases

    global currentPhase

    global infoStore
    
    last_message = history[-1][0].lower()

    keyInfo = identifyKeyInfo(phases[currentPhase], last_message)

    if keyInfo == '400':
        response = "Sorry, I don't understand, please try again."

    else:
    
        if currentPhase == 0:
            infoStore['questionLink'] = keyInfo
            response = "Great! Please paste your code for this problem."
        
        elif currentPhase == 1:    
            infoStore['userCode'] = keyInfo
            analysis = analyze(infoStore['questionLink'], infoStore['userCode'])
            infoStore['gptOutput'] = analysis
            response = "Awesome! \n\
                        Let me ask the first question: what's the time complexity for your answer?"
        
        elif currentPhase == 2:
            
            userTimeComplexity = keyInfo
            if userTimeComplexity.lower() == (infoStore['gptOutput']['time complexity']).lower():
                response = f"Correct! \n"
            else:
                response = f"Wrong! The correct answer is {infoStore['gptOutput']['time complexity']}, \
                            because {infoStore['gptOutput']['why time complexity']} . \n "
            response += "\nSecond question: what's the space complexity for your answer?"
    
        elif currentPhase == 3:

            userSpaceComplexity = keyInfo
            if userSpaceComplexity.lower() == (infoStore['gptOutput']['space complexity']).lower():
                response = f"Correct! \n"
            else:
                response = f"Wrong! The correct answer is {infoStore['gptOutput']['space complexity']}, \
                            because {infoStore['gptOutput']['why space complexity']} . \n "
            
            response += f"\nNow I will ask you a follow-up question: \n \
                        {infoStore['gptOutput']['follow-up questions']} \n"

        elif currentPhase == 4:

            scoreFeedback = eval(GiveOverallScore(history))
            response = f"Thank you for your time! \n \
                        Your overall score (out of 100) is {scoreFeedback['overall score out of 100']} \n \
                        \n \
                        You can check your detailed feedback below: \n \
                        {scoreFeedback['feedbacks']}. \n"
        
        currentPhase += 1
   
    history[-1][1] = response
    return history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot([(None, "Hello! I'm a coding interviewer powered by GPT. Please enter the LeetCode link for the problem you want to mock.")], elem_id="chatbot").style(height=600)

    with gr.Row():
        with gr.Column(scale=1):
            txt = gr.Textbox(
                show_label=False,
                placeholder= "Enter text and press enter",
            ).style(container=False)

    txt.submit(add_text, [chatbot, txt], [chatbot, txt]).then(
        bot, chatbot, chatbot
    )

demo.launch(debug = True)
