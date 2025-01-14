from google import genai
import typer
import os


# Only run this block for Google AI API
gemini_api_key = os.environ.get("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")
client = genai.Client(api_key=gemini_api_key)

# CLI commands
app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")

@app.command()
def fortune():
    chat = client.chats.create(model='gemini-2.0-flash-exp')
    response = chat.send_message('kismet, tell me my fortune')
    print(response.text)

if __name__ == "__main__":
    app()