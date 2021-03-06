# Bank Branches Backend
A Back-End API Application for getting information on banks using search query parameter. Users can set limit and offset for the API response. The API has been deployed to https://bankbranchfinder.herokuapp.com.

This Back-End API Application is part of a Full Stack Project. GitHub repo link for Front-End Web Application : https://github.com/WizArdZ3658/Bank-Branches-Frontend.

The website is deployed at Heroku, click [here](https://bankbranchesindia.herokuapp.com/) to view.

## Data Source
Repository Link : https://github.com/snarayanank2/indian_banks

I fetched data from this repository, it has a csv file and a sql dump file. For more information click [here](https://github.com/snarayanank2/indian_banks).

## API Endpoints
 * https://bankbranchfinder.herokuapp.com/api/branches/autocomplete?q=<> [returns possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset]
 * https://bankbranchfinder.herokuapp.com/api/branches?q=<> [returns possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset]

##### Examples :-
 * https://bankbranchfinder.herokuapp.com/api/branches/autocomplete?q=RTGS&limit=5&offset=0
 * https://bankbranchfinder.herokuapp.com/api/branches?q=Bangalore&limit=4&offset=0

Use HTTPie, cURL, Postman etc. to test these endpoints. **Please note that it is necessary to give values for limit and offset otherwise it will return HTTP Response with error code 422**.
You may skip the **q** parameter in the URL.

## Hosting
The database is hosted on Clever Cloud and the application is hosted on Heroku. The reason why I had to opt for a different database hosting is because the table has more than 127,000 records. The free tier of Heroku has a limit of 20MB whereas for Clever Cloud its 256MB. Read more about [Clever Cloud](https://www.clever-cloud.com/en/) and [Heroku](https://www.heroku.com/).

## Technology Stack
##### Languages :-
Python, SQL

##### Frameworks, Libraries and Tools:-
Django, Heroku, Clever Cloud, PyCharm, Django REST framework, Git

##### Databases:-
PostgreSQL(for development and production)

##### Environment:-
Windows(my PC), Linux(Deployment server)
