import customtkinter as ctk
from tkinter import *
from CTkMessagebox import CTkMessagebox
import requests
import json
import random
from PIL import Image
from io import BytesIO

class JanelaUsuario(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Página do Usuário')
        self.geometry("1450x800")
        self.opcoes_usuario()
        self.filme_principal()
        self.main_api()
        
        #variaveis
        self.id_genero = None
        self.titulo_principal = None
        self.titulo_teste = None
        
    def pegar_filme_genero(self, id_genero, auth_token):
        self.url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc&with_genres=43"
        self.token = "Bearer "+ auth_token
        self.params = {
        "with_genres":str(id_genero),
        "include_adult": "false",
        "include_video": "true",
        "language": "pt-BR",
        "page": self.page,
        "sort_by": "popularity.desc"
        }
        self.headers = {
            "accept": "application/json",
            "Authorization": self.token
        }

        self.response = requests.get(self.url, headers=self.headers, params=self.params)

        return self.response.text
    
    def pegar_trailer(self, id_filme):
        self.url = "https://api.themoviedb.org/3/movie/"+ str(id_filme) +"/videos?language=pt-BR"
        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
         }

        self.response = self.requests.get(self.url, headers=self.headers)

        return self.response.text

    def pegar_imagem(self, url_imagem):
        self.url = "https://image.tmdb.org/t/p/w500" + url_imagem

        self.response = self.requests.get(self.url)

        if self.response.status_code == 200:
            self.imagem = Image.open(BytesIO(self.response.content))
            self.res = self.imagem.show()
        else:
            self.res = "Falha ao obter a imagem"
        return self.res
    
    def pegar_diretor(self, id_filme):
        self.url = "https://api.themoviedb.org/3/movie/"+ str(id_filme) +"/credits?language=pt-BR"

        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
        }

        self.response = requests.get(self.url, headers=self.headers)

        return self.response.text
    
    def pegar_poster(self, lista, indice, transform_movie):
        movie = lista[indice]
        poster = transform_movie["results"][movie]["poster_path"]
        return poster

    def main_api(self):
        self.token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
        self.url = "https://api.themoviedb.org/3/discover/movie"
        self.page = random.randint(1, 200)
        self.header = "Bearer "+self.token
        self.headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
        }   
        
        if self.id_genero is not None:
            self.movie = self.pegar_filme_genero(self.id_genero, self.token)
            self.transform_movie = json.loads(self.movie)
            
            self.lista_indice_filmes = []
            while len(self.lista_indice_filmes) < 4:
                self.ran_movie = random.randint(0, 19)
                if self.ran_movie not in self.lista_indice_filmes:
                    self.lista_indice_filmes.append(self.ran_movie)
                else:
                    self.ran_movie = random.randint(0, 19)
            print(self.lista_indice_filmes)        
        else:
            CTkMessagebox(title= 'Inválido!',
                message= 'Marque uma opção de', 
                icon= 'warning',
                button_color='#A567BB',
                button_hover_color='#bc91e6',
                font=('Berlin Sans FB', 16)
            )
        

        
        self.pos_filme_principal = self.lista_indice_filmes[0]
        self.pos_filme1 = self.lista_indice_filmes[1]
        self.pos_filme2 = self.lista_indice_filmes[2]
        self.pos_filme2 = self.lista_indice_filmes[3]
        
        #info filme principal
        self.titulo_principal = self.transform_movie['results'][self.pos_filme_principal]["title"]
        self.lançamento_principal = self.transform_movie["results"][self.pos_filme_principal]["release_date"]
        self.tmdb_nota_principal = self.transform_movie["results"][self.pos_filme_principal]["vote_average"]
        '''self.filme_id_principal = self.transform_movie['results'][self.pos_filme_principal]["id"]
        self.obter_diretor = self.pegar_director(str(self.filme_id))
        self.transform_director = json.loads(self.obter_diretor)
        self.poster = self.transform_movie["results"][self.pos_filme_principal]["poster_path"]
        self.obter_trailer = self.get_trailer(str(self.filme_id))
        self.transformar_trailer = json.loads(self.obter_trailer)
        self.trailers = self.transformar_trailer['results']'''
        
        #conversões do filme principal
        self.titulo_principal_convertido = self.titulo_principal
        self.lançamento_principal_convertido = self.lançamento_principal
        self.tmdb_nota_principal_convertido = self.tmdb_nota_principal
        
        #frame de filmes
        self.frame_filmes = ctk.CTkTabview(
            self,
            width=800, 
            height=750,
            segmented_button_selected_color='#A567BB',
            segmented_button_fg_color='#A567BB',
            segmented_button_selected_hover_color='#A567BB',
            segmented_button_unselected_hover_color='#A567BB',
            segmented_button_unselected_color='#bc91e6'
        )
        self.frame_filmes.place(x=350, y=80)
        self.frame_filmes.add('INDICAÇÃO PRINCIPAL')
        self.frame_filmes.add('OPÇÃO 1')
        self.frame_filmes.add('OPÇÃO 2')
        self.frame_filmes.add('OPÇÃO 3')
        
        self.mostrar_titulo_principal = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            text=f'Título: {self.titulo_principal_convertido}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_titulo_principal.grid(row=0, column=0, padx=10, pady=10)
        
        '''self.mostrar_lançamento_principal = ctk.CTkLabel(
            self.frame_filme_principal,
            text=f'Data de Lançamento: {self.lançamento_principal_convertido}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_lançamento_principal.grid(row=1, column=0, padx=10, pady=10)
        
        self.mostrar_tmdb_nota_principal = ctk.CTkLabel(
            self.frame_filme_principal,
            text=f'Nota IMDB: {self.tmdb_nota_principal_convertido}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_tmdb_nota_principal.grid(row=2, column=0, padx=10, pady=10)'''
        


        
        
        
        
    






