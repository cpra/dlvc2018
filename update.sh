#!/bin/bash

# create directories

mkdir -p lectures assignments

# copy lecture slides

cp "../lectures/lecture0/slides/slides.pdf" "lectures/lecture0.pdf"
cp "../lectures/lecture1/slides/slides.pdf" "lectures/lecture1.pdf"
cp "../lectures/lecture2/slides/slides.pdf" "lectures/lecture2.pdf"
cp "../lectures/lecture3/slides/slides.pdf" "lectures/lecture3.pdf"
cp "../lectures/lecture4/slides/slides.pdf" "lectures/lecture4.pdf"
cp "../lectures/lecture5/slides/slides.pdf" "lectures/lecture5.pdf"
cp "../lectures/lecture6/slides/slides.pdf" "lectures/lecture6.pdf"
cp "../lectures/lecture7/slides/slides.pdf" "lectures/lecture7.pdf"
cp "../lectures/lecture8/slides/slides.pdf" "lectures/lecture8.pdf"
cp "../lectures/lecture9/slides/slides.pdf" "lectures/lecture9.pdf"
cp "../lectures/lecture10/slides.pdf" "lectures/lecture10.pdf"
cp "../lectures/lecture11/slides.pdf" "lectures/lecture11.pdf"

cp "../exam-questions/questions.pdf" "exam-questions.pdf"

# copy assignment reference code

cp "../assignments/general.md" "assignments/"
cp "../assignments/server.md" "assignments/"
cp -R "../assignments/src/reference" "assignments/"

# copy assignment 1 related things

cp -R "../assignments/assignment1" "assignments/"

# copy assignment 2 related things

cp -R "../assignments/assignment2" "assignments/"
rm "assignments/assignment2/gradient_descent_2d_impl.py"
rm "assignments/assignment2/fn/generate.py"
rm -rf "assignments/assignment1/autotest"
rm "assignments/assignment1/points.md"

# copy assignment 3 related things

cp -R "../assignments/assignment3" "assignments/"