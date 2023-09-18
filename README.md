# CS50W-Project-1-Wiki-Encyclopedia

## Overview

This project is developed as part of Harvard University's CS50W course which dives into the world of web development with Python and JavaScript. In this project, I have built an online encyclopedia reminiscent of Wikipedia, leveraging the power of Django.

[![Watch the video](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/hqdefault.jpg)](https://youtu.be/HvNuI6ut0Cs)

(Click on the image above to see the project demonstration on YouTube)

## Features

### Entry Page
Users can visit `/wiki/TITLE` to view an individual encyclopedia entry. In case the entry is non-existent, a user-friendly error page guides them.

### Index Page
A homepage enlisting all the encyclopedia entries and a feature that enables users to click on any entry for detailed viewing.

### Search
Implemented a robust search functionality allowing users to find encyclopedia entries. If the query exactly matches an entry title, it redirects the user to that page; otherwise, it suggests a list of entries containing the query string.

### New Page
Users can create new encyclopedia entries, enhancing the database with more rich and diverse content.

### Edit Page
Each entry page comes with an edit feature, where users can modify the Markdown content of the page, thereby updating it with more current and accurate information.

### Random Page
A feature that surprises users by redirecting them to a random encyclopedia entry, encouraging exploration and learning.

### Markdown to HTML Conversion
The markdown contents in the encyclopedia entries are dynamically converted to HTML, offering a streamlined and enhanced reading experience.
