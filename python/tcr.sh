#!/bin/zsh
pytest && git commit -am 'Tests passed' || git checkout src