Project README
Hello everyone! I hope you’re all doing well. This document outlines the instructions for our project. Feel free to use your imagination; the requirements are flexible.

Joseph and I created the database and defined the relations between each table. If you’d like to learn how to set up the database in VS Code and use SQL commands, Joseph and I are here to help!

Installation
Before you get started, please install the following packages:

You can install all required packages at once by running this command in your terminal or command prompt:


pip3 install Flask mysql-connector-python pandas matplotlib mpld3 numpy

Individual Package Installation:
Flask: The web framework for building your application.


pip3 install Flask
mysql-connector-python: The MySQL database connector for Python.

pip3 install mysql-connector-python
hashlib: This is part of the Python standard library, so no installation is needed. It’s used for hashing (e.g., creating password hashes).

Pandas: A powerful data manipulation and analysis library.

pip3 install pandas
Matplotlib: A plotting library for creating visualizations.


pip3 install matplotlib

mpld3: A library to visualize Matplotlib plots in a web browser using D3.js.


pip3 install mpld3
NumPy: A fundamental package for scientific computing with Python.

pip3 install numpy

How to use git: ( If you have experience with GitHub, you can skip this step and use this as a review if needed)

Step 1: Go to the repo that Donald invited you to on the GitHub website and Press "Code" and copy the HTTPS URL there. 
Step 2: Press "Settings" and then press "Command Palette" and type "Git Clone"
Step 3: Paste the URL and press enter.
Step 4: Pick a folder or make a folder you want to save the repo into on your computer and then press "Open" after you pick a folder.
Now you can access the repo on your VSCode.

Important commands to remember:
"git pull" = get any updated information put into the repo.
"git add ." = Set up your new files or folders or updates for upload. The period is important so it grabs all of your files.
"git commit -m " " " = committing your code into the repo and adding a comment to it if you want to give everyone else a little message around it.
"git push" = pushes your code to appear on the repo.

Accessing the Database

Please install the SQLTOOLS extension on VSCode. It is the yellow cylander as an icon. This will allow you to access the database and look at it. 
Step 1: Go to the new SQLTools tab on the top left. It looks like a cylinder.
Step 2: Open up the "setup.py" file on the repo. (This contains the information for accessing the database.)
Step 3: Press the "Add New Connection" and press "MySQL".
Step 4: Plug in the information that is in the "setup.py" file into the "Connection Assistant", and save the connection when done.
Step 5: Press the green plug button next to the newly added database (It should be called sql5736933.) and enter the password.

Now you are in the database. You can use some basic MySQL commands to see the data. I highly recommend using SQLBolt.com to learn how to look at the data, or pressing the arrow pointing at the database you've connected to, and slowly you will see each database open up. 
if you go to tables and press the magnifying glass, then you will be able to open up each table and see the information.



Project Parts
Part 1: User Authentication
Implement a login page that includes username and password fields.
Allow new users to be added to the database.
Implement a feature to delete user accounts based on username input.
Part 2: Webpage Functionalities
Enable users to click on a specific disease to display information for each country.
Part 3: Aggregate Functions
Create functionalities to compare and contrast statistics using line or bar graphs.
You can select which attributes and countries to compare.
Part 4: Front-End Development
Beautify the webpage with HTML, CSS, and JavaScript according to your design preferences.
Feel free to reach out if you have any questions or need assistance!