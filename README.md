# kismet

An evolutionary re-take on `fortune-mod`, Kismet is a modern Python command-line tool that delivers random quotations from llm generators, offering a touch of serendipity to your terminal. 

## Features

* **AI-Generated Fortunes:** Uses Google's Gemini API to generate personalized fortunes
* **Multiple Output Formats:** Support for plain text and JSON output
* **Modern CLI:** Built with Typer for a clean command-line interface
* **Secure API Key Management:** Uses environment variables for API key storage
* **Extensible Architecture:** Modular design for easy enhancement

## Installation

```bash
# Install dependencies
poetry install

# Or with pip (after cloning)
pip install -e .
```

## Setup

Set your Gemini API key:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

## Usage

```bash
kismet "Tell me my fortune"    # Generate a fortune
kismet --version               # Show version
kismet --format json "wisdom"  # Output in JSON format
```


## Acknowledgements

Inspired by the original `fortune-mod` utility and its contributors. 
