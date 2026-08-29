# DATA 607 - Data Acquisition and Management

**Author:** Andre Thomson

CUNY School of Professional Studies. Coursework repository - each assignment lives in a WeekNN folder.

## Weekly assignment tracker

| Week | Assignment | Due date | Files | Status |
| --- | --- | --- | --- | --- |
| [Week01](Week01/) | DATA607Beer, Quarto | not specified | assignment/assignment1.qmd | Source committed, needs review |
| [Week02](Week02/) | SQL and R, Movie Ratings | February 9, 2026 | assignment/movie_ratings_analysis.Rmd and code/movie_ratings.sql | Submitted |
| [Week03](Week03/) | - | - | - | Empty |
| [Week04](Week04/) | - | - | - | Empty |
| [Week05](Week05/) | - | - | - | Empty |
| [Week06](Week06/) | - | - | - | Empty |
| [Week07](Week07/) | - | - | - | Empty |
| [Week08](Week08/) | - | - | - | Empty |
| [Week09](Week09/) | - | - | - | Empty |
| [Week10](Week10/) | - | - | - | Empty |
| [Week11](Week11/) | - | - | - | Empty |
| [Week12](Week12/) | - | - | - | Empty |
| [Week13](Week13/) | - | - | - | Empty |
| [Week14](Week14/) | - | - | - | Empty |
| [Week15](Week15/) | - | - | - | Empty |

## Folder layout

Each week uses only the subfolders it actually needs.

| Folder | Contents |
| --- | --- |
| assignment/ | Quarto .qmd and R Markdown .Rmd sources, the submitted work |
| code/ | Standalone R scripts and SQL |
| data/ | Local datasets |
| output/ | Rendered HTML and PDF reports and charts |
| resources/ | Instructions, rubrics, and reference material |

Week03 through Week15 are empty placeholders, each holding a .gitkeep so Git tracks the folder. Assignment titles and due dates will be filled in from the course syllabus rather than guessed.

## Rendering

Run from the repository root.

R Markdown, verified working on R 4.3.3 with rmarkdown, knitr, DBI, RSQLite, dplyr, tidyr and ggplot2 installed:

    Rscript -e 'rmarkdown::render("Week02/assignment/movie_ratings_analysis.Rmd")'

Or open the .Rmd in RStudio and click Knit.

Quarto, after installing Quarto from quarto.org:

    quarto render Week01/assignment/assignment1.qmd

Note: that Quarto command has not been confirmed to complete on Week01/assignment/assignment1.qmd. That file contains a single line of roughly 3,000,000 characters of pasted CSV, which Pandoc does not process in a reasonable time. See Week01/README.md.

Move any rendered .html or .pdf into that week's output folder.
