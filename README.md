# Reading Score Calculator
The Reading Score Calculator is a web application that calculates reading scores based on raw assessment data from various standardized reading assessments. It provides a convenient way to measure reading abilities by comparing the assessment results against percentile ranges for assessments such as TOWRE, CTOPP, and more.

## About
This web application takes raw assessment data as input and calculates reading scores based on the provided data. It leverages percentile ranges specific to each standardized reading assessment to determine the corresponding reading score.

## Usage
To use the Reading Score Calculator, follow these steps:
* Install the required dependencies by running the following command:
```shell
pip install Flask==2.1.0 pandas==1.3.4
```
* Import the necessary modules and functions in your Python code:
```shell
from flask import Flask, request, send_file, render_template, send_from_directory
from importScores import importScores
import pandas as pd
```
* Set up the Flask application and define the necessary routes and endpoints to handle the assessment data.
* Utilize the importScores function from the importScores module to import and process the raw assessment data.
* Calculate the reading scores based on the imported assessment data and the corresponding percentile ranges.

Render the calculated scores in the desired format or present them to the user.

## Requirements
The Reading Score Calculator requires the following dependencies:
```shell
Flask==2.1.0
pandas==1.3.4
```
You can install these dependencies using the provided command:
```shell
pip install Flask==2.1.0 pandas==1.3.4
```

## License
The Reading Score Calculator is released under the MIT License. You are free to use, modify, and distribute the code in accordance with the terms and conditions of the license.
