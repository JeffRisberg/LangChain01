from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain


information = """
"""

if __name__ == "__main__":
    print("Hello LangChain")

    summary_template = """
      Given the information {information} about a person, I want to you create:
      1. a short summary of the person
      2. two interesting facts about the person

    """

    summary_prompt_template = PromptTemplate(
        input_variables = "information", prompt_template = summary_template)

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain)



