# Online-Book-Recommender-System
In this content-based book recommendation system, if users searches for a specific book then 5 more books will be recommended through the specific genre of the first book.

Recommendation engine uses the TFIDF Vectorizer algorithm. TFIDF, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.The tf–idf is the product of two statistics, term frequency and inverse document frequency.

We apply this algorithm on book genre. This produces a vector of TfIdf value of each books. Then we compute the distance between vectors by Cosine Similarity. This will produce a list of scores of each book that how a book is similar to other books based on genre. From the list top five most related books are taken and stored in the database named Recommended_list.

Book dataset is collected from CMU Book Summary Dataset. This dataset contains plot summaries for 16,559 books extracted from Wikipedia, along with aligned metadata from Freebase, including book author, title, and genre.

We use the first 1000 book titles from the CMU book summary dataset. First we clean the dataset, truncating the unnecessary fields published_year, plot summary. Our dataset only includes book id, title, author and genre fields.

First we created the database table Book_list importing from Book.csv file. Then the recommendation engine takes the database and produces the recommended list of each book in a new table named Recommende_list. A website is created using Django framework. All the books are listed in the website homepage. Each book has a page along with its title and the list of 5 recommended books.
