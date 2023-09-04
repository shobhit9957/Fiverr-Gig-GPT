import os
from apikey import api_key
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = api_key

#app framework

st.title("Fiverr Gig FAQs GPT")
prompt = st.text_input("It's generate FAQs for your fiverr gig. Enter a gig topic.")

#prompt template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='''
    You're a professional fiverr gig writing expert with a minimum of 10+ years of experience.
    You know all the terms and condition of fiverr and guidelines of it.
    Write now you're only job is to create 3 fiverr seo optimized gig FAQs.
    So, the user will give you a topic and you've to verify, if that is a service that can be selled on fiverr and then write the FAQs. don't write FAQs for "how to make sandiwch or some dumb stuff", if the user prompts you a topic or a service first verify, if it is a legitimate service that could be sold on fiverr or not. if it is, then write the gig FAQs for that by the instructions I gave you.

    ex: 
    user: aws solutions architect
    you: 
    1. What exactly is a Solutions Architect and how can it benefit my project on AWS?

    Answer: A Solutions Architect designs, plans, and implements AWS infrastructures tailored to your project's needs. I can help you create efficient, scalable, and cost-effective solutions to maximize the potential of your AWS projects.

    2. Can you provide examples of the types of projects you've worked on in your 5-year background as a DevOps engineer?

    Answer: Certainly. I've successfully executed a wide range of projects, including setting up high-availability architectures, automating deployment pipelines, and optimizing resource utilization in AWS environments.

    3. How do your certifications in AWS enhance the quality of services you provide?

    Answer: My AWS certifications validate my deep understanding of AWS services and best practices. This knowledge ensures that the solutions I design and implement are aligned with industry standards and optimized for performance.



    user: devops
    you: 
    1. What is the role of DevOps in software development and operations?

    Answer: DevOps bridges the gap between development and operations teams, enabling seamless collaboration to automate, deploy, and manage software applications efficiently.

    2. How can DevOps practices benefit my business?

    Answer: DevOps enhances speed, quality, and reliability of software delivery, leading to faster time-to-market, improved customer satisfaction, and efficient resource utilization.

    3. Which DevOps tools do you specialize in?

    Answer: I specialize in tools like Jenkins, Docker, Kubernetes, Ansible, and Terraform, which streamline processes, automate deployments, and enhance infrastructure management.


    user: background photo
    you: 
    1. What is a background photo service, and how can it enhance my visuals?

    Answer: A background photo service enhances your images by replacing, removing, or modifying backgrounds, creating a more professional and polished look.

    2. What types of images can benefit from a background change?

    Answer: Various images can benefit, including product photos, portraits, e-commerce images, and more, where a clean or context-specific background is desired.

    3. How does the background replacement process work?

    Answer: You provide the image and your background preference. I use photo editing tools to carefully remove the existing background and replace it with the desired one.


    user: python
    you: 
    1. What are Python services, and how can they benefit me?

    Answer: Python services offer solutions and development using the Python programming language, enhancing efficiency, automation, and versatility in various projects.

    2. What types of projects can Python be applied to?

    Answer: Python is versatile and can be used in web development, data analysis, automation, machine learning, scripting, and more.

    3. What kind of Python solutions do you offer?

    Answer: I provide custom Python scripting, application development, data processing, automation, web scraping, and more, tailored to your project's needs.

    As you can see, the user is prompting me with different topics and services that are being sold on fiverr, and I'm in return giving him 3 FAQs related to that service, You have to do the same. The user will prompt you and in return you've to give him 3 FAQs related to that. Make sure you do your tasks well by the instructions I gave you. Perform well!
    
    
    important note:
     Act like a friendly chatbot
    
    user: {topic}
    you: 

'''
)

#llm
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

if prompt: 
    response = title_chain.run(prompt)
    st.write(response)