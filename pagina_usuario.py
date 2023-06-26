import customtkinter as ctk
from tkinter import *
from CTkMessagebox import CTkMessagebox
from tmdb_api import *
import webbrowser
from database.database import DataBase

class JanelaUsuario(ctk.CTkToplevel, DataBase):
    def __init__(self, nome_usuario, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Página do Usuário')  
        self.geometry("1450x800")
        self.nome_chave_usuario = nome_usuario
        self.nome_usuario = self.nome_chave_usuario
        self.id_genero = None
        self.opcoes_usuario()
        '''self.conectar_db()
        self.cursor.execute("SELECT Username FROM 'Usuarios'")
        for linha in self.cursor.fetchall():
            print(linha)'''
        

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
            self.id_genero = 16
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
            self.id_genero = 12
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
    
    def opcoes_usuario(self):
        #frame olá
        self.frame_nome = ctk.CTkFrame(self, width=290, height=50)
        self.frame_nome.place(x=20, y=20)
        self.label_ola = ctk.CTkLabel(
            self.frame_nome,
            text=f'Olá, {self.nome_usuario}!',
            font=('Berlin Sans FB', 28)
        )   
        self.label_ola.place(x=15, y=10)
        
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
            command=self.randomizar_filme
        )
        self.botao_recomendar.grid(row=21, column=0, pady=25, padx=5)
        
        #elementos dos dados pessoais
        self.label_dados = ctk.CTkLabel(
            self.frame_usuario.tab('DADOS PESSOAIS'),
            text='seus dados cadastrais:',
            font=('Berlin Sans FB', 20)
        )   
        self.label_dados.grid(row=0, column=0, pady=15)
        
    def randomizar_filme(self):
        if self.id_genero is not None:
            genre = self.id_genero
            filmes = movie_genre(genre)
            filmes_sorteados = random_movie_pag_genre()
    
            #informações do principal
            id_filme_principal = get_movie_id(filmes_sorteados, 0, filmes)
            titulo_principal = get_title(filmes_sorteados, 0, filmes)
            self.titulo_principal = titulo_principal
            nota_principal = get_tmdb_vote(filmes_sorteados, 0, filmes)
            self.nota_principal = nota_principal
            data_principal = get_date(filmes_sorteados, 0, filmes)
            self.lançamento_principal = data_principal
            diretor_principal = get_director(id_filme_principal)
            self.diretor_principal = diretor_principal
            url_poster_principal = get_poster(filmes_sorteados, 0, filmes)
            self.converter_imagem_principal = mostrar_imagem(url_poster_principal)
            trailer_principal = get_trailer(id_filme_principal)
            self.trailer_principal = trailer_principal
            sinopse_principal = get_overview(filmes_sorteados, 0, filmes)
            self.sinopse_principal = sinopse_principal
            stream_principal = get_streaming(id_filme_principal)
            self.stream_principal = stream_principal
            
            #informações da op1
            id_filme_op1= get_movie_id(filmes_sorteados, 1, filmes)
            titulo_op1 = get_title(filmes_sorteados, 1, filmes)
            self.titulo_op1 = titulo_op1
            url_poster_op1  = get_poster(filmes_sorteados, 1, filmes)
            self.converter_imagem_op1 = mostrar_imagem(url_poster_op1)
            nota_op1 = get_tmdb_vote(filmes_sorteados, 1, filmes)
            self.nota_op1 = nota_op1
            data_op1 = get_date(filmes_sorteados, 1, filmes)
            self.lançamento_op1 = data_op1
            diretor_op1  = get_director(id_filme_op1)
            self.diretor_op1 = diretor_op1
            trailer_op1  = get_trailer(id_filme_op1)
            self.trailer_op1  = trailer_op1
            sinopse_op1 = get_overview(filmes_sorteados, 1, filmes)
            self.sinopse_op1  = sinopse_op1
            stream_op1 = get_streaming(id_filme_op1)
            self.stream_op1 = stream_op1
            
            #informações op2
            id_filme_op2 = get_movie_id(filmes_sorteados, 2, filmes)
            titulo_op2 = get_title(filmes_sorteados, 2, filmes)
            self.titulo_op2 = titulo_op2
            url_poster_op2  = get_poster(filmes_sorteados, 2, filmes)
            self.converter_imagem_op2 = mostrar_imagem(url_poster_op2)
            nota_op2 = get_tmdb_vote(filmes_sorteados, 2, filmes)
            self.nota_op2 = nota_op2
            data_op2 = get_date(filmes_sorteados, 2, filmes)
            self.lançamento_op2 = data_op2
            diretor_op2  = get_director(id_filme_op2)
            self.diretor_op2 = diretor_op2
            trailer_op2  = get_trailer(id_filme_op2)
            self.trailer_op2  = trailer_op2
            sinopse_op2 = get_overview(filmes_sorteados, 2, filmes)
            self.sinopse_op2  = sinopse_op2
            stream_op2 = get_streaming(id_filme_op2)
            self.stream_op2 = stream_op2
            
            #informações op3
            id_filme_op3 = get_movie_id(filmes_sorteados, 3, filmes)
            titulo_op3 = get_title(filmes_sorteados, 3, filmes)
            self.titulo_op3 = titulo_op3
            url_poster_op3  = get_poster(filmes_sorteados, 3, filmes)
            self.converter_imagem_op3 = mostrar_imagem(url_poster_op3)
            nota_op3 = get_tmdb_vote(filmes_sorteados, 3, filmes)
            self.nota_op3 = nota_op3
            data_op3 = get_date(filmes_sorteados, 3, filmes)
            self.lançamento_op3 = data_op3
            diretor_op3  = get_director(id_filme_op3)
            self.diretor_op3 = diretor_op3
            trailer_op3  = get_trailer(id_filme_op3)
            self.trailer_op3  = trailer_op3
            sinopse_op3 = get_overview(filmes_sorteados, 3, filmes)
            self.sinopse_op3  = sinopse_op3
            stream_op3 = get_streaming(id_filme_op3)
            self.stream_op3 = stream_op3

        else:
            CTkMessagebox(title= 'Inválido!',
                message= 'Marque uma opção de gênero!', 
                icon= 'warning',
                button_color='#A567BB',
                button_hover_color='#bc91e6',
                font=('Berlin Sans FB', 16)
            )
        
        #tab dos filmes
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
            text=f'{self.titulo_principal}',
            font=('Berlin Sans FB', 28)
        )
        self.mostrar_titulo_principal.place(x=5, y=20)
        
        self.abrir_imagem_principal = ctk.CTkImage(
            self.converter_imagem_principal, 
            size=(300, 450)
            )
        self.mostrar_imagem_principal = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
                text='', 
                image=self.abrir_imagem_principal,)
        self.mostrar_imagem_principal.place(x=450, y=80)
        
        self.mostrar_lançamento_principal = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            text=f'Data de Lançamento: {self.lançamento_principal}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_lançamento_principal.place(x=5, y=80)
        
        self.mostrar_tmdb_nota_principal = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            text=f'Nota IMDB: {self.nota_principal}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_tmdb_nota_principal.place(x=5, y=100)
        
        self.mostrar_diretor_principal = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            text=f'Dirigido por: {self.diretor_principal}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_diretor_principal.place(x=5, y=120)

        self.titulo_sinopse_princial = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            text='Sinopse:',
            font=('Berlin Sans FB', 20)
        )
        self.titulo_sinopse_princial.place(x=5, y=180)
        
        self.mostrar_sinopse_principal = ctk.CTkTextbox(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            width=410,
            height=310,
            font=('Berlin Sans FB', 20)
        )
        self.mostrar_sinopse_principal.place(x=5, y=220)
        self.mostrar_sinopse_principal.insert("0.0", f"{self.sinopse_principal}")
        
        self.botao_trailer_principal = ctk.CTkButton(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            width=200,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='VER TRAILER',
            font=('Berlin Sans FB', 18),
            corner_radius=15,
            command=lambda: webbrowser.open(f'{self.trailer_principal}')
        )
        self.botao_trailer_principal.place(x=500, y=545)
        
        self.titulo_stream_princial = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            text='Plataforma de Stream:',
            font=('Berlin Sans FB', 20)
        )
        self.titulo_stream_princial.place(x=5, y=545)
        
        self.mostrar_stream_principal = ctk.CTkLabel(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            text=f'{self.stream_principal}',
            font=('Berlin Sans FB', 20)
        )
        self.mostrar_stream_principal.place(x=5, y=565)
        
        '''self.marcar_filme_principal = ctk.CTkSwitch(
            self.frame_filmes.tab('INDICAÇÃO PRINCIPAL'),
            width=50,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='marcar como visto',
            font=('Berlin Sans FB', 18),
            corner_radius=15
        )
        self.marcar_filme_principal.place(x=500, y=545)'''
        
        #informações op1
        self.mostrar_titulo_op1 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 1'),
            text=f'{self.titulo_op1}',
            font=('Berlin Sans FB', 28)
        )
        self.mostrar_titulo_op1.place(x=5, y=20)
        
        self.abrir_imagem_op1 = ctk.CTkImage(
            self.converter_imagem_op1, 
            size=(300, 450)
            )
        self.mostrar_imagem_op1 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 1'),
                text='', 
                image=self.abrir_imagem_op1,)
        self.mostrar_imagem_op1.place(x=450, y=80)
        
        self.mostrar_lançamento_op1 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 1'),
            text=f'Data de Lançamento: {self.lançamento_op1}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_lançamento_op1.place(x=5, y=80)
        
        self.mostrar_tmdb_nota_op1 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 1'),
            text=f'Nota IMDB: {self.nota_op1}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_tmdb_nota_op1.place(x=5, y=100)
        
        self.mostrar_diretor_op1 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 1'),
            text=f'Dirigido por: {self.diretor_op1}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_diretor_op1.place(x=5, y=120)
        
        self.titulo_sinopse_op1 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 1'),
            text='Sinopse:',
            font=('Berlin Sans FB', 20)
        )
        self.titulo_sinopse_op1.place(x=5, y=180)
        
        self.mostrar_sinopse_op1 = ctk.CTkTextbox(
            self.frame_filmes.tab('OPÇÃO 1'),
            width=410,
            height=310,
            font=('Berlin Sans FB', 20)
        )
        self.mostrar_sinopse_op1.place(x=5, y=220)
        self.mostrar_sinopse_op1.insert("0.0", f"{self.sinopse_op1}")
        
        self.botao_trailer_op1 = ctk.CTkButton(
            self.frame_filmes.tab('OPÇÃO 1'),
            width=200,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='VER TRAILER',
            font=('Berlin Sans FB', 18),
            corner_radius=15,
            command=lambda: webbrowser.open(f'{self.trailer_op1}')
        )
        self.botao_trailer_op1.place(x=500, y=545)
        
        self.titulo_stream_op1 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 1'),
            text='Plataforma de Stream:',
            font=('Berlin Sans FB', 20)
        )
        self.titulo_stream_op1.place(x=5, y=545)
        
        self.mostrar_stream_op1 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 1'),
            text=f'{self.stream_op1}',
            font=('Berlin Sans FB', 20)
        )
        self.mostrar_stream_op1.place(x=5, y=565)
        
        #informações op2
        self.mostrar_titulo_op2 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 2'),
            text=f'{self.titulo_op2}',
            font=('Berlin Sans FB', 28)
        )
        self.mostrar_titulo_op2.place(x=5, y=20)
        
        self.abrir_imagem_op2 = ctk.CTkImage(
            self.converter_imagem_op2, 
            size=(300, 450)
            )
        self.mostrar_imagem_op2 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 2'),
                text='', 
                image=self.abrir_imagem_op2,)
        self.mostrar_imagem_op2.place(x=450, y=80)
        
        self.mostrar_lançamento_op2 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 2'),
            text=f'Data de Lançamento: {self.lançamento_op2}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_lançamento_op2.place(x=5, y=80)
        
        self.mostrar_tmdb_nota_op2 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 2'),
            text=f'Nota IMDB: {self.nota_op2}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_tmdb_nota_op2.place(x=5, y=100)
        
        self.mostrar_diretor_op2 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 2'),
            text=f'Dirigido por: {self.diretor_op2}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_diretor_op2.place(x=5, y=120)
        
        self.titulo_sinopse_op2 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 2'),
            text='Sinopse:',
            font=('Berlin Sans FB', 20)
        )
        self.titulo_sinopse_op2.place(x=5, y=180)
        
        self.mostrar_sinopse_op2 = ctk.CTkTextbox(
            self.frame_filmes.tab('OPÇÃO 2'),
            width=410,
            height=310,
            font=('Berlin Sans FB', 20)
        )
        self.mostrar_sinopse_op2.place(x=5, y=220)
        self.mostrar_sinopse_op2.insert("0.0", f"{self.sinopse_op2}")
        
        self.botao_trailer_op2 = ctk.CTkButton(
            self.frame_filmes.tab('OPÇÃO 2'),
            width=200,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='VER TRAILER',
            font=('Berlin Sans FB', 18),
            corner_radius=15,
            command=lambda: webbrowser.open(f'{self.trailer_op2}')
        )
        self.botao_trailer_op2.place(x=500, y=545)
        
        self.titulo_stream_op2 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 2'),
            text='Plataforma de Stream:',
            font=('Berlin Sans FB', 20)
        )
        self.titulo_stream_op2.place(x=5, y=545)
        
        self.mostrar_stream_op2 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 2'),
            text=f'{self.stream_op2}',
            font=('Berlin Sans FB', 20)
        )
        self.mostrar_stream_op2.place(x=5, y=565)
        
        #informações op3
        self.mostrar_titulo_op3 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 3'),
            text=f'{self.titulo_op3}',
            font=('Berlin Sans FB', 28)
        )
        self.mostrar_titulo_op3.place(x=5, y=20)
        
        self.abrir_imagem_op3 = ctk.CTkImage(
            self.converter_imagem_op3, 
            size=(300, 450)
            )
        self.mostrar_imagem_op3 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 3'),
                text='', 
                image=self.abrir_imagem_op3,)
        self.mostrar_imagem_op3.place(x=450, y=80)
        
        self.mostrar_lançamento_op3 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 3'),
            text=f'Data de Lançamento: {self.lançamento_op3}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_lançamento_op3.place(x=5, y=80)
        
        self.mostrar_tmdb_nota_op3 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 3'),
            text=f'Nota IMDB: {self.nota_op3}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_tmdb_nota_op3.place(x=5, y=100)
        
        self.mostrar_diretor_op3 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 3'),
            text=f'Dirigido por: {self.diretor_op3}',
            font=('Berlin Sans FB', 18)
        )
        self.mostrar_diretor_op3.place(x=5, y=120)
        
        self.titulo_sinopse_op3 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 3'),
            text='Sinopse:',
            font=('Berlin Sans FB', 20)
        )
        self.titulo_sinopse_op3.place(x=5, y=180)
        
        self.mostrar_sinopse_op3 = ctk.CTkTextbox(
            self.frame_filmes.tab('OPÇÃO 3'),
            width=410,
            height=310,
            font=('Berlin Sans FB', 20)
        )
        self.mostrar_sinopse_op3.place(x=5, y=220)
        self.mostrar_sinopse_op3.insert("0.0", f"{self.sinopse_op3}")
        
        self.botao_trailer_op3 = ctk.CTkButton(
            self.frame_filmes.tab('OPÇÃO 3'),
            width=200,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='VER TRAILER',
            font=('Berlin Sans FB', 18),
            corner_radius=15,
            command=lambda: webbrowser.open(f'{self.trailer_op3}')
        )
        self.botao_trailer_op3.place(x=500, y=545)
        
        self.titulo_stream_op3 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 3'),
            text='Plataforma de Stream:',
            font=('Berlin Sans FB', 20)
        )
        self.titulo_stream_op3.place(x=5, y=545)
        
        self.mostrar_stream_op3 = ctk.CTkLabel(
            self.frame_filmes.tab('OPÇÃO 3'),
            text=f'{self.stream_op3}',
            font=('Berlin Sans FB', 20)
        )
        self.mostrar_stream_op3.place(x=5, y=565)
        
    '''def ultimos_vistos(self):
        self.frame_filmes_recentes = ctk.CTkTabview(
            self,
            width=100, 
            height=750,
            segmented_button_selected_color='#A567BB',
            segmented_button_fg_color='#A567BB',
            segmented_button_selected_hover_color='#A567BB',
            segmented_button_unselected_hover_color='#A567BB',
            segmented_button_unselected_color='#bc91e6'
        )
        self.frame_filmes_recentes.place(x=900, y=80)
        self.frame_filmes_recentes.add('ULTIMOS VISTOS')'''

