"""Kismet Fortune - An evolutionary take on fortune-mod."""

__version__ = "0.1.0"

__all__ = ["FortuneGenerator", "main"]

def __getattr__(name):
    if name == "FortuneGenerator":
        from .fortune import FortuneGenerator
        return FortuneGenerator
    elif name == "main":
        from .cli import main
        return main
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")