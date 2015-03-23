This is the readme file for classify_posts which is a super-simple python
script for classifying csv files full of forum posts based on likes. The script
is so simple, in fact, that this readme will probably be longer than the
program itself.

***************
*RELEASE NOTES*
***************
1. March 23, 2015 added unit tests

*********
*INSTALL*
*********
What install? This is Python. You just download it from 
www.github.com/isaac-friedman/classify_posts.

*******
*USAGE*
*******
The script takes a csv file called "posts.csv." Currently, the file must have 
that name. It must also have columns called:
1. id 
2. title
3. timestamp
4. privacy
5. views 

"Privacy" must be a string either "private" or "public." (We do not yet support 
protected posts). The script creates files for the "top posts," the "other 
posts" and the top post for each day. For each category, sort_posts.py writes a 
csv file with the IDs, and the entire row from the input file. As long as the 
input file has the five (5) columns listed above, it can have as many other 
columns as necessary.

The criteria for top posts are:
1. Post must be public
2. Post must have more than 10 likes
3. Post must have more than 9000 views
4. Post title must be more than 40 characters long.

Currently, these criteria are arbitrary but a future release will contain a 
mechanism for classifying based on user-defined criteria. 

Top posts by day are simply the single post with the most likes for a given day.

*********
*LICENSE*
*********
Copyright (c) 2015. Isaac Friedman
This software is released under the MIT license available at 
http://opensource.org/licenses/MIT.