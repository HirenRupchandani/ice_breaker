from typing import Tuple
import streamlit as st
from dotenv import load_dotenv
import os
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agents import lookup as linkedin_lookup_agent
from output_parsers import summary_parser, Summary


def ice_break(name: str, position: str="Data Analyst") -> Tuple[Summary, str]:
    # linkedin_username = linkedin_lookup_agent(name=name)
    # linkedin_data = scrape_linkedin_profile(profile_url=linkedin_username)
    summary_template = """
        Given the LinkedIn information {information} about a person, I want you to create:
        1. A short summary about the person in 3 sentences.
        2. A few interesting facts about them.
        3. Rate the person's profile for a {position} Position from 1-10 with an explanation. Be a little strict about the rating and justify your rating.
        
        \n{format_instructions}
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information", "position"],
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()})

    # temperature decides how creative the model will be. 0 indicates it won't be creative
    llm = ChatOpenAI(temperature=1, model_name='gpt-3.5-turbo-0125')
    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    # LCL?
    chain = summary_prompt_template | llm | summary_parser
    linkedin_data = scrape_linkedin_profile()

    res: Summary = chain.invoke(input={"information": linkedin_data, "position": position})
    print('Result is here')
    print(res)
    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_break(name="Hiren Rupchandani")
