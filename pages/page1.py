import streamlit as st

from openai import OpenAI
# Custom CSS to remove padding

st.set_page_config(layout="wide")
# st.markdown(
#         """
#             <style>
#             .st-emotion-cache-1jicfl2 {
#             width: 100%;
#             padding: 1rem 1rem 1rem;
#             min-width: auto;
#             max-width: initial;
#             }
#         """,
#             unsafe_allow_html=True,
#         )

YOUR_API_KEY = "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"
topics = [
            "Waaree Technologies Ltd",
            "Identixweb Ltd",
            "Infonative Solutions Ltd",
            "Toss the Coin Ltd",
        ]
rIndex=2
feature_message = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant."
"Rules:"
"1. Provide only the final answer. It is important that you do not include any explanation on the steps below."
"2. Do not show the intermediate steps information."

"Steps:"
"1. Fetch the details about the Indian SME indicated by the user. Also check any annual report available"
"2. Write a brief and natural introduction based on the details gathered on the company."
"3. Include the following information : when the company was formed, if it is part of any group"
"4. Also include : number of employes, if the company is making profit, any news about the promotors"
"5. It should also cover the annual revenue, percentage of promoter holding etc"

        ),
    },
    {   
        "role": "user",
        "content": (
            topics[rIndex]
        ),
    },
]

market_performance_message = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant."
"Rules:"
"1. Provide only the final answer. It is important that you do not include any explanation on the steps below."
"2. Do not show the intermediate steps information."

"Steps:"
"1. Fetch the details from the BSE SME Market. Highlight the companies with top turnover, volume and trade"
"2. Write a 2 liner about each highlights in a natural language"

        ),
    },
    {   
        "role": "user",
        "content": (
            "1. What is the current value of BSE SME IPO. How much it changed from the previous session."
            "Provide the information in the following format"
             "S&P BSE SME IPO (BSE: 1146): 93290.24, Change :453.20(0.49%),16 May, 2025 3:59 PM (IST)"            
             "2. Get the closing price of the scrip for the last 5 sessions int he following JSON format that can be used to populate the graph :"
             "Date, Closing price"
        ),
    },
]

market_graph_message = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant."
"Rules:"
"1. Provide only the final answer. It is important that you do not include any explanation on the steps below."
"2. Do not show the intermediate steps information."

"Steps:"
"1. Fetch the details from the BSE SME Market. "
"2. Output should be in the following JSON format with no addditional text"
'{ [ {"Date": "May 16, 2025", "Closing Price": 93290.24},]}'

        ),
    },
    {   
        "role": "user",
        "content": (
            "1. Get the closing price of the scrip S&P BSE SME IPO (BSE: 1146) for the last 5 sessions int he following JSON format that can be used to populate the graph :"
             "Date, Closing price"
        ),
    },
]

news_latest_message = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant."
"Rules:"
"1. Provide only the final answer. It is important that you do not include any explanation on the steps below."
"2. Do not show the intermediate steps information."

"Steps:"
"1. Fetch the details on the companies listed in the BSE SME Market. Get the latest news on these companies and or their promotorrs"
"2. List each news in 2 liner in natural language. If there is no news within the last one month, do not include it "
        ),
    },
    {   
        "role": "user",
        "content": (
             ' '.join(topics)
        ),
    },
]
def callapi(message):
    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")
    # chat completion without streaming
    response = client.chat.completions.create(
    model="sonar-pro",
    messages=message,
    )
    return response


#Page display
tempname=st.session_state['username']
st.header("Welcome to _"+ tempname+"'s_ own SME page", divider="blue")

#st.write(response["choices"][0]["message"]["content"])
if 0:
    response=callapi(feature_message)
    st.write(str(topics[rIndex]))
    st.write(response.choices[0].message.content)
    st.write("References:")
    st.write(response.citations)
# chat completion with streaming
#response_stream = client.chat.completions.create(
#    model="sonar-pro",
#    messages=messages,
#    stream=True,
#)
#for response in response_stream:
#    print(response)
#    st.write("Hello world:")
#    st.write(response)

import pandas as pd
import json
# index prices
# featured SME
# recent news
 
# graph 
if 0:
    data= response.choices[0].message.content
    datajson= json.loads(data)
    df = pd.DataFrame.from_dict(datajson, orient='columns')
    st.dataframe(df) 
    st.table(df)
    #st.line_chart(df)
    st.line_chart(
    df,
    x="Date",
    y=["Closing Price"],
    color=["#FF0000"],  # Optional
)
    


if 1:
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Infonative Solutions Ltd")
        st.caption("Featured SME")
        st.write("Infonative Solutions Ltd is an Indian e-learning company that develops and designs e-learning content, services, and courseware, including cloud-based Learning Management Systems (LMS). The company was incorporated in 2014 and is a part of the BSE SME IPO segment[2]. It is headquartered in New Delhi, with operational offices also in Bengaluru[3][5].")
        st.write("Infonative Solutions is not part of any large corporate group but was founded by Yogeshh Goel, Saurabh Kathuria, and Abdur Rauf Rahmani[4]. The company employs more than 150 professionals, including instructional design experts, media specialists, and programmers[1].")
        st.write("The company is profitable, reporting a net income of ₹1.45 crore (14.50 million INR) in the most recent fiscal year, with annual revenue of approximately ₹17.69 crore (176.93 million INR)[4]. The company has shown improvement in financial health, notably reducing its debt and improving its debtor days from 48.9 to 31.8 days over the last period[2].")
        st.write("As of May 2025, Infonative Solutions Ltd has a market capitalization of about ₹45.1 crore, and its stock price is around ₹38.10. The promoter holding has decreased by 24.8% over the last quarter, which is a notable recent change[2]. There are no recent significant news reports about the promoters themselves in the provided data.")
    with col2:
        st.subheader("SME")

@st.cache_data(allow_output_mutation=True)
def UserList():
    return []

chat=UserList()
name = st.sidebar.text_input("UserName")
message = st.sidebar.text_area("UserDescription")
if st.sidebar.button("Switch User"):
    chat.append((name,message))

if len(chat) > 10:
    del(chat[0])

try:
    names, messages = zip(*chat)
    chat1 = dict(Name = names, Message =  messages)
    st.table(chat1)
except ValueError:
    st.title("Enter your name and message into the sidebar, and post!")    