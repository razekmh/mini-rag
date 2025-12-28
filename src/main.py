from fastapi import FastAPI

from routes import base, files

app = FastAPI()
app.include_router(base.base_router)
app.include_router(files.file_router)


def main():
    print("Hello from mini-rag!")


if __name__ == "__main__":
    main()
