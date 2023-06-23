import customtkinter as ctk
from tkinter import *

class JanelaUsuario(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Página do Usuário')
        self.geometry("1450x800")
        self.opcoes_usuario()
        '''self.ultimos_vistos()'''
        self.id_filme = None

    #verificação dos estados do botão e atribuição de valor a variavel self.id_filme
    def verificar_botao_acao(self):
        if self.botao_acao._check_state == True:
            self.id_filme = 28
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
            self.id_filme = None
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
            self.id_filme = 12
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
            self.id_filme = None
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
            self.id_filme = 16
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
            self.id_filme = None
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
            self.id_filme = 10770
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
            self.id_filme = None
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
            self.id_filme = 35
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
            self.id_filme = None
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
            self.id_filme = 80
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
            self.id_filme = None
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
            self.id_filme = 99
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
            self.id_filme = None
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
            self.id_filme = 18
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
            self.id_filme = None
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
            self.id_filme = 10751
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
            self.id_filme = None
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
            self.id_filme = 14
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
            self.id_filme = None
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
            self.id_filme = 37
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
            self.id_filme = None
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
            self.id_filme = 10752
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
            self.id_filme = None
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
            self.id_filme = 36
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
            self.id_filme = None
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
            self.id_filme = 9648
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
            self.id_filme = None
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
            self.id_filme = 10402
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
            self.id_filme = None
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
            self.id_filme = 10749
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
            self.id_filme = None
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
            self.id_filme = 878
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
            self.id_filme = None
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
            self.id_filme = 27
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
            self.id_filme = None
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
            self.id_filme = 53
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
            self.id_filme = None
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
        )
        self.botao_recomendar.grid(row=21, column=0, pady=25, padx=5)
        
        #elementos dos dados pessoais
        self.label_dados = ctk.CTkLabel(
            self.frame_usuario.tab('DADOS PESSOAIS'),
            text='seus dados cadastrais:',
            font=('Berlin Sans FB', 20)
        )   
        self.label_dados.grid(row=0, column=0, pady=15)
          
    def ultimos_vistos(self):
        self.frame_ultimo_vistos = ctk.CTkFrame(self, width=800, height=200)
        self.frame_ultimo_vistos.place(x=280, y=500)
    