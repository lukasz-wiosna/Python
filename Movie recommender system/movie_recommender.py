import pandas
import numpy
from sklearn.decomposition import TruncatedSVD

ratings_features = ['user_id', "item_id", "rating", "timestamp"]
ratings_dataframe = pandas.read_csv("Data/ratings.csv")
ratings_dataframe = ratings_dataframe.astype("float")
movies_dataframe = pandas.read_csv("Data/movies.csv")


movies_title_dataframe = movies_dataframe[["movieId", "title"]]
movies_title_dataframe["movieId"] = movies_title_dataframe["movieId"].astype(str).astype(float)

merge_dataframe = pandas.merge(ratings_dataframe, movies_dataframe, on = "movieId")

crosstab = merge_dataframe.pivot_table(values = "rating",
                             index = "userId",
                             columns = "title",
                             fill_value = 0)

X = crosstab.T  

NUMBER_OF_COMPONENTS = 12
singular_value_decomposition = TruncatedSVD(n_components = NUMBER_OF_COMPONENTS,
                                            random_state = 1)
                                            
correlation_matrix = singular_value_decomposition.fit_transform(X)
correlation_matrix = numpy.corrcoef(correlation_matrix)

movie_titles = crosstab.columns
movies_list = list(movie_titles)
# Enter the title below:
example_movie_index = movies_list.index("Predator 2 (1990)")

example_correlations = correlation_matrix[example_movie_index]

MAXIMUM_CORRELATION  = 1.0
MINIMUM_CORRELATION = 0.9

recommended_movies = list(movie_titles[(example_correlations < MAXIMUM_CORRELATION) & (example_correlations > MINIMUM_CORRELATION)])
print(recommended_movies)