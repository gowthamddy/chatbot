import pandas as pd
from langchain_openai import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv


class CricketRAGChatbot:
    def __init__(self, data_path="/Users/gowtham/Downloads/AI Internship/test.csv"):
        load_dotenv()  # Load environment variables

        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Dataset not found at {data_path}")

        self.data = self._load_data(data_path)
        self.vector_store = None
        self.conversation_chain = None
        self.setup_rag_pipeline()

    def _load_data(self, data_path):
        try:
            # Load the dataset
            df = pd.read_csv(data_path)

            # Convert dataframe to text format for processing
            text_data = []
            for _, row in df.iterrows():
                # Create a dynamic text representation based on available columns
                row_data = []
                for column in df.columns:
                    if pd.notna(row[column]):  # Only include non-null values
                        row_data.append(f"{column}: {row[column]}")
                text_data.append(", ".join(row_data))

            return "\n".join(text_data)

        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")

    def setup_rag_pipeline(self):

        # Split text into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        texts = text_splitter.split_text(self.data)

        # Create embeddings and vector store
        embeddings = OpenAIEmbeddings()
        self.vector_store = FAISS.from_texts(texts, embeddings)

        # Setup memory
        memory = ConversationBufferMemory(
            memory_key='chat_history',
            return_messages=True
        )

        # Create conversation chain
        self.conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=OpenAI(temperature=0),
            retriever=self.vector_store.as_retriever(),
            memory=memory
        )

    def ask_question(self, question):
        if not self.conversation_chain:
            raise Exception("RAG pipeline not initialized. Call setup_rag_pipeline first.")

        try:
            response = self.conversation_chain({"question": question})
            return response['answer']
        except Exception as e:
            return f"Error generating response: {str(e)}"


def main():

    try:
        # Initialize the chatbot with your specific path
        chatbot = CricketRAGChatbot()

        # Sample questions to test the chatbot
        sample_questions = [
            "Who scored the most runs in Test cricket?"
            "How many centuries did R Dravid (ICC/INDIA) score?"
            "Who played the most Test matches?"
            "What is the highest individual score?"
        ]

        # Save responses to a file
        with open("chatbot_responses.txt", "w") as f:
            for question in sample_questions:
                response = chatbot.ask_question(question)
                f.write(f"Q: {question}\nA: {response}\n\n")
                print(f"Q: {question}")
                print(f"A: {response}\n")

    except Exception as e:
        print(f"Error in main: {str(e)}")


if __name__ == "__main__":
    main()