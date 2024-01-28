## Training Your Own AI Model

This project is inspired by TechLead's video on YouTube: [Using ChatGPT with YOUR OWN Data](https://www.youtube.com/watch?v=9AXP7tCI9PI)

Using LangChain's documentation [here](https://python.langchain.com/docs/use_cases/question_answering/quickstart)

### Steps
1. Clone the repository.
2. Install Python and pip.
3. Install the dependencies using `pip install -r requirements.txt`
4. Get your OpenAI API key from [here](https://platform.openai.com/api-keys). <br/> You will need to create an account if you don't have one already. <br/> You will also need to add a credit card to your account to use the API and purchase some credits e.g. $5.
5. Create an environment variable file `.env` and add your API key to it. <br/> For example:
    ```
    OPENAI_API_KEY=<your openai api key>
    ``
6. Change the `data.txt` file to your own data or create a new file and update the path in `chatgpt.py`
7. Run `chatgpt.py` with your query as the argument. <br/> For example: `python chatgpt.py "Which books to read on Unit Testing?"` will give you some answer based on the `data.txt` file included in the repo.
8. You can also replace the pdf file with your own Resume pdf file and change the path in `chatpdf.py` <br/> and run with a query as the argument. <br/> For example: `python chatpdf.py "Which schools did I attend?"`.