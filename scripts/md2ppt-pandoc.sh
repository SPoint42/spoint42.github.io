#!/bin/bash
pandoc $1 -o $1.pptx --reference-doc=$2
