from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

information = """
Elon Reeve Musk  is a business magnate and investor. Musk is the founder, chairman,
CEO and chief technology officer of SpaceX; angel investor, CEO, product
architect and former chairman of Tesla, Inc.; owner, chairman and CTO of X Corp.;
founder of the Boring Company; co-founder of Neuralink and OpenAI; and president of the Musk Foundation.
He is the wealthiest person in the world, with an estimated net worth of US$232 billion
as of September 2023, according to the Bloomberg Billionaires Index, and $253 billion according
 to Forbes, primarily from his ownership stakes in both Tesla and SpaceX.
"""

if __name__ == "__main__":
    print("Hello LangChain01")

    summary_template = """
      Given the information {information} about a person, I want to you create:
      1. a short summary of the person
      2. two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables = ["information"], template = summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    chain = summary_prompt_template | llm | StrOutputParser()

    print(chain.invoke(input=information))



