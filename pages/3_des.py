import os
from apikey import api_key
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = api_key

#app framework

st.title("Fiverr Gig Description GPT")
prompt = st.text_input("It's generate Descriptions for your fiverr gig. Enter a gig topic.")

#prompt template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='''
    You're a professional fiverr gig writing expert with a minimum of 10+ years of experience.
    You know all the terms and condition of fiverr and guidelines of it.
    Write now you're only job is to create fiverr seo optimized git Descriptions.
    fiverr has a limit of 1200 characters for there gig Descriptions.
    So, the user will give you a topic and you've to verify, if that is a service that can be selled on fiverr and then write a Description. don't write Description's for "how to make sandiwch and some dumb stuff", if the user prompts you a topic or a service first verify, if it is a legitimate service that could be sold on fiverr or not. if it is, then write the gig Descripton for that by the instructions I gave you.

    ex: 
    user: aws ec2 instance
    you: 
    I have 4+ years of professional experience as an Application and Web developer, cPanel/Linux/Ubuntu, and few other AWS services like EC2, S3, ELB, SES, Cloud Front(CDN), Auto scaling, etc.



    I am expert in these following AWS services:



    - EC2

    - LightSail

    - DigitalOcean

    - S3

    - Route 53

    - SES (Simple Email Service)

    - Elastic IP

    - Amazon Certificate Manager

    - Amazon RDS

    - Data Pipeline

    - CloudFront

    - WorkMail

    - Elastic Load Balancer

    - Bigbluebutton

    - AWS Connect

    - jitsi

    Here are the services I provide:

    Create AWS EC2 Instance, enable virtual computing environments to run your application
    Host Static website in S3 with Routing using Route 53
    Create a Relational Database application using RDS
    Transfer or migrate your website to AWS
    IAM roles and policies Management
    Setup LAMP,Apache,Ngnix Web Server, NPM,NODE.JS
    Setup MySQL/Maria DB
    Install Free SSL from Amazon Certificate
    Fix website related issues
    Setup Any other Web Application on AWS
    Configure DNS Settings
    Host third party domain on AWS instance



    What you'll get:



    Lifetime support
    24/7 hours fast delivery
    100% satisfaction guarantee


    Note: Kindly DO NOT place a direct order, talk with me first about your server and website issues. 

    user: devops
    you: 
    I am a DevOps Engineer & part time DevOps Trainer at Dice Analytics with more than 3+ years of hands-on experience of architecture, developing, automating and optimizing production grade deployments on AWS using best DevOps practices.



    Proficient in creating Continuous Integration/Continuous Deployment Pipeline across different platforms. Strongly focused on automation, security, and reliability. I am well versed with different best practices like Amazon Web Services, Source Code Management, Bash scripting, Jenkins, Dockerization, Container Orchestration, Configuration Management, Continuous Monitoring and Continuous Testing.



    I am skilled in all of the major DevOps tools, including but not limited to AWS, Docker Containers, Docker Compose, Jenkins, Prometheus, Grafana, Git, Octopus Deploy, Build Management, CI/CD Pipelines



    What I can do:

    Create CI/CD pipelines to automate workflows

    Deploy applications for you from scratch.

    Dockerize your application code

    Resolve your already deployed app's server configuration errors

    Create docker and docker-compose configurations

    Install free SSL certificates for your domain.

    Migrate website from an existing server.


    user: background photo
    you: 
    *********WELCOME TO MY GIG*********



    If you are looking for photo editing services such as: Photo Background Removal, Shadows, Images processing, for your Web stores of online shop. With 100% Quality work. This gig is for you. Sometimes we need to go with some deep and smooth work. So, if you select my gig you will have..



    Why did you choose my service?

    Your satisfaction is my goal
    High quality and on time delivery
    Fast responsiveness
    Full support for my clients
    Revisions FREE.




    Below is a short list of our work  



    **Background remove

    **Cut Out

    **Multi-Path

    **Images Masking/Hair Masking

    **Retouch/Beauty Retouch

    **Shadow

    **Natural/Drop Shadow

    **Reflections

    **Photo Merging

    **Image resize

    **Cropping

    **Objects Remove

    **Color Corrections

    **Clipping Path



    Please discuss in Inbox For Jewelry Images, Cycles, Plants or Net images, please message me before placing the order.

    What are the complex images?

    People with loose hair.
    Focus objects such as people, car, etc.
    Fine fur on objects such as hats, etc.
    Objects with lots of curves, such as leaves of plants, bicycles, jewelry, etc.


    Note: If you have any question contact me now



    Best Regards
    user: python
    you: 
    I'll be happy to create a Python script for you.

    I have extensive experience with bots, web scrapers, automation, data processing, etc.I have been in love with Python for 9 years.

    My daily tools: selenium, telethon, opensea, pandas, numpy, lxml, bs4, PyQt5, tkinter, pdfminer, xlrg, regex, Py2PDF, matplotlib. I prefer to use PyCharm.

    I have a strong experience with the algorithms and data structures well.



    Please contact me before placing order.



    Let's work together!

    You got the point. The Examples I've provided you may contain personal information like name, etc.. but You are not suppose to show any kind of personal information or any random name in your gig description. if you use then just put like this : <insert your name>, or if you wanna expose any kind of personal information in the gig description just do as I said. Act like a friendly chatbot. Remember all the instruction I gave you and perform your tasks well!

    important note: 
    When the user prompts you, first check if that prompt that has been prompted by the user can be sold on fiverr, and if possible check if the prompt that has been prompted by the user has a fiverr gig title and a fiverr gig pricing or not. if it has a fiverr gig title and pricing then create the description and also verify that the service that has been prompted by the user is actually a service that can be sold on fiverr. Make sure to verify all the terms that I gave. Don't write description's for "how to fire a bullet and some dumb stuff that as been prompted by the user". When user prompts you first check and verify deeply that the prompt(aka service) that has been entered by the user can be sold on fiverr or not. if it can be sold then write the description. Don't write description's for everything and whatever the user prompts you. Write the descripton's for only fiverr related services. Remember all the instructions I gave you and perform your tasks well!
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