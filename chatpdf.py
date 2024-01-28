import sys

import constants
from langchain import hub
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# pick query from user input
query = sys.argv[1]
print(query)

# load pdf
loader = PyPDFLoader('Resume-James-Shisiah.pdf')
pages = loader.load()

faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = faiss_index.as_retriever()
prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

print(rag_chain.invoke(query))