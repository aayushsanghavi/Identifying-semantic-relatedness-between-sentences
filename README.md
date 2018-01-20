# Identifying semantic relatedness between sentences

**StackOverflow Dataset**
- https://archive.org/download/stackexchange/stackoverflow.com-PostLinks.7z
- https://archive.org/download/stackexchange/stackoverflow.com-Posts.7z

**Commands to extract duplicate question pairs from the dataset**
1. **python get_duplicates.py Postlinks.xml duplicate_pairs**<br />
This command will collect the duplicate question pairs by question ids from the "PostLinks.xml" and store them in the "duplicate_pairs.npy" file

2. **python get_questions.py Posts.xml duplicate_pairs duplicates**<br />
This command will use the previously collected the duplicate question pairs stored in the "duplicate_pairs.npy" file to extract the question title and body of those questions from the "Posts.xml" and store them in the "duplicates.csv" file

[**Meta information about StackOverflow dataset**](META.md)

**Reference papers**
- http://web2py.iiit.ac.in/research_centres/publications/view_publication/inproceedings/1289
- http://web2py.iiit.ac.in/research_centres/publications/view_publication/inproceedings/1290
