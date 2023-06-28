import requests
import json
import random
from PIL import Image
from io import BytesIO

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
url = "https://api.themoviedb.org/3/discover/movie"
page = random.randint(1,200)
header = "Bearer "+token
headers = {
"accept": "application/json",
"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
}

def get_movie_by_genre(genre_id, auth_token):
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=43"
    token = "Bearer "+ auth_token
    params = {
    "with_genres":str(genre_id),
    "include_adult": "false",
    "include_video": "true",
    "language": "pt-BR",
    "page": page,
    "sort_by": "popularity.desc"
    }
    headers = {
        "accept": "application/json",
        "Authorization": token
    }

    response = requests.get(url, headers=headers, params=params)
    return response.text

def movie_genre(genre):
    movie = get_movie_by_genre(genre, token)
    transform_movie = json.loads(movie) #essa linda pega meu filme dependendo do genêro e transforma o json em dic"
    return transform_movie

def random_movie_pag_genre():
    list_nominated_movies = []
    while len(list_nominated_movies) < 4:
        ran_movie = random.randint(0, 19)
        if ran_movie not in list_nominated_movies:
            list_nominated_movies.append(ran_movie)
        else:
            ran_movie = random.randint(0, 19)
    return list_nominated_movies

def get_movie_id(list_nominated_movies, indice, transform_movie):
    movie = list_nominated_movies[indice]
    movie_id= transform_movie['results'][movie]["id"]
    return str(movie_id)

def get_title(list_nominated_movies, indice, transform_movie):
    movie = list_nominated_movies[indice]
    title = transform_movie['results'][movie]["title"]
    return title

def get_tmdb_vote(list_nominated_movies, indice, transform_movie):
    movie = list_nominated_movies[indice]
    tmdb_vote = transform_movie["results"][movie]["vote_average"]
    return tmdb_vote

def get_date(list_nominated_movies, indice, transform_movie):
    movie = list_nominated_movies[indice]
    date = transform_movie["results"][movie]["release_date"]
    return date

def get_poster(list_nominated_movies, indice, transform_movie):
  movie = list_nominated_movies[indice]
  posters = transform_movie["results"][movie]["poster_path"]
  if posters:
    poster = "https://image.tmdb.org/t/p/w500" + str(posters)
    return poster
  else:
    poster = "Não tem poster disponível"
    return poster

def get_trailer(movie_id):
  url = "https://api.themoviedb.org/3/movie/"+ str(movie_id) +"/videos?language=pt-BR"
  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
  }
  response = requests.get(url, headers=headers)
  response = response.text
  transform_trailer = json.loads(response)
  trailers = transform_trailer['results']
  if trailers: #tratamento de cria pros trailer
    trailer = "https://www.youtube.com/watch?v=" + trailers[0]["key"]
  else:
    url_en = "https://api.themoviedb.org/3/movie/"+ str(movie_id) +"/videos?language=en-US"
    response_en = requests.get(url_en, headers=headers)
    response_en = response_en.text
    transform_trailer_en = json.loads(response_en)
    trailers_en = transform_trailer_en['results']
    if trailers_en:
      trailer = "https://www.youtube.com/watch?v=" + trailers_en[0]["key"]
    else:
      trailer = "Nenhum trailer disponível"
  return trailer

def get_director(movie_id):
    url = "https://api.themoviedb.org/3/movie/"+ str(movie_id) +"/credits?language=pt-BR"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
    }
    response = requests.get(url, headers=headers)
    response = response.text
    director = []
    transform_director = json.loads(response)
    for j in range(len(transform_director['crew'])):
        if transform_director['crew'][j]['job'] == "Director":
            director.append(transform_director['crew'][j]['name'])
    return director

def mostrar_imagem(url):
    resposta = requests.get(url)
    conteudo_imagem = resposta.content
    imagem_pil = Image.open(BytesIO(conteudo_imagem))
    return imagem_pil

def get_overview(list_nominated_movies, indice, transform_movie):
    movie = list_nominated_movies[indice]
    overview = transform_movie["results"][movie]["overview"]
    if overview == "":
        overview = "Nenhuma sinopse disponivel :("
    else:
        overview = transform_movie["results"][movie]["overview"]
    return overview

def get_streaming(movie_id):
  url = "https://api.themoviedb.org/3/movie/"+ str(movie_id) +"/watch/providers"

  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
  }

  response = requests.get(url, headers=headers)
  response = response.text
  transform_streaming = json.loads(response)
  streamings = transform_streaming.get("results",{})
  if "BR" in streamings :
    if "flatrate" in streamings["BR"]:
      streaming = streamings["BR"]["flatrate"][0]["provider_name"]
    elif "rent" in streamings["BR"]:
      streaming = streamings["BR"]["rent"][0]["provider_name"]
    else:
      streaming = "Não disponível em nenhum serviço de streaming brasileiro."
  else:
    streaming = "Não disponível em nenhum serviço de streaming brasileiro."

  return streaming