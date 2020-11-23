# Python Challenge - CWRU Bootcamp Assignment # 3

## Background

There were two primary assignments, PyPoll and PyBank and two bonus assignments PyBoss and PyParagraph. Summaries of techniques used are below: 

## PyBank

In this assignment we were tasked with summarizing financial data reported as net profit on a monthly basis over a significant length of time and reading the data from a CSV file. 

The trickiest part for this excercise was calculating the average change from month to month in net profit. I accomplished this by appending each months profits to a new list named 'revenue.' I then created a for loop to go through the list, subtracting the next month from the current month to calculate the change and then appending the result to a new list called 'monthly_change.' 

I then printed output to terminal as well as a new text file. 

## PyPoll

In this excercise I was tasked with going through election data and determining the total votes, votes per candidate and winning candidate. In order to track the votes each candidate received I researched and learned abou the Collections module for Python. Collections.counter() allowed me to store each candidate's name as a key in a dictionary and then keep track of the votes as the values in the dictionary. 

I was then able to use sorted function to sort the dictionary based on its values, split it into lists to return the candidates and votes they received in the same order. 

Again for this excercise we read in CSV files and generated the output to both terminal and a new text file. 

## PyBoss

For the first bonus excercise it was a challenge in reformatting/arranging a CSV file. I researched the datetime module for this excercise to take a birth date column in the CSV and conver it from YYYY-mm-dd to mm/dd/yyyy. I also split a couple of columns on various delimiters and retained only portions of those columns in the output. For example, taking a full SSN and converting it from 123-45-6789 to ***-**-1234. 

## PyParagraph

For the second bonus excercise we were tasked with allowing a user to choose a text file to read and then summarizing the data on the file based on the choice of the user. I was able to make use of Regular Expressions in this task which let me split the paragraphs into sentences and words quite accurately. 
