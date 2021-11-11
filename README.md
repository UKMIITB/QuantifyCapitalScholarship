# QuantifyCapitalScholarship

Selected solution to Quantitative Trading Program Scholarship of Quantify Capital

Link of website: https://www.quantifycapital.in/quantitative-trading-program/scholarship  
Doc link for question: https://docs.google.com/document/d/1dY7oenuyo6fEuOTfEtfzv85T-PU6xhhITUkA0sMG_dk/edit

## Info about the solution

1. The final answers are placed in finalSolution folder
2. 3131.csv is the data to be used for Q1 & Q2
3. Q2 has been solved in 2 ways, q2.py is the pythonic way & q2_new.py is the traditional loop method

## Scholarship Test for QTP

### Instructions:

Code the following questions in your machine.

Create a new python file per question. For q1.py, q2.py q3.py and q4.py

Once completed zip the folder which contains above files and then upload it in this google form -

https://docs.google.com/forms/d/e/1FAIpQLSeogGkyV8fwQxjBxaHsjOOPTifA0MDny7POkuJGWm7ZhGEDyg/viewform?usp=sf_link

You can connect with the team on +91 89283 81567 for any queries you may have.

### Python Coding

You have been provided with a CSV file called 3131.csv. Its contains end of data for Banknifty for 13years

3131.csv

https://drive.google.com/file/d/1W4TtUur2wSHRoLR7ScpPaTZS7B3YBJqq/view?usp=sharing

Find solutions to the below mentioned question. You can chose to python package

1. Find all the expiry days for the Banknifty
   Every week Thursday is an expiry day for Banknifty. But the days on which Thursday is a holiday then Wednesday becomes expiry. If Thursday and Wednesday are both holidays then Tuesdays is the expiry date.

2. Plot a monthly percentage return heatmap for Banknifty as shown below   

<img width="655" alt="Screenshot 2021-11-11 at 10 18 50 PM" src="https://user-images.githubusercontent.com/36126610/141338449-39f2a89d-250a-4acb-9373-c4f3b907f3c8.png">  


Month % Return =( Month Closing price -Month Open Price)/Month Open Price

3. Take a date input from a user in “YYYY-MM-DD” format. Find and print the last Wednesday of the month for entered date

4. Write code which flattens the nested dictionary and prints it.
   Input
   {"a": {"b": 4}, "z": {"c": {"a": 1}, "d": 1}, "y": 3}

Output
a_b: 4
z_c_a: 1
z_d: 1
y: 3
