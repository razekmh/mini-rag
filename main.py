from fastapi import FastAPI
from dotenv import load_dotenv
from routes import base

load_dotenv()

app = FastAPI()
app.include_router(base.base_router)


def main():
    print("Hello from mini-rag!")


if __name__ == "__main__":
    main()
