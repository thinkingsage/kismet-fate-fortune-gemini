"""Command-line interface for Kismet Fortune."""
import json
import sys
from typing import Optional
import typer


app = typer.Typer(help="An evolutionary take on fortune-mod.")


@app.command()
def fortune(
    prompt: str = typer.Argument("Tell me my fortune", help="Prompt for fortune generation"),
    format: str = typer.Option("text", "--format", "-f", help="Output format: text or json"),
    version: bool = typer.Option(False, "--version", help="Show version")
) -> None:
    """Generate a fortune using AI."""
    if version:
        typer.echo("kismet-fortune 0.2.0")
        return
    
    try:
        from .fortune import FortuneGenerator
        generator = FortuneGenerator()
        fortune_text = generator.generate(prompt)
        
        if format == "json":
            output = {"fortune": fortune_text, "prompt": prompt}
            typer.echo(json.dumps(output, indent=2))
        else:
            typer.echo(fortune_text)
            
    except ValueError as e:
        typer.echo(f"Configuration error: {e}", err=True)
        typer.echo("Set GEMINI_API_KEY environment variable", err=True)
        sys.exit(1)
    except RuntimeError as e:
        typer.echo(f"Error: {e}", err=True)
        sys.exit(1)


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()