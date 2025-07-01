# Kismet Fortune 🔮

> *An evolutionary take on the classic `fortune-mod` command*

Kismet is a modern Python CLI tool that generates personalized fortunes, quotes, and wisdom using Google's Gemini AI. Get a touch of serendipity in your terminal with AI-powered insights.

## ✨ Features

- 🤖 **AI-Generated Content** - Powered by Google's Gemini API
- 📄 **Multiple Formats** - Plain text and JSON output
- 🎯 **Customizable Prompts** - Tailor fortunes to your needs
- 🔒 **Secure** - Environment-based API key management
- ⚡ **Fast & Modern** - Built with Typer and async support
- 🧪 **Well-Tested** - Comprehensive test coverage

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/kismet-fate-fortune.git
cd kismet-fate-fortune

# Install with Poetry (recommended)
poetry install

# Or with pip
pip install -e .
```

### Setup API Key

```bash
# Set your Gemini API key
export GEMINI_API_KEY="your-api-key-here"

# Or add to your shell profile for persistence
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
```

## 📖 Usage

### Basic Commands

```bash
# Get a random fortune
fortune-ai

# Custom prompt
fortune-ai "Give me wisdom about coding"

# JSON output for scripting
fortune-ai --format json "motivational quote"

# Check version
fortune-ai --version
```

### Example Output

```bash
$ fortune-ai "wisdom about life"

"The journey of a thousand miles begins with a single step, but remember 
that even the longest journey is made up of individual moments of choice."

— Lao Tzu (adapted)
```

```bash
$ fortune-ai --format json "coding wisdom"
{
  "fortune": "Code is like humor. When you have to explain it, it's bad.",
  "prompt": "coding wisdom"
}
```

## 🛠️ Development

### Running Tests

```bash
# Run all tests
poetry run pytest

# With coverage
poetry run pytest --cov=kismet_fortune
```

### Project Structure

```
kismet-fate-fortune/
├── kismet_fortune/
│   ├── __init__.py      # Package interface
│   ├── cli.py           # Command-line interface
│   ├── fortune.py       # Core fortune generation
│   └── __main__.py      # Entry point
├── tests/
│   └── test_fortune.py  # Test suite
├── pyproject.toml       # Project configuration
└── README.md           # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- Inspired by the original `fortune-mod` utility
- Built with [Typer](https://typer.tiangolo.com/) for the CLI
- Powered by [Google's Gemini API](https://ai.google.dev/)

---

*"Fortune favors the bold, but Kismet favors the curious."* ✨ 
