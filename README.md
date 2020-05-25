# Description

A personal gallery application used to display images from different locations and categories. Users can view details of picture by clicking on the info icon.

## Author

Trinityrace

### Code Beat

....here..

### User stories

These are the behaviours/features that the application implements for use by a user.

#### As a user I can

- View different photos that interest them. *Click on a single photo to expand it and also view the details of the photo.
- View the most recent posts.
- Search for different categories of photos. (ie. Travel, Food).
- Copy a link to the photo to share with my friends.
- View photos based on the location they were taken.

## Specifications

### Behaviour

- Display Landing page
- Display picture information
- Display different picture categories
- Display pictures from different categories

### Input

On page load

- Click info icon on picture
- Enter search term on the search bar
- Click 'Location/Globe' Icon on the navigation bar
Output

#### Site description and gallery pictures

- Opens a modal that shows a large version of the picture and its details
- Display search results if search term meets database categories
- Displays a select field that allows users to search for pictures from a specific country/location

#### SetUp / Installation Requirements

'''

* Prerequisites

- python3.6

- pip

- postgres database

- virtualenv

- django

* Cloning In your terminal:

$ git clone <https://github.com/Trinityrace/galla.git> $ cd gallery

* Creating the virtual environment

$ python3.6 -m venv --without-pip virtual $ source virtual/bin/env $ curl <https://bootstrap.pypa.io/get-pip.py> | python

* Installing Django and other Modules

$ python3.6 -m pip install -r requirements.txt

* Run the application:

$ python3 manage.py runserver

* Testing the Application

- To run the tests for the class files:

$ python3.6 manage.py test

'''

## Technologies Used

- Python 3.6

- Django2.2

### Support and contact details

For any questions, troubleshooting or contributions, find me on:
Email: trinityrtime@gmail.com

### License

licensed under the MIT License copyright(c) 2020 Gallery