## Training Your Own AI Model

This project is inspired by TechLead's video on YouTube: [Using ChatGPT with YOUR OWN Data](https://www.youtube.com/watch?v=9AXP7tCI9PI)

Using LangChain's documentation [here](https://python.langchain.com/docs/use_cases/question_answering/quickstart)

### Steps
1. Clone the repository.
2. Install Python and pip.
3. Install the dependencies using `pip install -r requirements.txt`
4. Create an environment variable file `.env` and add the following:
    ```
    OPENAI_API_KEY=<your openai api key>
    ``
5. Change the `data.txt` file to your own data or create a new file and update the path in `chatgpt.py`
6. Run `chatgpt.py` with your query as the argument. <br/> For example: `python chatgpt.py "Which books to read on Unit Testing?"` will give you some answer based on the `data.txt` file included in the repo.
7. You can also replace the pdf file with your own Resume pdf file and change the path in `pdf2txt.py` <br/> and run with a query as the argument. <br/> For example: `python chatpdf.py "Which schools did I attend?"`.