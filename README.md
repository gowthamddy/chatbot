# Cricket Knowledge Chatbot 🏏

A conversational AI chatbot built using **LangChain**, **OpenAI embeddings**, and **FAISS** to answer questions about cricket statistics and player performance.

---

## Features
- Conversational interface for cricket-related queries.
- Retrieval-Augmented Generation (RAG) pipeline to generate answers.
- Interactive chat interface powered by **Streamlit**.
- Persistent memory for conversation history.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.7+
- `langchain`
- `openai`
- `faiss-cpu`
- `pandas`
- `streamlit`
- `python-dotenv`

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/gowthamddy/chatbot.git
   cd chatbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the project root.
   - Add your OpenAI key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

---

## Project Structure

```
.
├── model.py                # Core chatbot implementation using LangChain
├── app.py                  # Streamlit app for user interaction
├── requirements.txt        # List of dependencies
└── README.md               # Project documentation
```

---

## RUN

### Run the Chatbot
To start the chatbot application:
```bash
streamlit run app.py
```

### Ask Questions
Examples of cricket-related questions you can ask:
- "Who scored the most runs in Test cricket?"
- "How many centuries did R Dravid (ICC/INDIA) score?"
- "Who played the most Test matches?"
- "What is the highest individual score?"

---

## Sample Outputs
- **Q**: "Who scored the most runs in Test cricket?"
  - **A**: "The player with the most runs in Test cricket is SR Tendulkar (INDIA) with 15,921 runs."

