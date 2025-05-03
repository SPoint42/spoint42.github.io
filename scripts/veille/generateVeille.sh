#!/bin/bash
~/.venv/bin/activate
~/.venv/bin/python3 pocGemini.py -o $1
~/.venv/bin/python3 pocGemini.py -o $1 -m gemini-2.5-flash-preview-04-17
~/.venv/bin/python3 pocGemini.py -o $1 -m gemini-2.5-pro-exp-03-25
~/.venv/bin/python3 pocGemini.py -o $1 -m gemma-3-27b-it


