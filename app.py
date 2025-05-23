import streamlit as st

from openai import OpenAI
# Custom CSS to remove padding

# Set page config
st.set_page_config(
    page_title="SME Curio - BSE SME IPO Index Tracker",
    page_icon="📈",
    layout="wide"
)

# App title and description
st.title("BSE SME IPO Index Real-Time Tracker")
st.markdown("### Where SME Curiosity Meets Opportunity")
st.markdown("---")


YOUR_API_KEY = "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"
topics = [
            "Waaree Technologies Ltd",
            "Identixweb Ltd",
            "Infonative Solutions Ltd",
            "Toss the Coin Ltd",
        ]
import random
rIndex=random.randint(0, 3)
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
"1. Fetch the details from the BSE SME Market."
"2. share the information in the following JSON format with no addditional text"
'{"index_value": 97095.12,  "timestamp": "2025-05-22T15:18:54Z",  "change": 1309.48,  "change_percent": 1.37,  "open": 94057.38,  "high": 94355.02,  "low": 93101.41,  "prev_close": 92837.04}'

        ),
    },
    {   
        "role": "user",
        "content": (
            "Give me the latest value of the BSE SME IPO index as of now in JSON format with keys"
             "index_value,timestamp, change, change_percent , open, high, low, prev_close"
        ),
    },
]

weekly_price_message = [
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant."
"Rules:"
"1. Provide only the final answer. It is important that you do not include any explanation on the steps below."
"2. Do not show the intermediate steps information."

"Steps:"
"1. Fetch the details from the BSE SME Market. "
"2. Do not include any code block formatting, no triple backticks, and no language tags. Output only raw JSON."
'{ [ {"Date": "May 16, 2025", "Closing Price": 93290.24},]}'

        ),
    },
    {   
        "role": "user",
        "content": (
            "1. Get the closing price of the scrip S&P BSE SME IPO (BSE: 1146) for the last 10 sessions in the following JSON format that can be used to populate the graph :"
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
# cola,colb=st.columns(2)
# with cola:
#     st.header("Welcome to _Your_ own SME page", divider="gray")
# with colb:
#     st.write("BSESME IPO 97,095.12 +1,309.48 +1.37%")        

#Featured SME
if 1:
    response=callapi(feature_message)
    st.write("Featuresd SME")
    st.write("Company Name: " + topics[rIndex])
    #st.write(str(topics[rIndex]))
    st.write(response.choices[0].message.content)
    st.write("References:")
    st.write(response.citations)

import pandas as pd
import json

if 1:
    response=callapi(news_latest_message)
    st.write("SME News")
    data= response.choices[0].message.content
    st.write(data)
    
if 1:
    response=callapi(weekly_price_message)
    st.write("My Graph")
    data= response.choices[0].message.content
    #st.write(data)
    print(data)
    datajson= json.loads(data)
    df = pd.DataFrame.from_dict(datajson, orient='columns')
    #st.dataframe(df) 
    #st.table(df)
    
    st.line_chart(
    df,
    x="Date",
    y=["Closing Price"],
    color=["#FF0000"],  # Optional
)
# Read the script list from 
if 1:
    infile = open('LIST_BSE_SME2.txt', 'r')
    firstLine = infile.readline()
    scriptlistforCMP=[
    {
        "role": "system",
        "content": (
            "You are a helpful AI assistant."
"Rules:"
"1. Provide only the final answer. It is important that you do not include any explanation on the steps below."
"2. Do not show the intermediate steps information."

"Steps:"
"1. Fetch the details from the BSE SME Market.For the listed companies get the details from latest trading day from BSE SME market in the following JSON format that can be used to populate the list :"
"Company Name,  Closing Price,  Number of trades" 
"2. Output should be in the following JSON format with no addditional text"
'[{"Company Name": "Infonative Solutions Ltd", "Closing Price": 123.05, "Number of trades":200},'
'{"Company Name": "Infonative Solutions Ltd", "Closing Price": 123.05, "Number of trades":200} ]'

        ),
    },
    {   
        "role": "user",
        "content": (
            ' '.join(firstLine)
            
        ),
    },
]


#the sample trial one
if 1:
    col1,col2=st.columns(2)
    with col1:
        st.subheader("Infonative Solutions Ltd")
        st.caption("Featured SME")        
        with open('TXT_Infonative Solutions Ltd.txt','r',newline='') as rf:
            content = rf.read()
            st.write(content)    
    with col2:
        response=callapi(scriptlistforCMP)
        data= response.choices[0].message.content
        #st.write(data)
        datajson= json.loads(data)
        df = pd.DataFrame.from_dict(datajson, orient='columns')
        st.dataframe(df) 
        #st.table(df)
        

# The real 1 with random topic 


# Step 3: Write to the output file
       

@st.cache_data()
def UserList():
    return []

chat=UserList()
name = st.sidebar.text_input("UserName")
message = st.sidebar.text_area("UserDescription")
if st.sidebar.button("Switch User"):
    chat.append((name,message))
    st.session_state['username'] = name
    st.switch_page("pages/page1.py")

if len(chat) > 10:
    del(chat[0])

try:
    names, messages = zip(*chat)
    chat1 = dict(Name = names, Message =  messages)
    st.table(chat1)
except ValueError:
    st.write("Enter your name and message into the sidebar, and post!")    

#the one time set ups
if 0:
        st.subheader("SME List")
        with open('LIST_BSE_SME.txt','r') as rf:
            lines = rf.readlines()
        processed_lines = [f'"{line.strip()}",' for line in lines]
        st.write(processed_lines) 
        with open('LIST_BSE_SME2.txt', "w") as file:
            file.writelines(processed_lines) 
#-------- Get the Mainboard data
import requests
from bs4 import BeautifulSoup
# Function to fetch BSE SME IPO Index data
@st.cache_data(ttl=60)  # Cache for 60 seconds
def fetch_bse_sme_ipo_data():
        
        return {
            "index_value": "95,771.49",
            "change": "+791.57",
            "change_percent": "+0.83%",
            "open": "95,039.50",
            "high": "96,049.57",
            "low": "94,927.87",
            "prev_close": "94,979.92",
            "timestamp": ''
        }

# Initialize session state for historical data
if 'historical_data' not in st.session_state:
    st.session_state.historical_data = []

# Main content area with columns
if 1:
    st.write('Today')
    response=callapi(market_performance_message)
    data= response.choices[0].message.content
    print(data)
    try:
        dictdata = eval(data)
        #st.write(dictdata["index_value"])  # 97095.12

        d_open=dictdata["open"]

        d_prev_close=dictdata["prev_close"]
        d_timestamp=dictdata["timestamp"]
    except Exception as e:
        # Handle the exception
        st.write("Error:", e)
        d_change=None
    
    # Display current value with color based on change
    try :
        d_index_value=dictdata["index_value"]
        d_change=dictdata["change"]        
        d_change_percent=dictdata["change_percent"]
        change_color = "red" if 0> d_change else "green"
        st.markdown(f"""
        # <span style='color: {change_color};'>{d_index_value}</span>
        ## <span style='color: {change_color};'>{d_change} ({d_change_percent})</span>
        """, unsafe_allow_html=True)
    except Exception as e:
        # Handle the exception
        st.write("Error:", e)


    # Display other metrics
    try:
        d_high=dictdata["high"]
        d_low=dictdata["low"]
        st.markdown("### Today's Range")
        st.progress((float(d_low) / float(d_high)))
        st.markdown(f"**Low:** {d_low} | **High:** {d_high}")
    except Exception as e:
        # Handle the exception
        st.write("Error:", e)

    # Additional metrics
    try:
        d_open=dictdata["open"]
        d_prev_close=dictdata["prev_close"]
        d_timestamp=dictdata["timestamp"]
        metrics = {
        "Open": d_open,
        "Previous Close": d_prev_close,
        "Last Updated": d_timestamp
    }
    
        for label, value in metrics.items():
            st.metric(label=label, value=value)        
    except Exception as e:
        # Handle the exception
        st.write("Temporary Error:", e)
