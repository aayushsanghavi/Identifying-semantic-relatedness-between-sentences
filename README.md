# Identifying semantic relatedness between sentences

**StackOverflow Dataset**
- https://archive.org/download/stackexchange/stackoverflow.com-PostLinks.7z
- https://archive.org/download/stackexchange/stackoverflow.com-Posts.7z

**Commands to extract duplicate question pairs from the dataset**
1. **python get_duplicates.py Postlinks.xml duplicate_pairs**<br />
This script will collect the duplicate question pairs by question ids from the "PostLinks.xml" and store them in the "duplicate_pairs.npy" file

2. **python get_questions.py Posts.xml duplicate_pairs duplicates**<br />
This script will use the previously collected the duplicate question pairs stored in the "duplicate_pairs.npy" file to extract the question title and body of those questions from the "Posts.xml" and store them in the "duplicates.csv" file

3. **python get_words.py Posts.xml stackoverflow_words**<br />
This script will extract unique word and alphanumeric tokens from the "Posts.xml" and store them in the "words" file

4. **python remove_numbers.py stackoverflow_words**<br />
This script remove all the number sequences from the previously collected tokens and store them in the "stackoverflow_words_cleaned" file

[**Meta information about StackOverflow dataset**](META.md)

**Reference papers**
- http://web2py.iiit.ac.in/research_centres/publications/view_publication/inproceedings/1289
- http://web2py.iiit.ac.in/research_centres/publications/view_publication/inproceedings/1290
