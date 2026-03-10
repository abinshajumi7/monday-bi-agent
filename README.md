# Monday.com Business Intelligence Agent
Overview

This project is a simple business intelligence agent that connects to Monday.com boards and answers basic questions about deals and work orders.

The application fetches data using the Monday.com GraphQL API, processes it with Python and Pandas, and displays the results through a Streamlit web interface.

Features

Reads data from Monday.com boards

Works with both Deals and Work Orders boards

Handles missing or incomplete data

Shows basic insights such as total deals and status distribution

Simple conversational interface using Streamlit

Tech Stack

Python

Streamlit

Pandas

Monday.com GraphQL API

Project Structure
app.py            Streamlit application
monday_api.py     Monday API integration
query_engine.py   Data processing logic
requirements.txt  Project dependencies
README.md         Project documentation
Running the Project

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py
Live Demo

Streamlit App:
https://monday-bi-agent.streamlit.app

Note

This project was developed as part of a technical assignment to demonstrate integration with Monday.com data and basic business intelligence functionality.
