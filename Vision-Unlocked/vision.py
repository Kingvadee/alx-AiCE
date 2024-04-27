import sys
from typing import Sequence
from ollama import Message, chat

def vision_chat(path: str, question: str):
    prompt: Sequence[Message] = [
        { 'role': 'user', 'content': question, 'images': [ path ] }
    ]
    response = chat(model="llava", messages=prompt)
    print(response['message']['content'])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python vision.py <image_path> <prompt>")
        sys.exit(1)
    path = sys.argv[1]
    prompt = sys.argv[2]
    vision_chat(path, prompt)