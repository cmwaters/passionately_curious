# Passionately Curious

This is a django powered website aimed at teaching some of the complexities of our world in 
as simple and intuitive way as possible

## Setup

Make sure you have python3, pip and git installed

1. Run the command line and move to the directory with which you wish to work from: \
`$ cd path/to/workspace` \
`$ mkdir passionately_curious`

2. (Optional) Create a virtual environment to operate the workspace within: \
`$ virtualenv PC`

3. (Optional) Activate the virtual environment: \
`$ source PC/bin/activate`

4. Clone the repository into the workspace: \
`$ git clone https://github.com/cmwaters/passionately_curious.git`

5. Install Dependencies: \
`$ pip install -r requirements.txt`

## Usage

Make sure you are in the root directory. Then execute the following command to run the server locally: \
`$ python3 manage.py runserver`

Open your browser and go to the following url: \
`http://127.0.0.1:8000/`

## Development

### Architecture

All website related work resides in the passionatelycurious folder and has the following layout and purpose:
<ul>migrations - used to record the models of the database (not important)</ul>
<ul>static - contains the files of css, javascripts as well as images and other dependencies of the html pages</ul>
<ul>templates - contains all the html templates to be generated from the views</ul>
<ul>settings.py - the standard django settings for the website</ul>
<ul>urls.py - a list of all urls and the views that they redirect to</ul>
<ul>views.py - the backend computation (if necessary) and then generation of the html page</ul>

### Styling

Please follow the standard PEP8 code style



