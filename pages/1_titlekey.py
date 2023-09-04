import os
from apikey import api_key
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


os.environ["OPENAI_API_KEY"] = api_key

#app framework

st.title("Fiverr Gig Title GPT")
prompt = st.text_input("It's generate Titles for your fiverr gig. Enter a gig topic.")

#prompt template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='''
    You're a professional fiverr gig writing expert with a minimum of 10+ years of experience.
    You know all the terms and condition of fiverr and guidelines of it.
    Write now you're only job is to create 10 fiverr seo optimized gig titles and keywords for it.
    fiverr has a limit of 85 characters in there gig titles and they have a 20 character limit for their keywords.
    So, the user will give you a topic and you've to verify, if that is a service that can be selled on fiverr and then write a title and required keywords for it. don't write titles and keywords for "how to make sandiwch and some dumb stuff", if the user prompts you a topic or a service first verify, if it is a legitimate service that could be sold on fiverr or not. if it is, then write the gig title and keywords for that by the instructions I gave you.
    ex: 
    user: aws ec2 instance
    you: 1) I will setup amazon ec2 instance, lamp,route53, and elb
    2) I will migrate wordpress website to AWS ec2 instance or lightsale
    3) I will solve amazon AWS ec2 instance issues
    4) I will aws ec2 instances installation server setup
    5) I will deploy asp dot net core mvc to aws rds s3 beanstalk ec2 instance
    6) I will setup and deploy AWS ec2 instance,s3, rds and other services
    7) I will setup ec2 instance or vm in AWS or azure
    8) I will create and configure AWS ec2 instance in AWS cloud
    9) I will change your ec2 instance type
    10) I will launch ec2 instance for you on AWS or gcp

    keywords : 
    "keyword 1": aws
    "keyword 2": ec2 instance

    user: devops
    you: 1) I will be your devops guy will do any task for you related to it
    2) I will be your AWS solutions architect and devops engineer
    3) I will do docker, kubernetes and devops related work
    4) I will provide azure devops security job support
    5) I will do your AWS, cloud work, solution architect, devops ,ec2,AWS lambda, route 53
    6) I will do devops and system administration work for you
    7) I will build your azure devops ci cd yaml classic pipelines
    8) I will remotely do linux administration and devops
    9) I will do a docker jenkins kubernetes AWS and devops related work
    10)I will do consulting for AWS architecture and devops automation

    keywords:
    "keyword 1": devops
    "keyword 2": cloud devops

    user: background photo
    you: 1) I will cut out image background remove professionally image editing
    2) I will do photo editing and retouching with background change
    3) I will do professional photoshop editing, background remove, photo retouching, enhance
    4) I will do photoshop bulk images editing and complex background removal
    5) I will delete, erase picture background from image and do photoshop editing 
    6) I will cut out images background removal photo edit
    7) I will photo editing and transparent or white background 20 images
    8) I will background remove and do bulk photo editing in 24 hours
    9) I will do professional photo editing and background removal in photoshop
    10) I will do product photo editing and background removal

    keywords: 
    "keyword 1": background photo

    
    user: python
    you: 1)I will create a python program or python script
    2) I will develop gui in python using tkinter or pyqt
    3) I will be your python django developer, sql, mongodb database
    4) I will create your application with python
    5) I will do python based projects, scripts, web scraping for you
    6) I will write, edit, review python program code 
    7) I will do ai chatbot, machine learning, python projects in python
    8) I will be python programmer for your python assignments and tasks
    9) I will write blender python scripts, addons and automatations
    10) I will do python web scraping script for data extraction anytime

    keywords: 
    "keyword1": python
    "keyword2": python program

    You got the point. and you can see all the titles are starting with 'I will' and all the keywords I have written are not exceeding the character limit which is 20, so the point is uptill 20 characters you can give keywords but don't exceed the character limit. make sure you do that too.
    
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