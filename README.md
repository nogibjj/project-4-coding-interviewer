[![CI](https://github.com/nogibjj/aws-template/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/nogibjj/aws-template/actions/workflows/cicd.yml)
[![Codespaces Prebuilds](https://github.com/nogibjj/aws-template/actions/workflows/codespaces/create_codespaces_prebuilds/badge.svg?branch=main)](https://github.com/nogibjj/aws-template/actions/workflows/codespaces/create_codespaces_prebuilds)

# Serverless GPT Coding Interviewer

Endpoint: https://duke-coding-interviewer.hf.space/

## Highlights
- Built a serverless GPT-empowered coding interviewer chatbot, whe the interviewer can analyze users' code and ask questions for users about time and space complexity, and related follow-up questions. 
- Deployed in Hugging Face Spaces (super easy, highly recommand!)

## Future Steps:
- Make it more flexible.
- Maybe further use any voice AI that need you to record your respone and interact with GPT interviewer.

## Steps
- Define the application architecture: The first step is to define the architecture of the application. Since we are building a serverless application, we will be using AWS Lambda to run the backend code. For the frontend, we can use a simple HTML page and JavaScript to interact with the Lambda functions.

- Setup AWS Lambda: Next, we need to create an AWS Lambda function to handle the backend logic of the application. We can use any programming language that Lambda supports. For example, we can use Node.js or Python to write the Lambda function.

- Integrate GPT3.5 API: We will use the OpenAI API to integrate GPT3.5 into our application. We need to sign up for an API key from OpenAI and then use it to make API requests from our Lambda function.

- Define the interview flow: We need to define the flow of the interview. For example, we can start with a simple coding question and then ask follow-up questions based on the response. We can use GPT3.5 to analyze the code and suggest improvements or ask questions about the complexity of the solution.

- Build the frontend: We can use HTML and JavaScript to build the frontend of the application. We can create a simple form where the user can input their code and submit it to the backend. We can also add a microphone input to allow the user to speak their answers to the interviewer.

- Implement the interview logic: We need to write the Lambda function to handle the interview logic. The function should receive the user's code and use GPT3.5 to analyze it and generate follow-up questions. The function should then return the questions to the frontend, which can display them to the user.

- Test and deploy: Once the application is complete, we can test it locally and then deploy it to AWS Lambda. We can use the AWS CLI or the AWS Console to deploy the application. We should also test the application thoroughly to ensure that it works as expected.

In summary, building a serverless web application to mock a coding interview with a GPT-empowered interviewer involves defining the application architecture, setting up AWS Lambda, integrating GPT3.5 API, defining the interview flow, building the frontend, implementing the interview logic, and testing and deploying the application.











## Template for AWS Projects

1. First thing to do on launch is to open a new shell and verify virtualenv is sourced.

Things included are:

* `Makefile`

* `Pytest`

* `pandas`

* `Pylint`

* `Dockerfile`

* `GitHub copilot`

* `jupyter` and `ipython` 

* Most common Python libraries for ML/DL and Hugging Face

* `githubactions` 

### Used in Following Projects

* [coursera-mlops-aws-c3-step-functions](https://github.com/nogibjj/coursera-mlops-aws-c3-step-functions)
* [coursera-mlops-aws-c3-eda](https://github.com/nogibjj/coursera-mlops-aws-c3-eda)
* [coursera-mlops-aws-c3-linear-regression](https://github.com/nogibjj/coursera-mlops-aws-c3-linear-regression)
* [coursera-mlops-aws-c30fine-tune-sagemaker-studio-lab](https://github.com/nogibjj/coursera-mlops-aws-c30fine-tune-sagemaker-studio-lab)

### References

* [Watch GitHub Universe Talk:  Teaching MLOps at scale with Github](https://watch.githubuniverse.com/on-demand/ec17cbb3-0a89-4764-90a5-9debb58515f8)
* [Building Cloud Computing Solutions at Scale Specialization](https://www.coursera.org/specializations/building-cloud-computing-solutions-at-scale)
* [Python, Bash and SQL Essentials for Data Engineering Specialization](https://www.coursera.org/learn/web-app-command-line-tools-for-data-engineering-duke)
* [Implementing MLOps in the Enterprise](https://learning.oreilly.com/library/view/implementing-mlops-in/9781098136574/)
* [Practical MLOps: Operationalizing Machine Learning Models](https://www.amazon.com/Practical-MLOps-Operationalizing-Machine-Learning/dp/1098103017)
* [Coursera-Dockerfile](https://gist.github.com/noahgift/82a34d56f0a8f347865baaa685d5e98d)
