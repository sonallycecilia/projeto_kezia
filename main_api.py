import requests
import json
import random
from PIL import Image
from io import BytesIO
import datetime

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

# passa os parametros que eu quero pegar do filme pra api (filmes do genero x da pagina y ordenada por popularidade da lingua pt-br )

def get_trailer(id_filme):
  url = "https://api.themoviedb.org/3/movie/"+ str(id_filme) +"/videos?language=pt-BR"
  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
  }

  response = requests.get(url, headers=headers)

  return response.text

def get_image(url_imagem):
  url = "https://image.tmdb.org/t/p/w500" + url_imagem

  response = requests.get(url)

  if response.status_code == 200:
    imagem = Image.open(BytesIO(response.content))
    res = imagem.show()
  else:
    res = "Falha ao obter a imagem"
  return res

def get_director(id):
  url = "https://api.themoviedb.org/3/movie/"+ str(movie_id) +"/credits?language=pt-BR"

  headers = {
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
  }

  response = requests.get(url, headers=headers)

  return response.text

#essas 3 de cima vão pegar coisas que eu não consigo passar naquela primeira função, nota tbm vou precisar so id do filme pro url ficar completo

token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
url = "https://api.themoviedb.org/3/discover/movie"
page = random.randint(1,200)
header = "Bearer "+token
headers = {
"accept": "application/json",
"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
}

# esse cabecalho aí basicameente permite que a gente use a api do tmdb e o page vai pegar as páginas que to impoortando a api e randomizar (tem 500 tamo pegando "só" 200 por causa das qualidade de filme)

movie = get_movie_by_genre("16",token)
transform_movie = json.loads(movie) #essa linda pega meu filme dependendo do genêro e transforma o json em dic"

list_nominated_movies = []
while len(list_nominated_movies) < 4:
  ran_movie = random.randint(0,19)
  if ran_movie not in list_nominated_movies:
    list_nominated_movies.append(ran_movie)
  else:
    ran_movie = random.randint(0,19)

# o sr.bloco aí em cima faz com que a gente não pegue sempre os 4 primeiros filmes fixos da pag tlgd, ele dá um randon nos filmes da pag

# aqui embaixa tá tudo dentro de um for pra conseguir acesssar os indices dessas belezura e puxar da api/dic

for i in range(len(list_nominated_movies)):
  x = list_nominated_movies[i]
  title = transform_movie['results'][x]["title"]
  rel_date = transform_movie["results"][x]["release_date"]
  tmdb_vote = transform_movie["results"][x]["vote_average"]
  movie_id= transform_movie['results'][x]["id"]
  obtain_director = get_director(str(movie_id))
  transform_director = json.loads(obtain_director)
  poster = transform_movie["results"][x]["poster_path"]
  obtain_trailer = get_trailer(str(movie_id))
  transform_trailer = json.loads(obtain_trailer)
  trailers = transform_trailer['results']

# é pouco indutivo, mas se liga, meus mano transform são tipo dics, e esse monte de [] vai acessar informações específicas que o projeto que, e o [x] indica a posição e que buscar isso baseado na lista dos indidicado

  if trailers: #tratamento de cria pros trailer
    trailer = "https://www.youtube.com/watch?v=" + trailers[0]["key"]
  else:
    trailer = "Nenhum trailer disponível"

  if x == list_nominated_movies[0]: #indicação principal
    print(title)
    print(rel_date)
    print(tmdb_vote)
    print("Dirigido por:")
    for j in range(len(transform_director['crew'])):
      if transform_director['crew'][j]['job'] == "Director":
        director = transform_director['crew'][j]['name']
        print(director)
    # isso aí em cima é pra acessar lugares muito especificos da api e printar mais de um diretor se tiver
    # basicamenete na api o diretor é puxado dos créditos que 1.são gigantescos, 2.não são iguais pra todos os filmes, mas eles tem uma padronização
    # os creditos são divididos em "caixinhas", e aqui eu acesso pra pegar o diretor é o crew(equipe em pt-br), primeira coisa que faço é um for com base no len de crew (ou seja ele vai sair lendo crew)
    # enquanto ele ler crew ele vai procurar em job quem assume a função de diretor, se achar é criada uma variável diretor que vai pegar o nome na posição que ele achou a posição diretor
    #:)
    print(get_image(poster))
    print(trailer)
    print("*" * 70)
  else: # indicações secundárias
    print(get_image(poster))
    print(title)
    print("*" * 70)

    # é isso, peço perdão se ficou mal explicado