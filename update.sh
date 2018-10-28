#!/bin/bash

# create directories

mkdir -p lectures assignments

# copy lecture slides

cp "../lectures/lecture0/slides/slides.pdf" "lectures/lecture0.pdf"
cp "../lectures/lecture1/slides/slides.pdf" "lectures/lecture1.pdf"
cp "../lectures/lecture2/slides/slides.pdf" "lectures/lecture2.pdf"
cp "../lectures/lecture3/slides/slides.pdf" "lectures/lecture3.pdf"

# copy assignment reference code

cp -R "../assignments/src/reference" "assignments/"

# copy assignment 1 related things

cp -R "../assignments/assignment1" "assignments/"
