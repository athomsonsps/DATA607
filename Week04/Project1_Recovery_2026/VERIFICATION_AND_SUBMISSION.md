# Verification and submission checklist

## Independently verified from the original tournament text and uploaded CSV (JavaScript audit)
- 64 player records
- 448 player-round records (64 × 7)
- 408 numbered-opponent records; 204 paired games
- 40 rounds without a numbered opponent excluded from opponent rating averages
- All numbered-opponent records have reciprocal round/opponent matches and complementary win/loss or draw results
- 64 CSV rows and five requested columns
- Gary Hua: ON, 6.0 points, 1794 pre-rating, 1605 rounded opponent mean
- All 64 exported rows agree with source when accounting for R's round-to-even rule: Kyle William Murphy has a mean of 1248.5, which R rounds to 1248
- Main and speaker-note reports contain the exact same 9 executable R chunks
- Duplicate validation block removed from main report; speaker notes now show original R code instead of being a standalone outline
- Speaker-note claim that Copilot was used removed, because that review was not verified

## Not independently verified
- Actual execution in R / Quarto Render: unavailable in this environment
- Visual inspection of rendered charts: requires render
- Recording and submission of video: not performed
- Brightspace submission: not performed

## Before submission
- [ ] Render main QMD in RStudio / Quarto and confirm there are no errors
- [ ] Render speaker-note QMD and verify code, tables, and charts appear
- [ ] Open exported CSV and verify first row and five column names
- [ ] Submit actual main GitHub file URL and rendered HTML if professor requests it
- [ ] Record/submit Project 1 video explainer, if accepted late
- [ ] Keep the source data alongside each QMD when moving between computers

## Honest status
Source/data audited; code not executed in R. Treat package as prepared for local render and submission, not as a verified successful render.
