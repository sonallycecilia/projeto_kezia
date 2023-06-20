import customtkinter as ctk


class JanelaUsuario(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Página do Usuário')
        self.geometry("1450x800")
        self.opcoes_usuario()
        '''self.ultimos_vistos()'''
    

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
        
        #tab geral
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
            text='selecione os seus gêneros \nde filme favoritos:',
            font=('Berlin Sans FB', 20)
        )   
        self.label_intrucoes.grid(row=0, column=0, pady=15)
       
        # botões de categoria
        self.btn_cadastro_acao = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='AÇÃO',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
        )
        self.btn_cadastro_acao.grid(row=2, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_aventura = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='AVENTURA',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_aventura.grid(row=3, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_animacao = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='ANIMAÇÃO',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_animacao.grid(row=4, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_comedia = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='COMÉDIA',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_comedia.grid(row=5, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_crime = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='CRIME',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_crime.grid(row=6, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_documentario = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='DOCUMENTÁRIO',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_documentario.grid(row=7, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_drama = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='DRAMA',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_drama.grid(row=8, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_familia = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='FAMÍLIA',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_familia.grid(row=9, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_fantasia = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='FANTASIA',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_fantasia.grid(row=10, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_historia = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='HISTÓRIA',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_historia.grid(row=11, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_terror = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='TERROR',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_terror.grid(row=12, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_musica = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='MÚSICA',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_musica.grid(row=13, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_misterio = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='MISTÉRIO',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_misterio.grid(row=14, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_romance = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='ROMANCE',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_romance.grid(row=15, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_scifi = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='FICÇÃO CIENTÍFICA',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_scifi.grid(row=16, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_cinemaTV = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='CINEMA TV',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_cinemaTV.grid(row=17, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_thriller = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='THRILLER',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_thriller.grid(row=18, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_guerra = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='GUERRA',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_guerra.grid(row=19, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_faroeste = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='FAROESTE',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_faroeste.grid(row=20, column=0, pady=1, padx=1, sticky='w')
        
        self.btn_cadastro_todasCategorias = ctk.CTkCheckBox(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='TODAS CATEGORIAS',
            font=('Berlin Sans FB', 14),
            corner_radius=30
        )
        self.btn_cadastro_todasCategorias.grid(row=21, column=0, pady=1, padx=1, sticky='w')
        
        #botão de gerar recomendação
        self.botao_recomendar = ctk.CTkButton(
            self.frame_usuario.tab('CATEGORIAS DE FILMES'),
            width=250,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='GERAR RECOMENDAÇÕES',
            font=('Berlin Sans FB', 16),
            corner_radius=15,
        )
        self.botao_recomendar.grid(row=22, column=0, pady=25, padx=5)
        
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
    