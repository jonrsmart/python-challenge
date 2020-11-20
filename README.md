# Python Challenge - CWRU Bootcamp Assignment # 3

## Background

There were two primary assignments, PyPoll and PyBank and two bonus assignments PyBoss and PyParagraph. Summaries of techniques used are below: 

## PyBank

In this assignment we were tasked with summarizing financial data reported as net profit on a monthly basis over a significant length of time and reading the data from a CSV file. 

The trickiest part for this excercise was calculating the average change from month to month in net profit. I accomplished this by appending each months profits to a new list named 'revenue.' I then created a for loop to go through the list, subtracting the next month from the current month to calculate the change and then appending the result to a new list called 'monthly_change.' Example output is below:

## PyPoll

In this excercise I was tasked with going through election data and determining the total votes, votes per candidate and winning candidate. 

## Hints and Considerations

* Consider what we've learned so far. To date, we've learned how to import modules like `csv`; to read and write files in various formats; to store contents in variables, lists, and dictionaries; to iterate through basic data structures; and to debug along the way. Using what we've learned, try to break down your tasks into discrete mini-objectives. This will be a _much_ better course of action than spending all your time looking for a solution on Stack Overflow.

* As you will discover, for some of these challenges, the datasets are quite large. This was done purposefully, as it showcases one of the limits of Excel-based analysis. While our first instinct, as data analysts, is often to head straight into Excel, creating scripts in Python can provide us with more robust options for handling "big data".

* Write one script for each dataset provided. Run your script separately to make sure that the code works for its respective dataset.

* Feel encouraged to work in groups, but don't shortchange yourself by copying someone else's work. You get what you put in, and the art of programming is extremely unforgiving to moochers. Dig your heels in, burn the night oil, and learn this while you can! These are skills that will pay dividends in your future career.

* Start early, and reach out for help often! Challenge yourself to identify _specific_ questions for your instructors and TAs. Don't resign yourself to simply saying, "I'm totally lost." If you need help, reach out because we're happy to help. But, come prepared and show us what you have done and your thought process.

* Always commit your work and back it up with GitHub/GitLab pushes. You don't want to lose hours of your work because you didn't push it to GitHub/GitLab every half hour or so.

  * Ensure your repository has regular commits (i.e. 20+ commits) and a thorough README.md file



## Copyright

Trilogy Education Services © 2019. All Rights Reserved.
