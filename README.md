
# Plan your trip with Kayak!

Project carried out within the framework of my training Data Fullstack, Jedha's Bootcamp Paris. 

To help Kayak Marketing Team, the goal was to recommend where people should plan their next holidays, based on real data about: weather and hotels in the area.
I had a list of 35 cities / place in France to do so. 

To carry out this project, I:
- scraped Booking.com to get hotels informations.
- called openweathermap API to get weather informations.
- stored all the informations into a csv file available in a S3 bucket.
- transfered datas into a sql database for people to get access to it and be able to work with. 









## Installation

To install my project in local, you first need to git clone the repository (https://github.com/Fanny-Mlmrtl/Bloc_1). Then, create a virtual environment (see Environment Variables section).

    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`numpy`
`pandas`
`requests`
`json`
`re`
`plotly.express`
`os`
`logging`
`scrapy`
`urllib.parse`
`boto3`
`csv`



## Demo

https://share.vidyard.com/watch/8qUm3EqkgbRDoeWL85nLrW



## Screenshots

![First map "Top 5 destinations based on weather"](https://github.com/Fanny-Mlmrtl/Bloc_1/blob/main/Top%2020%20hotels%20by%20top%20destinations.png)
![Second map "Top 20 hotels by top destinations"](https://github.com/Fanny-Mlmrtl/Bloc_1/blob/main/Top%2020%20hotels%20by%20top%20destinations.png)

## Roadmap

To go further with this project we can create a streamlit app and deploy it with Heroku.

## Authors

[Fanny Malmartel ](https://github.com/Fanny-Mlmrtl)
contact: fannymalmartel@gmail.com


