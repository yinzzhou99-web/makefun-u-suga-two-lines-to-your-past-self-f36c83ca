import os
from pathlib import Path

TEXT = (
    "On that Tuesday night in March, don't say \"I'll do it tomorrow\" when "
    "the application is due at midnight.\n"
    "The site crashed at 11:58, and the scholarship went to the girl who "
    "clicked send while you were still deciding whether to sleep on it."
)


def main():
    out = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    target = out / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    os.chmod(target, 0o644)


main()
