#!/bin/zsh

./algodraw.py
./generate_readme.py >! README.md
./lcodeJquery.py
./lcodeReact.py