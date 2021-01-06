# Bank Branches Backend
A Back-End API service for finding banks using search query parameter. People can also set limit and offset for the API response.

# Data Source
Repository Link : https://github.com/snarayanank2/indian_banks

I fetched data from this repository, it has a csv file and a sql dump file. For more information click on the link [here](https://github.com/snarayanank2/indian_banks).

# API Endpoints
 * /api/branches/autocomplete?q=<>
 * /api/branches?q=<>

##### Examples :-
 * /api/branches/autocomplete?q=RTGS&limit=5&offset=0
 * /api/branches?q=Bangalore&limit=4&offset=0

# Hosting
The database is hosted on Clever Cloud and the application is hosted on Heroku. The reason why I had to opt for a different database hosting is because the table has more than 127,000 records. The free tier of Heroku has a limit of 20MB whereas for Clever Cloud its 256MB. Read more about [Clever Cloud](https://www.clever-cloud.com/en/) and [Heroku](https://www.heroku.com/).

## Technology Stack
##### Languages :-
Python, SQL, Git

##### Frameworks, Libraries and Tools:-
Django, Heroku-CLI, Clever Cloud, PyCharm, Django REST framework

##### Databases:-
PostgreSQL(for development and production)

##### Environment:-
Windows(my PC), Linux(Deployment server)
