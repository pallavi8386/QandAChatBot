#!/usr/bin/env python
# coding: utf-8

# #### Authentication

# In[1]:


import openai
import os
from secret_key import api_key
openai.api_key = api_key


# #### Openai API Call

# In[2]:


def qa_app(input_text):
    # Create a list of messages containing the user input
    messages = [
        {
            "role": "system",
            "content": "You will be provided with a question, and your task is to answer it correctly."
        },
        {
            "role": "user",
            "content": input_text
        }
    ]

    # Generate response from the model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        max_tokens=256
    )

    # Return the generated output
    return response.choices[0].message['content']


# In[3]:


#qa_app("Why is sky blue?")


# ### Deploying the QA app

# In[5]:


#!pip install streamlit


# In[6]:


import streamlit as st
def main():
    st.title("My Question and Answers Bot")
    st.write("Ask me a question.")
    
    conversation = []
    counter=0
    
    while True:
        user_input=st.text_input("You: ",key=f'user_input_{counter}')
        if user_input:
            conversation.append({"role":"user","content":user_input})
            generated_output = qa_app(user_input)
            
            conversation.append({"role":"model","content":generated_output})
#             st.write(f"{conversation[-1]['role']}:{conversation[-1]['content']}")
            st.write(f"{conversation[-1]['content']}")
            counter+=1
        else:
            break

# In[7]:


if __name__=="__main__":
    main()


# In[ ]:




