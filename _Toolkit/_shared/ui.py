#!/usr/bin/env python3
"""
_toolkit/shared/ui.py – Gemeinsame Terminal-UI für alle _Toolkit-Skripte.

Bietet einheitliche, minimalistische ASCII-Formatierung ohne Emojis.
"""

import sys as _sys
import shutil

_COLS = _sys.stderr.isatty() and shutil.get_terminal_size((72, 20)).columns or 72
W = min(_COLS, 66)


def header(text: str, width: int = W) -> None:
    """Box-header mit Titel."""
    inner = width - 4
    print()
    print(f"  ┌{'─' * inner}┐")
    for line in text.splitlines():
        print(f"  │ {line:<{inner - 1}}│")
    print(f"  └{'─' * inner}┘")
    print()


def section(text: str, width: int = W) -> None:
    """Trennlinie mit Abschnitts-Überschrift."""
    line = width - len(text) - 8
    print(f"  ── {text} {'─' * max(line, 2)}")


def hr(width: int = W, char: str = "─") -> None:
    """Horizontale Trennlinie."""
    print(f"  {char * (width - 2)}")


def ok(text: str) -> None:
    """Erfolgsmeldung."""
    print(f"  [OK]  {text}")


def fail(text: str) -> None:
    """Fehlermeldung."""
    print(f"  [!]  {text}")


def info(text: str) -> None:
    """Info-Meldung."""
    print(f"  [*]  {text}")


def tip(text: str) -> None:
    """Hinweis/Tipp."""
    print(f"  [ i ]  {text}")


def keyval(key: str, value: str, width: int = W) -> None:
    """Schlüssel: Wert in einheitlicher Breite."""
    print(f"  {key:<18} {value}")


def spacer(lines: int = 1) -> None:
    """Leerzeilen."""
    for _ in range(lines):
        print()


def boxed(text: str, width: int = W) -> None:
    """Text in einer Box."""
    inner = width - 6
    print(f"  ┌{'─' * (width - 4)}┐")
    for line in text.splitlines():
        print(f"  │ {line:<{inner}} │")
    print(f"  └{'─' * (width - 4)}┘")


def list_items(items: list[str], numbered: bool = False, start: int = 1) -> None:
    """Liste von Items, optional nummeriert."""
    for i, item in enumerate(items, start):
        if numbered:
            print(f"  {i:2d})  {item}")
        else:
            print(f"  \u2022  {item}")


def prompt(text: str, default: str = "") -> str:
    """Eingabeaufforderung mit optionalem Default."""
    if default:
        return input(f"  >> {text} [{default}]: ").strip() or default
    return input(f"  >> {text}: ").strip()


# ── Animation ──────────────────────────────────────────────

import threading as _threading
import time as _time


class Spinner:
    """Einfacher ASCII-Spinner für Hintergrundprozesse.

    Usage:
        with ui.Spinner("Scanning vault..."):
            time.sleep(2)  # (tatsächliche Arbeit)
    """

    CHARS = ["|", "/", "-", "\\"]

    def __init__(self, text: str = ""):
        self.text = text
        self._running = False
        self._thread = None

    def start(self):
        self._running = True
        self._thread = _threading.Thread(target=self._spin, daemon=True)
        self._thread.start()

    def _spin(self):
        i = 0
        while self._running:
            _sys.stdout.write(f"\r  {self.CHARS[i % 4]}  {self.text}")
            _sys.stdout.flush()
            _time.sleep(0.12)
            i += 1

    def stop(self, clear: bool = True):
        self._running = False
        if self._thread:
            self._thread.join(timeout=0.3)
        if clear:
            blanks = len(self.text) + 8
            _sys.stdout.write("\r" + " " * blanks + "\r")
        _sys.stdout.flush()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()
