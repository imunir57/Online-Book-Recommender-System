from recs.models import Book_list, Recommended_list
import os
import csv
import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def run():

		with open('C:\\Users\\MuNir\\book\\brs\\book.csv') as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				b = Book_list()
				b.id=row['ID']
				b.name= row['Name']
				b.author=row['Author']
				b.genre= row['Genre']
				b.save()
				

		books = pd.read_csv('C:\\Users\\MuNir\\book\\brs\\book.csv', sep=',', error_bad_lines=False, encoding ='latin-1')
		books.columns = ['ID', 'Name', 'Author', 'Genre']

		tf = TfidfVectorizer(analyzer='word', ngram_range=(1,2), min_df=0, stop_words='english')
		tfidf_matrix = tf.fit_transform(books['Genre'])

		cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
		results={}

		for i, row in books.iterrows():
			similar_indices = cosine_similarities[i].argsort()[:-100:-1]
			similar_items = [(books['ID'][j]) for j in similar_indices]
			row_id = row['ID']
			results[row_id] = similar_items
			results[row_id].pop(results[row_id].index((row_id)))

			r = Recommended_list()
			r.idx = Book_list.objects.get(id=row_id)
			r.rec1 = results[row_id][0]
			r.rec2 = results[row_id][1]
			r.rec3 = results[row_id][2]
			r.rec4 = results[row_id][3]
			r.rec5 = results[row_id][4]
			r.save()