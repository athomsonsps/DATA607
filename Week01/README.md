# Week 01 - DATA607Beer

**Course:** DATA 607 - Data Acquisition and Management
**Author:** Andre Thomson
**Due date:** not specified

## Required files

| Path | Description |
| --- | --- |
| assignment/assignment1.qmd | Quarto source, title "DATA607Beer" |

## Assignment instructions

Not recorded in this repository. To be filled in from the course syllabus.

## Submission status

Source committed. Needs review before submission - see the notes below.

## Notes

- The .qmd is currently the default Quarto template, with the beer review dataset pasted into a non-executable display block as one line of roughly 3,000,000 characters. No analysis code has been written yet.

- Upstream data source, as noted in the document: beer_review_data_cleaned.csv from the public kreitlerj/Beer-Data-Project repository. It is not stored here as a file, so there is no data folder for this week.

- quarto render on this file did not complete within a 10-minute budget because of that single very long line. Reading the CSV with read.csv in an R chunk instead of pasting it inline would fix both problems.

- A byte-identical copy named assignment1.hmtl.qmd, a misspelling of html, was removed. The sha256 of both files was f971674f74e362a4f9face57ba69f431ede9dd4f66e2a941e730ae4f8a4301b5
