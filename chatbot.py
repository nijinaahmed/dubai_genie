from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()

#Title of the app
st.title("Dubai Trip Planner")

#Initial message
initial_message=[{"role": "system", "content": "You are a trip planner in Dubai.You are an expert in Dubai tourism locations,food,events,hotels etc.You are able to guide users to plan thier vacations to Dubai.You should respond professionally.Your name is Dubai Genie short name DG.Your response should not exceed 200 words.Always ask questions to the user and help them to plan the trip.Finally give a daywise iterinary.Deal with user professionally"},
        {
            "role": "assistant",
            "content": "Hello,my name is DG,your expert travel partner.How can i help you?"
        }
]
#Function to get response from AI
def get_response_from_llm(messages):
   completion = client.chat.completions.create(
    model="gpt-4o-mini",
     messages=messages
        )
   return completion.choices[0].message.content

#Initialising session state for messages
if "messages" not in st.session_state:
    st.session_state.messages=initial_message

#Displaying previous messages except system
for message in st.session_state.messages:
        if(message["role"] != "system"):
            with st.chat_message(message["role"]):
             st.markdown(message["content"])
#Getting user input from textbox
user_message=st.chat_input("Enter your message here")
#Appending usermessage to the excisting messages
if user_message:
    new_message={
                  "role": "user",
                  "content":user_message
                }
    st.session_state.messages.append(new_message)
 #Display user message   
    with st.chat_message(new_message["role"]):
         st.markdown(new_message["content"])

#Generating AI response after displaying user message
    response = get_response_from_llm(st.session_state.messages)
#Appending ai response
    if response:
      response_message={
          "role":"assistant", 
          "content":response
          }
    st.session_state.messages.append(response_message)
#Displaying ai response
    with st.chat_message(response_message["role"]):
       st.markdown(response_message["content"])




 