
Codes used for scraping, cleaning, and analyzing thread titles from the Economic Job Market Rumor website. I was able to scrape data on thread titles, original link to each thread, number of views, votes, and the "freshness" (defined as the time elapsed since the last post) of the thread. There's roughly 286,000 observations going back at least 6 years.

In theory, one could scrape all of the posts within each thread, but that would be a tremendous amount of data (which is fantastic) and would take much longer. If you feel inspired to do this, please let me know!

There are still a lot of things I'd like to analyze using this data and will get to it when I have more time (see the todo list below).

The codes for each step are stored in three IPython notebooks. For the analysis, see the ejmr_analysis.ipynb notebook. The notebooks are run in the following order:

* ejmr_scrape
* ejmr_clean
* ejmr_analysis

todo:
* X scrape: post title, views, number of posts, votes, freshness
* X include original link to post
* X word frequency (with plot)
* X top posts by views, number of posts, votes, etc.
* word trends over time
    - date inferred from freshness field and download date field
* funny posts
* Words most frequently used in the same sentence
* economic related post vs non-econ., troll vs non-troll
* sentiment analysis

Good references:
* https://stackoverflow.com/questions/21972690/beautifulsoup-scraping-a-forum-page
* http://francescopochetti.com/tag/sentiment-analysis/
* http://varianceexplained.org/r/hn-trends/