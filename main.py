from dotenv import load_dotenv
import os

load_dotenv()


def main():
    print("Hello, LangChain!")
    print(os.environ.get("DEEPSEEK_API_KEY"))


if __name__ == "__main__":
    main()
