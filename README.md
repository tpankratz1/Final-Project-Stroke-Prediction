# Stroke Prediction — Final Project

### Team members:
- Janice Courtois
- Alex Norgren
- Tom Pankratz
- Rachel Rautenberg

### Selected topic
The goal of this project is to find out if we are able to predict which factors may correlate (and possibly contribute) to higher stroke mortality rates within the United States. Factors which we've explored, trained and tested through various machine learning models include:

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

- Are we able to predict potential stroke mortality rates based on a set of health-related or social-related factors?
- Are there certain factors that are more important than others?


## Technologies Used:

### Data Cleaning and Analysis
Python Pandas was used to clean the data and perform an exploratory analysis, and further analysis was performed using Python.

### Database Storage
PostgreSQL is the database we've used, connected to AWS via pgAdmin 4.

### Machine Learning
SciKitLearn is the ML library we'll be using. See additional comprehensive detail below under "Machine Learning Model" section.

### Dashboard
An interactive web site has been created and is hosted on pythonanywhere.com. It will include interactive dashboards built in Tableau (that will be embedded on the site via iframes). The web site also includes an interactive form, built with Flask. It will allow users to enter data for the chosen features/factors and use a machine learning model to predict stroke mortality rates based on that input data.


## Segment 2 Deliverables (May 29)

### Presentation

A presentation has been created on Google Slides, outlining the project and includes the following sections, as required. The file can be found here: https://docs.google.com/presentation/d/1E1D_wDwgtw-h_wREXM73hGIfPYEHObPIjhqgLeNW1OE/edit?usp=sharing

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
    - All code necessary to perform exploratory analysis. See files above, explained below.
    - Some code necessary to complete the machine learning portion of project. See files above, explained below.
- README.md
  - README.md should include:
    - Description of the communication protocols. See above.
    - Outline of the project (this may include images, but they should be easy to follow and digest). See above.

- Individual Branches
  - Requirements for the individual branches follow:
    - At least one branch for each team member
    - Each team member has at least four commits for the duration of the second segment (eight total commits per person)

### Machine Learning Model
  - The team members are expected to submit the code for the machine learning model, as well as the following:
    - Description of preliminary data preprocessing
      - Once our team determined that stroke mortality rates by counties within the United States was to be our target dataset, we brainstormed on possible health-related and social-related factors to research that may correlate (and possibly contribute) to higher stroke mortality rates within the United States. We did a lot of Google searches on random factors such as average days of sunlight per year, amount of drug use, number of fitness facilities per capity, number of restaurants per capita, and many more. After an extensive search, we identified the original datasets from the following two sources, with the first containing the target data, and the second containing data to be used for the features:
        - Stroke Mortality Data Among US Adults (35+) by State/Territory and County (2018)
            - Data.gov
            - Publisher: Centers for Disease Control and Prevention
            - This dataset is intended for public access and use.
            - https://catalog.data.gov/dataset/stroke-mortality-data-among-us-adults-35-by-state-territory-and-county-2017-2019-d738a
        - County Health Rankings (2018)
            - Countyhealthrankings.org
            - Publisher: University of Wisconsin Population Health Institute (Program: County Health Rankings & Roadmaps (CHR&R))
            - https://www.countyhealthrankings.org/explore-health-rankings/rankings-data-documentation/national-data-documentation-2010-2019
      - Cleaning the stroke mortality dataset:
        - The stroke mortality dataset was less extensive, but required quite a bit of cleaning and pre-processing. Python was used, using Pandas and Numpy, and here's the file: https://github.com/Norgs87/Final-Project-Stroke-Prediction/blob/main/Models%20Practice%20%26%20Cleaning%20Code/Stroke_Mortality_Cleaned.ipynb. The original dataset had 59,094 rows and 20 columns. We knew that the county ID (or FIPS) would be the common primary key in the PostgreSQL database, and thus needed to clean the data down to 3,142 rows, or the number of counties within the United States. Non-beneficial columns were dropped. Column names were renamed for clarity. Columns with additional data not needed were filtered out. Extra regions were removed, such as Puerto Rico, Guam and more. Finally, extra values not neeeded were dropped, reducing the total number of rows to the needed 3,142, and to only include 2 columns: The FIPS (primary key) and the stroke mortality rate by county.
        - The health rankings dataset, which includes social factors, was more extensive and also required a fair amount of preprocessing. Python was again used, along with Pandas and Numpy, and here's the file: https://github.com/Norgs87/Final-Project-Stroke-Prediction/blob/main/Models%20Practice%20%26%20Cleaning%20Code/Health_Rankings_Cleaned.ipynb. It initially contained 3,143 rows and 166 columns. The team spent a considerable amount of time selecting which factors to use as the features for the machine learning models, hypothesizing which ones could have the biggest influence on stroke mortality rates across the United States. The team finally chose 13 total, with 6 health-related and 7 social or environment-related. The job then began to preprocess the data down to only what was needed. To start, unwanted columns were dropped. The remaining columns were renamed for consistency. Another dataset was discovered a day later, showing percent urban vs. rural for each county, so it was loaded and then merged with the main dataset, using Pandas. Colums were then rearranged in preparation to merge with the other dataset in the PostgreSQL database.
    - Description of preliminary feature engineering and preliminary feature selection, including the decision-making process
        - The target was easily identifiable as the team seeks to develop a model that provides a stroke mortality prediction. With the datasets that we have chosen to 
            use, there will be a minimum of three [similar] models as we work through understanding what the best predictors may be for an individual.  We will build a machine learning model, using RandomForestRegressor, against all applicable features of the dataset.  We also will copy / edit the working model two times;
            one time to run the model against clearly health related features such as smoker or obesity, while the other will be run against the environmental / 
            economic features that are included such as air quality or unemployment.  A fourth model will be run against the features that were identified as top
            importances. This model will not be considered as the final machine learning, but as a support tool to view metrics with just these features. We
            understand the risk of overfitting by reducing to only the features of importance, so this fourth model is more of interest than final use.
    - Description of how data was split into training and testing sets
        - Training and testing sets were split using the default parameters.
    - Explanation of model choice, including limitations and benefits (model base research: https://community.alteryx.com/t5/Data-Science/Predictive-Process-Step-1-Finding-Your-Target-Variable/ba-p/401639)
        - The first model attempted was Spline. Because our team chose to work with a continuous target rather than binary, we did some research on model options
      that may apply.  This model was working well in practice / learning, however we ran in to our first challenge when finding no clear path for using the
      the multiple features that we wanted to include for use in our dataset. 
        - The second model attempted was the MARS. Practice modeling with a single feature went smoothly, however we quickly recognized the limitations of this
      model were similar to that of Spline. While we could run multiple features using MARS, having 13 features would be difficult to interpret in the model
      due to the complexity in the 3D modeling. 
        - Following in class discussion, we then moved to exploring convulutional neural network and random forest regressor modeling. At this time CNN did not 
      move foward as a model to use due to high usage for image data which we are not working with. 

### Database Integration
  - The team members are expected to present a fully integrated database, including the following:
    - Database stores static data for use during the project. See below.

      ![Original attempt](Resources/New_table_after_JOIN_in_pgAdmin.jpg)

    - Database interfaces with the project in some format (e.g., scraping updates the database). 
      - See this file: https://github.com/Norgs87/Final-Project-Stroke-Prediction/blob/main/RFR_ML_DB_Connect.ipynb
    - Includes at least two tables (or collections, if using MongoDB). See below.

      ![Original attempt](Resources/Two_Tables_in_pgAdmin_before_JOIN.jpg)

    - Includes at least one join using the database language (not including any joins in Pandas). See below.
      
      ![Original attempt](Resources/SQL_Table_JOIN_in_pgAdmin.jpg)

    - Includes at least one connection string (using SQLAlchemy or PyMongo)
      - SQLAlchemy psycopg2 was used, as shown in this file: https://github.com/Norgs87/Final-Project-Stroke-Prediction/blob/main/RFR_ML_DB_Connect.ipynb
    - If you use a SQL database, you must provide your ERD with relationships. See below.

      ![Original attempt](Resources/ERD_2_tables.png)

### Dashboard
  - A blueprint for the dashboard is created and includes all of the following:
    - Storyboard on a Google Slide(s): 
      - Original draft has been created. See screenshot below and Google slide(s): https://docs.google.com/presentation/d/1E1D_wDwgtw-h_wREXM73hGIfPYEHObPIjhqgLeNW1OE/edit?usp=sharing
    - Description of the tool(s) that will be used to create the final dashboard
      - An interactive web site has been created and is hosted on pythonanywhere.com. It will include interactive dashboards built in Tableau (that will be embedded on the site via iframes).
    - Description of interactive element(s)
      - The web site will also include an interactive form, built with Flask. It will allow users to enter data for the chosen features/factors and use a machine learning model to predict stroke mortality rates based on that input data. See screenshot below.

      ![Original attempt](Resources/stroke_predictor_website.png)


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





