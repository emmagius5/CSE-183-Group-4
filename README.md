# Project: Bird Watching App

The goal of the project is to build a bird-watching app/site, loosely modeled on ebird.org.  The project has been chosen in a way that will let us play with many interesting features in web development, including developing responsive one-page apps, maps integration, user communication, and more. 

The project is organized around the following main pages: 

- Index page.  Welcomes users and shows a map of bird densities. 
- Checklist page.  Enables users to enter a checklist. 
- Stats page.  Enables users to see stats and compilations about their own data. 
- Location page.  Enables users to ask for details about a birding location. 

There can of course be auxiliary management pages built.  The four pages above should be developed in vue.js.  You can, for instance, assign one group member to develop each page. 

## Index page

This is the page users see when they log in. They should see a map, centered on their region, with a density indication of where birds have been seen. The page should contain links to submit a checklist (the checklist page) and “My birding” (the stats page). 
On the map, users should be able to draw a rectangle, and click on a button that says “statistics on region”.  This leads them to the statistics page for the selected region. 
The map is also governed by a species selection box.  Users can select a species, and the map will show the density of that species. 

Emma Gius created everything on the Index page, including the interactive map, and worked on the index.html, index.js, and 
index_controller.py files. ALso, near the beginning of the project, there is a Git commit thatis from "Ubuntu" which was just Emma pushing changes from my virtual machine, before Emma established what user name Emma's machine should push from. 

### Species selection

There must be some way of choosing which species to display on the map. If no species is selected, you should show data for all species.  You can have a search box with autocomplete in which users can select the species, etc. 

## Checklist page

In this page, users can enter a checklist.  This page should be accessed by selecting a position on the map page, and click on an "enter checklist" button.  Users need to be logged in to enter a checklist. 

In the checklist page, you should have on top a search bar that enables to select the species, so that if one enters "spar" one sees only the sparrows.  Then, for each species, there should be a row in a table with species name, a place where users can enter a number of birds seen, and a button to increment the number of birds seen. 

When the user is done, they can click on a "submit" button, and the checklist is saved.

There should be some additional page where users see the list of checklists they have submitted, and where they can delete them, or go edit them (via the checklist page).  This "My Checklists" page 

Selam worked on Checklist and My Checklist pages, that involve checklist.html, checklist_controller.py, checklist.js, my_checklist.js and my_checklists.html. The Checklist page allows users to add species sightings with counts and submit them, while the My Checklist page displays submitted checklists in a table with editable counts, deletion options, and proper grouping by date.

## Location page

When users select a region on the map page and click on "region information" (or similar), they should be able to view the statistics for that region. The statistics should include:

- A list of species seen in the region, with the number of checklists and total number of sightings for the region. 
- Some kind of graph showing the number of birds in a species seen over time. For example, when one clicks on a species in the above list, such graph should be displayed. 
- Some information on the top contributors for the region. 

You can use the [D3.js](https://d3js.org/) library to create visualizations, or the [Chart.js](https://www.chartjs.org/) library.  Other libraries are also possible.

Donovan deVise seamlessly integrated the location page
with the index page to showcase all bird species spotted in 
the selected region. He created a chart alongside a list of
all species which could be selected to view sightings over time
for a given species. He also designed the page to show total 
sightings as well as which observation sessions resulted in the
most sightings.
## User statistics

Users should be able to see their own statistics.  This page should show things like: 
- A list of all species they have seen, searchable.  When they click on a species, they should see some visualization of when they saw it, and if one liked, even where (you can include a map here). 
- Some visualization of how their bird-watching has trended in time. 

Andy worked on My Birding / Stats page, which involves stats.html, stats_controller.py, and stats.js. The page includes a table of species sighting, an interactable map sighting, and a graph of user activity over time. The entry on the table can be expanded to view the map. 

## Developing your app

### Development advice 

I advise developing the database schema first, discussing it all togehter.  Once that is in place, each person can take the lead in developing one of the pages, and you can use synthetic data to test and develop the pages (using the data I will provide, or augmenting it with your own data).

### Sample data

You should prime the database with [this data](https://drive.google.com/drive/folders/1NV5vMn0h3O5peppvBHqcdJAudPQe_Qkg?usp=sharing). 
The data is in the form of three csv files, which can be loaded into the database, for example by reading them via the `csv` Python module and inserting them into the database: 

- `species.csv` contains the species of birds (about 400). 
- `checklists.csv` contains the checklists.  Each checklist has a user, a location, and a data, among other fields. 
- `sightings.csv` contains the sightings.  Each sighting has a checklist, a species, and a number of birds seen.

The checklists and sightings are linked by the `SAMPLING EVENT IDENTIFIER` field. 
Note that while the original data comes from 10 days of eBird checklists in the area, it has been modified, so the data does not correspond to real observations (you may find strange observations, such as sparrows in the ocean!). 

To prime the database, you can use code in `models.py` like this:

```
if db(db.species).isempty():
    with open('species.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            db.species.insert(name=row[0])
```

and similarly for the other tables.

## Project Submission

### Project repository

You should create a ***private*** repository on GitHub, and add as collaborators: 
- `lucadealfaro`
- `Fallenhh`
- `mathewNJoseph`

You will be able to make the project public, if you so wish, after the project is graded.

### By November 17

Please provide by November 17 the details on your project, including the members and the GitHub location of the repository, using [this form](https://docs.google.com/forms/d/e/1FAIpQLSderx0Rco4qotKG2-1-tZHpKfNU1lQELCdyn7219QwFr1OACg/viewform?usp=sf_link).

### By Thursday, December 12

#### Project submission

You should submit the project to [this form](https://docs.google.com/forms/d/e/1FAIpQLSfb6Y0sCuNWBsKgr4mkHPT7xLZXlr1WGJVK-9hSskPpIqOyOQ/viewform?usp=sf_link).
The project should be submitted as a zip file containing the project directory; please verify that the zip enables someone to run the project without any additional information. 
A `zipit.py` program will be provided here shortly for zipping the project. 

#### Peer evaluation

You should also fill a [peer evaluation](https://docs.google.com/forms/d/e/1FAIpQLScZ7Ux-SsqclZkBblviTJuxXvIKC0rCvqO6TkjYYxj83xay1g/viewform?usp=sf_link). 

## Project grading

The project will be graded on the following criteria:

- Code quality
- Security
- User interface
- Completeness
- Creativity

The project will be graded by the instructor and the TAs.  We will look in detail at the commit log of the project, so please make sure to commit often and with meaningful messages, and make sure everybody commits their own code so we can attribute the work correctly.
