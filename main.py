from pathlib import Path

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(
    "I can see half a second into the future, just early enough to hear myself say 'you too' to the waiter.",
    encoding="utf-8",
)
