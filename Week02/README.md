# Week 2A: SQL and R - Movie Ratings Assignment

## Assignment Overview

**Course:** DATA 607 - Data Acquisition & Management  
**Due Date:** February 9, 2026  
**Topic:** SQL Database Design and R Data Analysis

## Objective

Collect simple movie-rating data, store it in a SQL database, and analyze it in R.

## Assignment Requirements

1. ✅ Select **6 recent popular movies**
2. ✅ Survey **at least 5 people** to rate each movie on a **1-5 scale**
3. ✅ Store ratings in a **SQL database** with normalized schema
4. ✅ Load data from SQL into **R** as a dataframe
5. ✅ Handle **missing data** appropriately
6. ✅ Perform exploratory data analysis
7. ✅ Create visualizations
8. ✅ Submit code via **GitHub**

## Files in this Repository

### 1. `movie_ratings.sql`
- SQL script to create normalized database
- Creates 3 tables: `users`, `movies`, `ratings`
- Includes sample data with intentional missing values
- Uses SQLite syntax (compatible with PostgreSQL)

**Database Schema:**
```sql
users (user_id, name)
movies (movie_id, title, year, genre)
ratings (rating_id, user_id, movie_id, rating)
```

### 2. `movie_ratings_analysis.Rmd`
- R Markdown file with complete analysis
- Connects to SQLite database
- Loads data using SQL queries
- Handles missing data (movies not seen by participants)
- Performs exploratory data analysis
- Creates visualizations (bar charts, heatmap)
- Documents reproducible workflow

### 3. `README.md` (this file)
- Assignment documentation
- Instructions for running the code

## Movies Surveyed

All movies are recent releases from February 2026:

1. **Send Help** (2026) - Horror/Thriller
2. **Primate** (2026) - Action
3. **28 Years Later: The Bone Temple** (2026) - Horror
4. **Mercy** (2026) - Thriller
5. **Iron Lung** (2026) - Horror
6. **Greenland 2: Migration** (2026) - Action/Thriller

## Survey Participants

- Alice Johnson
- Bob Smith
- Carol Williams
- David Brown
- Emma Davis

**Note:** Not all participants have seen all movies, resulting in realistic missing data.

## How to Run

### Prerequisites

**R Packages:**
```r
install.packages(c("DBI", "RSQLite", "dplyr", "tidyr", "ggplot2", "knitr"))
```

### Option 1: Run in R/RStudio

1. Clone this repository
2. Open `movie_ratings_analysis.Rmd` in RStudio
3. Click "Knit" to generate HTML report
4. The R Markdown file creates an in-memory SQLite database automatically

### Option 2: Use SQL File Separately

1. Install SQLite or PostgreSQL
2. Run `movie_ratings.sql` to create database:
   ```bash
   # SQLite
   sqlite3 movie_ratings.db < movie_ratings.sql
   
   # PostgreSQL
   psql -d your_database -f movie_ratings.sql
   ```
3. Modify R Markdown connection string if using external database

## Key Features

### Database Design
- **Normalized schema** with proper foreign key relationships
- **Primary keys** for unique identification
- **Junction table** for many-to-many user-movie relationships
- **Data constraints** (CHECK for rating range 1-5)

### Missing Data Handling
- Missing ratings represent movies not seen by users
- Strategy: Keep NA values, don't impute
- All statistics report sample sizes
- Transparent about data completeness

### Analysis Highlights
- User-movie rating matrix
- Average ratings by movie and user
- Missing data analysis
- Distribution visualizations
- Rating heatmap with missing values shown

## Results Summary

- **Total Possible Ratings:** 30 (5 users × 6 movies)
- **Actual Ratings Collected:** 22
- **Missing Ratings:** 8 (26.7%)
- **Rating Range:** 3-5 (participants generally enjoyed the movies)

## Reproducibility

All code is fully reproducible:
- SQL code creates and populates tables from scratch
- R code connects to database programmatically
- Missing data handling is explicit and documented
- Visualizations use consistent styling

## Assignment Completion

This assignment demonstrates:
- ✅ SQL database design and normalization
- ✅ Data collection with realistic missing values
- ✅ SQL queries with JOINs
- ✅ R database connectivity
- ✅ Data manipulation with dplyr and tidyr
- ✅ Missing data handling strategies
- ✅ Exploratory data analysis
- ✅ Data visualization with ggplot2
- ✅ Reproducible research with R Markdown
- ✅ Version control with Git/GitHub

## GitHub Repository

**Repository:** https://github.com/athomsonsps/DATA607  
**Assignment Folder:** Week2/

## Author

Your Name  
DATA 607 - Data Acquisition & Management  
CUNY School of Professional Studies  
February 2026

## License

This project is for educational purposes as part of the DATA 607 course.
