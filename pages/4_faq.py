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
    1. What kind of services do you offer as an AWS Solutions Architect?

    Answer: As an AWS Solutions Architect, I offer a variety of services, including designing and implementing AWS cloud infrastructure, system and network architecture, and troubleshooting and resolving AWS-related issues.

    2. What experience do you have as an AWS Solutions Architect?

    Answer: I have 5+ years of experience as a DevOps engineer and am AWS certified in Solutions Architect, with extensive experience in creating efficient, scalable, and cost-effective AWS infrastructures.

    3. What certifications do you hold that can help enhance the services you offer?

    Answer: Yes, I am AWS certified in Solutions Architect. This certification validates my deep understanding of AWS services and best practices, ensuring the solutions I design and implement are of the highest quality.



    user: devops
    you: 
    1. What professional experience do you have in DevOps?

    Answer: I have been working in DevOps for 5 years, successfully executing a wide range of projects. My AWS certifications validate my expertise and guarantee that the solutions I design are aligned with industry standards and optimized for performance.

    2. Why should I hire you for my DevOps projects?

    Answer: With my expertise in DevOps, I can assure you that your project will be efficiently planned and implemented, while minimizing unnecessary costs. Additionally, I provide communication, documentation, debugging and troubleshooting, to ensure that your project goes smoothly.

    3. Do you have experience working in a variety of different tools?

    Answer: I specialize in tools like Jenkins, Docker, Kubernetes, Ansible, and Terraform, which streamline processes, automate deployments, and enhance infrastructure management.


    user: graphic designing
    you: 
    1. How do you ensure the quality of your graphic design services?

    Answer: I use the latest design software and techniques to ensure a high-quality result for every project. I also offer unlimited revisions until you are completely satisfied with the results.

    2. What types of graphic design services do you offer?

    Answer: I offer a range of custom graphic design services, such as logo design, brand identity creation, web design, and illustrations.

    3. How can I be confident that I will be satisfied with the final design?

    Answer: ith my 10+ years of experience as a professional designer, I ensure that you are satisfied with the final design. If for any reason you are not satisfied, I will revise the design until it meets your expectations.


    user: web development
    you: 
    1. What expertise do you have in web development?

    Answer: I have extensive experience in web development, specializing in Tailwind and Bootstrap. I can help turn complex web design ideas into reality, creating websites that are both visually appealing and easy to navigate.

    2. What areas of my website can you help me with?

    Answer:  I specialize in designing and development of the entire website, including landing pages, e-commerce functionality, content management systems, databases, and more.

    3. What is the experience level of your web development services using Tailwind and Bootstrap?

    Answer: I have 5+ years of experience in web development with Tailwind and Bootstrap. My knowledge of these technologies allows me to create rich, interactive, and responsive web applications that are tailored to your project's needs.

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