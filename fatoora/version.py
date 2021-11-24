__all__ = "version", "version_info"

version = "1.2.0"


def version_info() -> str:
    import platform
    import sys
    from pathlib import Path

    info = {
        "fatoora version": version,
        "install path": Path(__file__).resolve().parent,
        "python version": sys.version,
        "platform": platform.platform(),
    }
    return "\n".join(f"{key}:{val}" for key, val in info.items())
