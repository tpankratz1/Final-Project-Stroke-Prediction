# Stroke Prediction — Final Project

### Team members:
- Janice Courtois
- Alex Norgren
- Tom Pankratz
- Rachel Rautenberg

### Selected topic
The goal of this project is to predict which factors may correlate (and possibly contribute) to higher stroke mortality rates within the United States, looking at any variances by region, state and county. Factors which we'll be exploring and training and testing through a machine learning model include:

Health-related factors:
- Smoking
- Obesity
- Access to healthy foods
- Access to exercise opportunities
- Primary care availability
- Availability of mental health providers

Social-related factors:
- College education
- Unemployment
- Income	
- Violent crime rate
- Air pollution
- Length and type of commute to work
- Urban vs. rural

### Reasons for selecting topic
All four team members work in health care at Mayo Clinic, so there was a desire to answer questions related to our industry. Also, several team members have family members who have had strokes, including a grandfather and a father, so the topic is personal as well and any insights gleaned will be helpful to better understand various factors that could lead to a stroke.

### Source data:

- Stroke Mortality Data Among US Adults (35+) by State/Territory and County (2018)
    - Data.gov
    - Publisher: Centers for Disease Control and Prevention
    - This dataset is intended for public access and use.
    - https://catalog.data.gov/dataset/stroke-mortality-data-among-us-adults-35-by-state-territory-and-county-2017-2019-d738a
- County Health Rankings (2018)
    - Countyhealthrankings.org
    - Publisher: University of Wisconsin Population Health Institute (Program: County Health Rankings & Roadmaps (CHR&R))
    - https://www.countyhealthrankings.org/explore-health-rankings/rankings-data-documentation/national-data-documentation-2010-2019

### Questions hoped to get answered:
To what extent do factors listed above correlate to higher stroke mortality rates? What differences can be uncovered by region, state and county?

## Technologies Used:

### Data Cleaning and Analysis
Pandas will be used to clean the data and perform an exploratory analysis. Further analysis will be completed using Python.

### Database Storage
PostgreSQL is the database we intend to use, connected to AWS.

### Machine Learning
SciKitLearn is the ML library we'll be using to create a classifier. Our training and testing setup is ___. [Extra ML verbiage will be added here].

### Dashboard
We intend to either integrate D3.js or use Tableau for a fully functioning and interactive dashboard displayed on a web page, highlighting results from the data and machine learning exercises. We also plan to include an interactive web form to gather user input to run through our machine learning module, using Flask and hosted on PythonAnywhere.com.

## Segment 2 Deliverables (May 29)

### Presentation

- Content
  - The presentation outlines the project, including the following:
  - Selected topic
  - Reason topic was selected
  - Description of the source of data
  - Questions the team hopes to answer with the data
  - Description of the data exploration phase of the project
  - Description of the analysis phase of the project

- Slides
  - Presentations are drafted in Google Slides.


### GitHub Repository

- Main Branch
  - All code in the main branch is production-ready. The main branch should include:
    - All code necessary to perform exploratory analysis
    - Some code necessary to complete the machine learning portion of project

- README.md
  - README.md should include:
    - Description of the communication protocols
    - Outline of the project (this may include images, but they should be easy to follow and digest)

- Individual Branches
  - Requirements for the individual branches follow:
    - At least one branch for each team member
    - Each team member has at least four commits for the duration of the second segment (eight total commits per person)

### Machine Learning Model
  - The team members are expected to submit the code for the machine learning model, as well as the following:
    - Description of preliminary data preprocessing
    - Description of preliminary feature engineering and preliminary feature selection, including the decision-making process
    - Description of how data was split into training and testing sets
    - Explanation of model choice, including limitations and benefits

### Database Integration
  - The team members are expected to present a fully integrated database, including the following:
    - Database stores static data for use during the project
    - Database interfaces with the project in some format (e.g., scraping updates the database)
    - Includes at least two tables (or collections, if using MongoDB)
    - Includes at least one join using the database language (not including any joins in Pandas)
    - Includes at least one connection string (using SQLAlchemy or PyMongo)
    - If you use a SQL database, you must provide your ERD with relationships.

### Dashboard
  - A blueprint for the dashboard is created and includes all of the following:
    - Storyboard on a Google Slide(s)
    - Description of the tool(s) that will be used to create the final dashboard
    - Description of interactive element(s)


## Segment 1 Deliverables (May 15)

### Summary
The team pivoted mid-week to change the approach to the project, including the sources for our data, and increase the amount of data we plan to run through a machine learning model. The "plumbing" has been set up with Python, PostgreSQL and AWS, and now the work begins to clean the data, merge and create final tables in the database, and then continue to test the machine learning model(s).

### Presentation
See above

### GitHub

- Communication protocol
    - The team is communicating regularly via the following tools:
        - Slack channel
        - Tuesday & Thursday class times, 7 pm CST
        - Daily touchpoints, 8:30 pm CST
- Each team member has created a GitHub branch
- Each team member has at least four commits

### Machine Learning Model

- A provisional machine learning model has been created (see very preliminary .ipynb draft file in GitHub repository)
    - It takes in data from the provisional database (PostgreSQL)
    - It outputs labels for input data

        ![Original attempt](Resources/updated_ML_to_Database.PNG)

### Database

- A provisional database has been created (PostgreSQL)
    - Sample data has been added

        ![Original attempt](Resources/database_table1_mockup.jpg)

    - A draft machine learning module is connected to the provisional database (see screenshot above within "Machine Learning Model" section)





