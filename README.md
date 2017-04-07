# legacy-name-generator
It's always fun to look back on things you did wrong in the past. This is how the legacy-name-generator came to life.
Back in the days when you used version control in the names of the documents, especcially when working with multiple people on documents.
Documents like important.doc ended up as important_v2_final_reviewed.doc.

This tool lets you generate your own legacy names for your new files!

## Usage
`python legacy-name-generator.py -f important.doc`

## Options
-h help, shows options

-f filename, to generate legacy name for

-l length, amount of legacy additions

-s seperator, seperator of legacy names

## Example outputs

Some example outputs for:

`
python legacy-name-generator.py -f important.doc
`

`
New Legacy name is:  important_review_v3_v2_final2.doc

New Legacy name is: important_v3_new_v1_final2.doc

New Legacy name is:  important_draft_review_tested_updated.doc
`

## Contact
For more information or questions contact: github@jellesmeets.nl
