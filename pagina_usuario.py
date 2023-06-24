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
        self.pegar_imagem(self.poster)
        self.pegar_poster()
        
        #variaveis
        self.id_genero = None

    #verificação dos estados do botão e atribuição de valor a variavel self.id_genero
    def verificar_botao_acao(self):
        if self.botao_acao._check_state == True:
            self.id_genero = 28
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)       
        else:
            self.id_genero = None
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_animacao(self):    
        if self.botao_animacao._check_state == True:
            self.id_genero = 12
            self.botao_acao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_aventura(self):
        if self.botao_aventura._check_state == True:
            self.id_genero = 16
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)    

    def verificar_botao_cinemaTV(self):
        if self.botao_cinemaTV._check_state == True:
            self.id_genero = 10770
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL) 
    
    def verificar_botao_comedia(self):
        if self.botao_comedia._check_state == True:
            self.id_genero = 35
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
            
    def verificar_botao_crime(self):
        if self.botao_crime._check_state == True:
            self.id_genero = 80
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_documentario(self):
        if self.botao_documentario._check_state == True:
            self.id_genero = 99
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_drama(self):
        if self.botao_drama._check_state == True:
            self.id_genero = 18
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_familia(self):
        if self.botao_familia._check_state == True:
            self.id_genero = 10751
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_fantasia(self):
        if self.botao_fantasia._check_state == True:
            self.id_genero = 14
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_faroeste(self):
        if self.botao_faroeste._check_state == True:
            self.id_genero = 37
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_guerra(self):
        if self.botao_guerra._check_state == True:
            self.id_genero = 10752
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_historia(self):
        if self.botao_historia._check_state == True:
            self.id_genero = 36
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_misterio(self):
        if self.botao_misterio._check_state == True:
            self.id_genero = 9648
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_musica(self):
        if self.botao_musica._check_state == True:
            self.id_genero = 10402
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_romance(self):
        if self.botao_romance._check_state == True:
            self.id_genero = 10749
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_scifi(self):
        if self.botao_scifi._check_state == True:
            self.id_genero = 878
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_terror(self):
        if self.botao_terror._check_state == True:
            self.id_genero = 27
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_thriller.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_thriller.configure(state=NORMAL)
    
    def verificar_botao_thriller(self):
        if self.botao_thriller._check_state == True:
            self.id_genero = 53
            self.botao_acao.configure(state=DISABLED)
            self.botao_animacao.configure(state=DISABLED)
            self.botao_aventura.configure(state=DISABLED)
            self.botao_cinemaTV.configure(state=DISABLED)
            self.botao_comedia.configure(state=DISABLED)
            self.botao_crime.configure(state=DISABLED)
            self.botao_documentario.configure(state=DISABLED)
            self.botao_drama.configure(state=DISABLED)
            self.botao_familia.configure(state=DISABLED)
            self.botao_fantasia.configure(state=DISABLED)
            self.botao_faroeste.configure(state=DISABLED)
            self.botao_guerra.configure(state=DISABLED)
            self.botao_historia.configure(state=DISABLED)
            self.botao_misterio.configure(state=DISABLED)
            self.botao_musica.configure(state=DISABLED)
            self.botao_romance.configure(state=DISABLED)
            self.botao_scifi.configure(state=DISABLED)
            self.botao_terror.configure(state=DISABLED)
        else:
            self.id_genero = None
            self.botao_acao.configure(state=NORMAL)
            self.botao_animacao.configure(state=NORMAL)
            self.botao_aventura.configure(state=NORMAL)
            self.botao_cinemaTV.configure(state=NORMAL)
            self.botao_comedia.configure(state=NORMAL)
            self.botao_crime.configure(state=NORMAL)
            self.botao_documentario.configure(state=NORMAL)
            self.botao_drama.configure(state=NORMAL)
            self.botao_familia.configure(state=NORMAL)
            self.botao_fantasia.configure(state=NORMAL)
            self.botao_faroeste.configure(state=NORMAL)
            self.botao_guerra.configure(state=NORMAL)
            self.botao_historia.configure(state=NORMAL)
            self.botao_misterio.configure(state=NORMAL)
            self.botao_musica.configure(state=NORMAL)
            self.botao_romance.configure(state=NORMAL)
            self.botao_scifi.configure(state=NORMAL)
            self.botao_terror.configure(state=NORMAL)
    
    #backend api
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

        self.response = requests.get(self.url)

        if self.response.status_code == 200:
            self.imagem = Image.open(BytesIO(self.response.content))
            self.res = self.imagem.show()
            return self.res
        else:
            self.res = "Falha ao obter a imagem"
            return None
    
    def pegar_poster(self, lista, indice, transform_movie):
        self.movie = lista[indice]
        self.poster = transform_movie["results"][self.movie]["poster_path"]
        return self.poster
    
    def pegar_diretor(self, id_filme):
        self.url = "https://api.themoviedb.org/3/movie/"+ str(id_filme) +"/credits?language=pt-BR"

        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MzQ4YjZlYTcwZmIyZmFlYmEzOWFhNmIyYTg5YTY2ZCIsInN1YiI6IjY0N2Y2YTMwMzg1MjAyMDBhZjE0ZTAxMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KRNryLZZzPdxCe0c6UYv6LLlzZlAnrVGd8Y4q8xCm-0"
        }

        self.response = requests.get(self.url, headers=self.headers)

        return self.response.text

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
                message= 'Marque uma opção de gênero!', 
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
        self.filme_id_principal = self.transform_movie['results'][self.pos_filme_principal]["id"]
        self.poster = self.transform_movie["results"][self.pos_filme_principal]["poster_path"]
        '''self.obter_trailer = self.get_trailer(str(self.filme_id))
        self.transformar_trailer = json.loads(self.obter_trailer)
        self.trailers = self.transformar_trailer['results']
        self.obter_diretor = self.pegar_director(str(self.filme_id))
        self.transform_director = json.loads(self.obter_diretor)'''
        
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

        #informação frame principal
        self.mostrar_titulo_principal = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            text=f'Título: {self.titulo_principal_convertido}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_titulo_principal.grid(row=0, column=0, padx=10, pady=10)
        
        self.mostrar_lançamento_principal = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            text=f'Data de Lançamento: {self.lançamento_principal_convertido}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_lançamento_principal.grid(row=1, column=0, padx=10, pady=10)
        
        self.mostrar_tmdb_nota_principal = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            text=f'Nota IMDB: {self.tmdb_nota_principal_convertido}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_tmdb_nota_principal.grid(row=2, column=0, padx=10, pady=10)

        '''self.mostra_essa_bosta = self.pegar_imagem(self.poster)
        self.poster_filme_principal = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'), 
            text='', 
            image=self.mostra_essa_bosta
        )
        self.poster_filme_principal.grid(row=3, column=0, padx=10, pady=10)'''
        
    def opcoes_usuario(self):
        #frame olá
        self.frame_nome = ctk.CTkFrame(self, width=50, height=50)
        self.frame_nome.place(x=20, y=20)
        self.label_ola = ctk.CTkLabel(
            self.frame_nome,
            text='  Olá, nome!  ',
            font=('Berlin Sans FB', 28)
        )   
        self.label_ola.grid(row=0, column=0, pady=15, padx=15)
        
        #tab geral do usuario
        self.frame_usuario = ctk.CTkTabview(
            self,
            width=250, 
            height=750,
            segmented_button_selected_color='#A567BB',
            segmented_button_fg_color='#A567BB',
            segmented_button_selected_hover_color='#A567BB',
            segmented_button_unselected_hover_color='#A567BB',
            segmented_button_unselected_color='#bc91e6'
        )
        self.frame_usuario.place(x=20, y=80)
        self.frame_usuario.add('CATEGORIAS DE FILMES')
        self.frame_usuario.add('DADOS PESSOAIS')
        
        #elementos da tab categorias
        self.label_intrucoes = ctk.CTkLabel(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            text='selecione um gênero abaixo \npara indicarmos um filme:',
            font=('Berlin Sans FB', 20)
        )   
        self.label_intrucoes.grid(row=0, column=0, pady=15)
       
        # botões de categoria
        self.botao_acao = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='AÇÃO',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_acao
        )
        self.botao_acao.grid(row=2, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_animacao = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='ANIMAÇÃO',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_animacao
        )
        self.botao_animacao.grid(row=3, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_aventura = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='AVENTURA',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_aventura
        )
        self.botao_aventura.grid(row=4, column=0, pady=1, padx=1, sticky='w')
    
        self.botao_cinemaTV = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='CINEMA TV',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_cinemaTV
        )
        self.botao_cinemaTV.grid(row=5, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_comedia = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='COMÉDIA',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_comedia
        )
        self.botao_comedia.grid(row=6, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_crime = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='CRIME',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_crime
        )
        self.botao_crime.grid(row=7, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_documentario = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='DOCUMENTÁRIO',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_documentario
        )
        self.botao_documentario.grid(row=8, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_drama = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='DRAMA',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_drama
        )
        self.botao_drama.grid(row=9, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_familia = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='FAMÍLIA',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_familia
        )
        self.botao_familia.grid(row=10, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_fantasia = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='FANTASIA',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_fantasia
        )
        self.botao_fantasia.grid(row=11, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_faroeste = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='FAROESTE',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_faroeste
        )
        self.botao_faroeste.grid(row=12, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_guerra = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='GUERRA',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_guerra
        )
        self.botao_guerra.grid(row=13, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_historia = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='HISTÓRIA',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_historia
        )
        self.botao_historia.grid(row=14, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_misterio = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='MISTÉRIO',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_misterio
        )
        self.botao_misterio.grid(row=15, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_musica = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='MÚSICA',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_musica
        )
        self.botao_musica.grid(row=16, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_romance = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='ROMANCE',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_romance
        )
        self.botao_romance.grid(row=17, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_scifi = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='FICÇÃO CIENTÍFICA',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_scifi
        )
        self.botao_scifi.grid(row=18, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_terror = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='TERROR',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_terror
        )
        self.botao_terror.grid(row=19, column=0, pady=1, padx=1, sticky='w')
        
        self.botao_thriller = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='THRILLER',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.verificar_botao_thriller
        )
        self.botao_thriller.grid(row=20, column=0, pady=1, padx=1, sticky='w')
        
        #botão de gerar recomendação
        self.botao_recomendar = ctk.CTkButton(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            width=250,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='GERAR RECOMENDAÇÃO',
            font=('Berlin Sans FB', 16),
            corner_radius=15,
            command=self.main_api
        )
        self.botao_recomendar.grid(row=21, column=0, pady=25, padx=5)
        
        #elementos dos dados pessoais
        self.label_dados = ctk.CTkLabel(
            self.frame_usuario.tab('DADOS PESSOAIS'),
            text='seus dados cadastrais:',
            font=('Berlin Sans FB', 20)
        )   
        self.label_dados.grid(row=0, column=0, pady=15)
          
    def filme_principal(self):
        pass
