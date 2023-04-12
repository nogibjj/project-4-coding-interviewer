import gradio as gr
import openai

from test import generatePrompt, generate_response, APIKEY 

openai.api_key = "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"

         




def analyze(questionLink, userCode):
    prompt = generatePrompt(questionLink, userCode)
    response = generate_response(prompt)
    # try:
    #     input_dict = eval(response)
    #     if (type(input_dict) != dict):
    #         gr.Error("invalid input! Try it again!")
    # except:
    #     gr.Error("invalid input!")
    
    return eval(response)

infoStore = {}

def add_text(history, text):
    history = history + [(text, None)]
    return history, ""

def bot(history):
    global infoStore
    last_message = history[-1][0].lower()
    if "leetcode.com" in last_message:
        
        infoStore['questionLink'] = last_message
        response = "Great! Please paste your code for this problem."
    
    elif "return" in last_message:
        
        infoStore['userCode'] = last_message
        analysis = analyze(infoStore['questionLink'], infoStore['userCode'])
        
        infoStore['gptOutput'] = analysis
        response = "Awesome! Let me ask the first question: what's the time complexity for your answer?"
    
    elif "time" in last_message:
        response = f"Time complexity of your code: {infoStore['gptOutput']['time complexity']}, \
                    because {infoStore['gptOutput']['why time complexity']} . \n \
                    Second question: what's the space complexity for your answer?"

    elif "space" in last_message:
        response = f"Space complexity of your code: {infoStore['gptOutput']['space complexity']}, \
                    because {infoStore['gptOutput']['why space complexity']} . \n \
                    Now I have some follow-up questions for you: {infoStore['gptOutput']['follow-up questions']} \n"
    
    history[-1][1] = response
    return history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot([(None, "Hello! I'm a coding interviewer powered by GPT. Please enter the LeetCode link for the problem you want to mock.")], elem_id="chatbot").style(height=500)

    with gr.Row():
        with gr.Column(scale=1):
            txt = gr.Textbox(
                show_label=False,
                placeholder= "Enter text and press enter",
            ).style(container=False)

    txt.submit(add_text, [chatbot, txt], [chatbot, txt]).then(
        bot, chatbot, chatbot
    )

demo.launch(debug = True, share = True)
