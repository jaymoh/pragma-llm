import sys

import constants
from langchain import hub
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.vectorstores import Chroma, FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

# pick query from user input
query = sys.argv[1]
print(query)

# Samples CSV files from: https://www.datablist.com/learn/csv/download-sample-csv-files
loader = CSVLoader(file_path='data.csv', csv_args={
    'delimiter': ';',
    'quotechar': '"',
    'fieldnames': ['Index', 'Organization Id', 'Name', 'Website', 'Country', 'Description', 'Founded', 'Industry', 'Number of employees']
})

data = loader.load()

faiss_index = FAISS.from_documents(data, OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = faiss_index.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

# you can change gpt models
# https://platform.openai.com/docs/models/gpt-3-5
llm = ChatOpenAI(model_name="gpt-4-1106-preview", temperature=0)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# python chatcsv.py "List names of Organizations dealing with Building Materials in bullet points."
# python chatcsv.py "Name of organization with the highest number of employees"
print(rag_chain.invoke(query))

