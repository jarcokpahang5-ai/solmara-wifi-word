"""One Word for Your Wi-Fi -- make.fun entry.

One word describing the Wi-Fi: Buffering. It is always buffering --
the video, the call, the page, the will to live. The program checks
the word, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

WORD = "Buffering"

LIMIT = 30
TARGET = "/output/entry.txt"


def check_entry(word):
    """Accept exactly one word within the limit."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not word or word != word.strip():
        raise ValueError("entry must be a non-blank word")
    if " " in word or "\n" in word or "\r" in word or "\t" in word:
        raise ValueError("entry must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry must be a single alphabetic word")
    if len(word) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(word), LIMIT))
    return word


def check_shape(word):
    """The word must read as a state the Wi-Fi is stuck in."""
    if word != word.capitalize():
        raise ValueError("entry must be a single capitalised word")
    return word


def write_entry(word):
    """Print the word and store it in /output/entry.txt."""
    print(word)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(word + "\n")
    os.chmod(TARGET, 0o644)


def run():
    # Check before writing, so only a well-formed word is stored.
    write_entry(check_shape(check_entry(WORD)))


if __name__ == "__main__":
    run()
