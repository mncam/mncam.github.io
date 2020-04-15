#!/bin/sh

$jupyter nbconvert --to html --ExecutePreprocessor.enabled=True index.ipynb
$git add --all
$git commit -m "Initial commit"
$git push -u origin master

