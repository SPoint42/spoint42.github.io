#!/bin/bash
~/.venv/bin/activate
~/.venv/bin/python3 pocGemini.py -o $1 -m gemini-2.0-flash
~/.venv/bin/python3 pocGemini.py -o $1 -m gemini-2.5-flash-preview-05-20
#~/.venv/bin/python3 pocGemini.py -o $1 -m gemini-2.5-pro-preview-03-25
#~/.venv/bin/python3 pocGemini.py -o $1 -m gemma-3n-e4b-it


