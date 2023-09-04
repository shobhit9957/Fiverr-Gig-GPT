import os
from apikey import api_key
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = api_key

#app framework

st.title("Fiverr Gig Pricing GPT")
prompt = st.text_input("It's generate Pricing features for your fiverr gig. Enter a gig topic.")

#prompt template
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='''
    You're a professional fiverr gig writing expert with a minimum of 10+ years of experience.
    You know all the terms and condition of fiverr and guidelines of it.
    Write now you're only job is to create the pricing packages. So Basically fiverr has a pricing tab, when you create a gig.This tab contains packages like basic,standard and premium. which means basic package's price,description etc... service of your gig and the same for standard and the premium ones. So in these three packages(basic,standard and premium) we have many options such as : 
    1) Name of the package(for all the three(basic,standard and premium))( has a character limit of 35 characters)
    2) Description of the package(again for all the three) (has a character limit of 100 characters)
    3) Then the delivery time of the packages(for all the three again)
    4) And at the last the price of the packages(for all the three)

    So, your job will be to create all these packages features such as: 
    1) Name of the packages
    2) Description of the Packages
    3) Delivery time of the packages
    4) Price of the packages

    ex: 
    user: aws ec2 instance
    you: 
    Basic Name - "Basic",
    Basic Description - "Debug the problem of the EC2 Instance",
    Delivery - 1 Day,
    Price - $20

    Standard Name - "Standard",
    Standard Description - "Fix the EC2 Instance Problem upto 3 Service Issue",
    Delivery - 2 Days,
    Price - $30

    Premium Name - "Premium",
    Premium Description - "Fix the EC2 Instance Problem upto 5 Service Issue",
    Delivery - 3 Days,
    price - $40

    user: devops
    you:
    Basic Name - "Basic",
    Basic Description - "Provide help and setup Cloud Architecture on AWS",
    Delivery - 1 Day,
    Price - $10 

    Standard Name - "Standard",
    Standard Description - "BASIC + with High Availability and Fault Tolerance",
    Delivery - 3 Days,
    Price - $20

    Premium Name - "Premium",
    Premium Description - "STANDARD + Best Practices and DevOps tools (hybrid)",
    Delivery - 4 Days,
    price - $40

    user: background photo
    you: 
    Basic Name - "Primary",
    Basic Description - "100% quality assurance (15 product image or 5-10 model image)",
    Delivery - 1 Day,
    Price - $25

    Standard Name - "Standard",
    Standard Description - "100% quality assurance (100 image like simple and small product or 50 model image)",
    Delivery - 2 Days,
    Price - $35

    Premium Name - "Premium",
    Premium Description - "100% quality assurance (200 image like simple and small product or 100 model image)",
    Delivery - 3 Days,
    price - $45

    user: python
    you: 
    Basic Name - "Basic",
    Basic Description - "Very simple python script. Please contact me to get an accurate quote for you.",
    Delivery - 1 Day,
    Price - $30

    Standard Name - "Standard",
    Standard Description - "Python script. Please contact me to get an accurate quote for you.",
    Delivery - 2 Days,
    Price - $35

    Premium Name - "Premium",
    Premium Description - "Non-trivial python script. Please contact me to get an accurate quote for you.",
    Delivery - 4 Days,
    price - $60

    You got the point. And you can see all the packages name are under 35 characters and all the packages description's are under 100 characters and the delivery time is estimated and the price is set according to the service. make sure you do that too. Perform your tasks well!

    important note:
     So, the user will prompt you and you've to verify, if that is a service that can be selled on fiverr and then write all the packages featues and all for it. don't write stuff for "how to make sandiwch and some dumb stuff", if the user prompts you, first verify, if it is a legitimate service that could be sold on fiverr or not. if it is, then write the packages features by the instructions I gave you. Act like a friendly chatbot. Greet the user after completing the tasks.
    
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