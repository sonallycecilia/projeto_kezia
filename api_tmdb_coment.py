#código comentado

import requests # biblioteca HTTP para Python, utilizada para fazer requisições a URLs.
import json #Esta linha importa o módulo json, que fornece funções para trabalhar com dados no formato JSON (JavaScript Object Notation)
import random #importa o módulo random, que contém funções relacionadas à geração de números aleatórios
from PIL import Image #Esta linha importa a classe Image do módulo PIL (Python Imaging Library), que é uma biblioteca para manipulação de imagens.
from io import BytesIO #Esta linha importa a classe BytesIO do módulo io, que é utilizada para trabalhar com fluxos de bytes em memória.
import datetime #Esta linha importa o módulo datetime, que fornece classes para manipulação de datas e horários.

# passa os parametros que eu quero pegar do filme pra api (filmes do genero x da pagina y ordenada por popularidade da lingua pt-br )
def get_movie_by_genre(genre_id, auth_token): #genre_id (o ID do gênero do filme) e auth_token (o token de autenticação).
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=43" #Esta linha define a URL da API que será chamada para obter filmes com base no gênero. Ela contém vários parametros 
    token = "Bearer "+ auth_token # Esta linha concatena o valor do parâmetro auth_token com a string "Bearer " para formar o token de autenticação necessário para a requisição HTTP.
    params = { #parâmetros da requisição HTTP. O parâmetro with_genres é definido com o valor de genre_id passado para a função.
      "with_genres":str(genre_id),
      "include_adult": "false",
      "include_video": "true",
      "language": "pt-BR",
      "page": page,
      "sort_by": "popularity.desc"
    }
    headers = { # Esta linha define um dicionário chamado headers que contém os cabeçalhos da requisição HTTP. O cabeçalho accept é definido como "application/json" e o cabeçalho Authorization é definido com o valor do token de autenticação.
        "accept": "application/json",
        "Authorization": token
    }

    response = requests.get(url, headers=headers, params=params) #Esta linha faz uma requisição HTTP GET para a URL especificada, passando os parâmetros e cabeçalhos definidos anteriormente. O resultado da requisição é armazenado na variável response.

    return response.text #Esta linha retorna o conteúdo da resposta da requisição HTTP como uma string


def get_trailer(id_filme):
  url = "https://api.themoviedb.org/3/movie/"+ str(id_filme) +"/videos?language=pt-BR" # Esta linha define a URL da API para obter os trailers de um filme específico. O ID do filme é convertido para uma string e inserido na URL.
  headers = { #Esta linha define um dicionário chamado headers que contém os cabeçalhos da requisição HTTP. O cabeçalho
      "accept": "application/json", # definido como "application/json" e o cabeçalho
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
  } #authorization contém um token de autenticação válido.

  response = requests.get(url, headers=headers) #Esta linha faz uma requisição HTTP GET para a URL especificada, passando os cabeçalhos definidos anteriormente.

  return response.text #Esta linha retorna o conteúdo da resposta da requisição HTTP como uma string.
 
def get_image(url_imagem): #url_imagem representa a URL da imagem que queremos obter.
  url = "https://image.tmdb.org/t/p/w500" + url_imagem #: Esta linha concatena a URL base "https://image.tmdb.org/t/p/w500" com a url_imagem fornecida. A URL base indica o local onde as imagens estão armazenadas no The Movie Database (TMDb), e "w500" especifica o tamanho da imagem (500 pixels de largura).

  response = requests.get(url) # Esta linha faz uma requisição HTTP GET para a URL completa da imagem. O resultado da requisição é armazenado na variável response.

  #verifica o status da solicitação, se for 200 significa que esta sem nenhum erro
  if response.status_code == 200: # se a resposta bem-sucedida O BytesIO é usado para ler os bytes do conteúdo da resposta como um fluxo de bytes.
    imagem = Image.open(BytesIO(response.content)) #cria uma instância da classe Image do módulo PIL (Pillow) usando o conteúdo da resposta como entrada.
    #O BytesIO é usado para ler os bytes do conteúdo da resposta como um fluxo de bytes.
    res = imagem.show() #Em seguida, essa linha exibe a imagem usando o método show() da instância da classe Image. Isso abrirá uma janela para exibir a imagem.
  else:
    res = "Falha ao obter a imagem" 
  return res #Por fim, o valor de res é retornado como resultado da função.

def get_director(id): #id fo filme
  # Esta linha define a URL da API para obter os créditos do filme, incluindo o diretor. O ID do filme é convertido para uma string e inserido na URL
  url = "https://api.themoviedb.org/3/movie/"+ str(movie_id) +"/credits?language=pt-BR" 

  headers = { #conversão para json
      "accept": "application/json",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
  }

  response = requests.get(url, headers=headers) #Esta linha faz uma requisição HTTP GET para a URL especificada, passando os cabeçalhos definidos anteriormente.
  return response.text

#essas 3 de cima vão pegar coisas que eu não consigo passar naquela primeira função, nota tbm vou precisar so id do filme pro url ficar completo

#main
token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
url = "https://api.themoviedb.org/3/discover/movie" #Essa variável armazena a URL base da API para descobrir filmes.
page = random.randint(1,200) #número que randamiza a pagina 
header = "Bearer "+token #concatena a string "Bearer " com o valor do token, criando um cabeçalho de autorização válido para as requisições HTTP
headers = { #conversão para json
"accept": "application/json",
"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
}
# esse cabecalho aí basicameente permite que a gente use a api do tmdb e o page vai pegar as páginas que to impoortando a api e randomizar (tem 500 tamo pegando "só" 200 por causa das qualidade de filme)

movie = get_movie_by_genre("16",token) #movie vai receber a função de pegar pelo genero, 16 = id_filme
transform_movie = json.loads(movie) #essa linda pega meu filme dependendo do genêro e transforma o json em dic"
#Esta linha utiliza a função json.loads para transformar a string movie em um objeto Python. A função json.loads analisa a string JSON e retorna um objeto Python equivalente, que é atribuído à variável transform_movie.

list_nominated_movies = [] #vai ser preenchida com os indices dos filmes indicados
while len(list_nominated_movies) < 4: #roda até 4 movies serem indicados
  ran_movie = random.randint(0,19) #Essa linha gera um número inteiro aleatório entre 0 e 19, representando um índice de filme.
  if ran_movie not in list_nominated_movies: #se não ta na lista, adiciona a lista
    list_nominated_movies.append(ran_movie)
  else:
    ran_movie = random.randint(0,19) #se esta, randomiza de novo
# o sr.bloco aí em cima faz com que a gente não pegue sempre os 4 primeiros filmes fixos da pag tlgd, ele dá um randon nos filmes da pag

# aqui embaixa tá tudo dentro de um for pra conseguir acesssar os indices dessas belezura e puxar da api/dic
for i in range(len(list_nominated_movies)): #iteração sobre os indices da lista
  x = list_nominated_movies[i] #x = indice 0 da lista e assim por diante enquanto durar o laço
  title = transform_movie['results'][x]["title"] 
  rel_date = transform_movie["results"][x]["release_date"] #data de lançamento
  tmdb_vote = transform_movie["results"][x]["vote_average"] # nota
  movie_id= transform_movie['results'][x]["id"] #O ID será usado para obter informações sobre o diretor e o trailer do filme.
  obtain_director = get_director(str(movie_id)) # função especifica do diretor
  transform_director = json.loads(obtain_director) # transforma em dic
  poster = transform_movie["results"][x]["poster_path"] #obtem o caminho do poster
  obtain_trailer = get_trailer(str(movie_id)) #obtem o caminho do trailer chamando a função
  transform_trailer = json.loads(obtain_trailer) # trans
  trailers = transform_trailer['results']
# é pouco indutivo, mas se liga, meus mano transform são tipo dics, e esse monte de [] vai acessar informações específicas que o projeto que, e o [x] indica a posição e que buscar isso baseado na lista dos indidicado

  if trailers: #tratamento de cria pros trailer, verificação pra saber se tem trailer
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
    print(get_image(poster)) #apenas exibe a imgagem
    print(trailer)
    print("*" * 70)
  else: # indicações secundárias
    print(get_image(poster)) 
    print(title)
    print("*" * 70)

    # é isso, peço perdão se ficou mal explicado