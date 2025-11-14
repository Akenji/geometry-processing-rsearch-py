# Geometry Processing Research in Python

## Acknowledgments

This project is built based on the lessons and instructions provided by  [geometry-processing-research-in-python](https://github.com/odedstein/geometry-processing-research-in-python) excellent repository


This is a Python tutorial for basic geometry processing in Python.
In this tutorial, you will learn a quick way to get started doing geometry
processing research in Python using the [Gpytoolbox](https://gpytoolbox.org) and
[Polyscope](https://polyscope.run) libraries.



This tutorial accompanies an [SGP 2024 graduate school](https://sgp2024.github.io/program/) course.
Click on the image below to see the lecture.

[![SGP course recording](https://img.youtube.com/vi/wQU9H4lp21k/0.jpg)](https://www.youtube.com/watch?v=wQU9H4lp21k)


### What is the difference between Gpytoolbox and libigl?

Both [Gpytoolbox](https://gpytoolbox.org) and [libigl](https://libigl.github.io)
are geometry processing libraries with Python interfaces.
Libigl is a more extensive and more established geometry processing library with
a `C++` core and Python bindings to that `C++` code.
You should use libigl, it is great!
In fact, quite a few Gpytoolbox functions are based on libigl functions or wrap
libigl in some way.

Gpytoolbox is a smaller library with functions mostly written in Python that is
great for research code specifically.
It is geared towards geometry processing researchers, is easy to use, with
well-documented code that is ready for you to use in your projects immediately.
