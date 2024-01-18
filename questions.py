import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Add your API key here

# List of questions
questions = [
    "How has the Alcoa Corporation revenue trend evolved over the last few fiscal quarters? consider its cash flow in the past fiscal year?",
    "What key metrics indicate the liquidity position of Almaden Minerals Ltd.? also elaborate that has there been a significant change in the company's financial ratios over the past two years?",
    "How has the American Assets Trust, Inc. rental income grown over the past fiscal years and what are the major components affecting American Assets Trust's cash flow from operations?",
    "What are the trends in Advance Auto Parts' gross profit margin over the last five years?",
    "How have the sales figures for The Aaron's Company trended in comparison to the industry, are there any noticeable changes in the company's key metrics, indicating potential areas of financial strength or weakness?",
    "How has American Airlines' operating income fluctuated in response to changes in revenue and expenses?",
    "What major components contribute to Ares Acquisition's revenue stream?",
    "Can you compare the financial health of Microsoft and Apple over the last four years, focusing on their balance sheets and key financial ratios?",
    "AXS First Priority CLO Bond ETF: How does the AXS First Priority CLO Bond ETF's net asset value (NAV) compare to its cash flow from operating activities?"
]

# Empty list to store question-response pairs
responses = []

# Function to get AI responses
def get_ai_response(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a financial analyst."},
            {"role": "user", "content": question}
        ],
        temperature=0.5,
        max_tokens=150
    )
    return response['choices'][0]['message']['content']

# Loop through questions, get responses, and store in list of dictionaries
for question in questions:
    response_text = get_ai_response(question)
    response_dict = {'question': question, 'response': response_text}
    responses.append(response_dict)

# Display the list of question-response pairs
for pair in responses:
    print(pair)
