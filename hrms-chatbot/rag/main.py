# main.py

from pipeline.ingestor import ingest
from chat.chatbot import build_chatbot, chat
import os
import sys

if __name__ == "__main__":
    if not os.path.exists("vectorstore") or not os.listdir("vectorstore"):
        ingest()

    print("\nBuilding chatbot...")
    chain = build_chatbot()

    print("\nHRMS Chatbot ready. Type 'exit' to quit.\n")
    while True:
        try:
            question = input("You: ").strip()
            if not question:
                continue
            if question.lower() == "exit":
                break
            answer = chat(chain, question)
            print(f"Bot: {answer}\n")
            sys.stdout.flush()
        except KeyboardInterrupt:
            print("\nExiting...")
            break