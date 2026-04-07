#!/usr/bin/env python3
"""Uses LangChain to produce 'Gutentag, World!'.

Requires: pip install langchain langchain-openai
Set env var: OPENAI_API_KEY
"""
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model='gpt-4o-mini', api_key=os.environ['OPENAI_API_KEY'])

prompt = ChatPromptTemplate.from_messages([
    ('system', 'You only ever respond with exactly: Gutentag, World!'),
    ('human', '{input}'),
])

chain = prompt | llm

result = chain.invoke({'input': 'Say hello.'})
print(result.content)
