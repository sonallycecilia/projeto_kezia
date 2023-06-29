
import sqlite3
from CTkMessagebox import CTkMessagebox

class DataBase:
    def conectar_db(self): #conectar ao banco de dados
        self.conn = sqlite3.connect('database\Sistema_cadastro.db') #cria o banco
        self.cursor = self.conn.cursor() #ponto de entrada
        print('Banco de dados conectado.')
        
    def desconectar_db(self):
        self.conn.close() #desconecta o banco de dados
        print('Banco de dados desconectado.')
        
    def criar_tabela(self):
        self.conectar_db() #conecta ao banco de dados
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Usuarios(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT NOT NULL,
                Username TEXT NOT NULL UNIQUE, 
                Numero INTEGER NOT NULL,
                Senha TEXT NOT NULL, 
                Confirmar_senha TEXT NOT NULL
            );
        ''') #cria comandos sql no python de forma organizada
        self.conn.commit() #coloca os dados na tabela
        print('Tabela Usuario criada com sucesso.')
        self.desconectar_db()
    
    def validar_username(self):
        self.conectar_db()
        self.username_cadastro = self.entrada_username_cadastro.get()
        self.cursor.execute("SELECT * FROM usuarios WHERE username = ?",
                            (self.username_cadastro,))
        resultado_username = self.cursor.fetchone()
        self.desconectar_db()
        
        if resultado_username is None:
            CTkMessagebox(title= 'Liberado!',
                message= 'O nome de usuário é válido!', 
                icon= 'check', 
                button_color='#A567BB', 
                button_hover_color='#bc91e6',
                font=('Berlin Sans FB', 16)
            )
        if len(resultado_username) > 0:
            CTkMessagebox(title= 'Erro!',
                message= 'O nome de usuário já está em uso!', 
                icon= 'cancel', 
                button_color='#A567BB', 
                button_hover_color='#bc91e6',
                font=('Berlin Sans FB', 16)
            )
            
    def cadastrar_usuario(self):
        self.nome_cadastro = self.entrada_nome_cadastro.get()
        self.username_cadastro = self.entrada_username_cadastro.get()
        self.numero_cadastro = self.entrada_numero_cadastro.get()
        self.senha_cadastro = self.entrada_senha_cadastro.get()
        self.confirmar_senha_cadastro = self.entrada_confirmar_senha_cadastro.get()
        
        self.conectar_db()
        #insere os dados no banco de dados
        self.cursor.execute("""
            INSERT INTO Usuarios 
            (Nome, Username, Numero, Senha, Confirmar_senha)
            VALUES (?, ?, ?, ?, ?)""", 
            (self.nome_cadastro, self.username_cadastro,
            self.numero_cadastro, self.senha_cadastro,
            self.confirmar_senha_cadastro)
        )
        
        if (self.nome_cadastro == '' or self.username_cadastro == '' 
            or self.numero_cadastro == '' or self.senha_cadastro == '' 
            or self.confirmar_senha_cadastro == ''):
                CTkMessagebox(title= 'Erro!',
                                message= 'Preencha todos os campos!', 
                                icon= 'cancel', 
                                button_color='#A567BB', 
                                button_hover_color='#bc91e6',
                                font=('Berlin Sans FB', 16)
                )
                self.desconectar_db()            
        elif (len(self.username_cadastro) < 4):
            CTkMessagebox(title= 'Nome de usuário inválido!',
                            message= 'O username deve conter mais de 4 caracteres.', 
                            icon= 'warning', 
                            button_color='#A567BB', 
                            button_hover_color='#bc91e6',
                            font=('Berlin Sans FB', 16)
            )
            self.desconectar_db()            
        elif (len(self.senha_cadastro) < 6):
            CTkMessagebox(title= 'Senha inválida!',
                            message= 'A senha deve conter mais de 5 caracteres.', 
                            icon= 'warning',
                            button_color='#A567BB', 
                            button_hover_color='#bc91e6',
                            font=('Berlin Sans FB', 16)
            )
            self.desconectar_db()            
        elif (len(self.numero_cadastro) != 11):
            CTkMessagebox(title= 'Número com formato inválido!',
                            message= 'Digite apenas números no formato: \n(xx) xxxxx-xxxx', 
                            icon= 'warning',
                            button_color='#A567BB', 
                            button_hover_color='#bc91e6',
                            font=('Berlin Sans FB', 16)
            )
            self.desconectar_db()         
        elif (self.senha_cadastro != self.confirmar_senha_cadastro):
            CTkMessagebox(title= 'Erro!',
                message= 'As senhas não são as mesmas! \nVerifique novamente.',
                icon= 'cancel', 
                button_color='#A567BB',
                button_hover_color='#bc91e6',
                font=('Berlin Sans FB', 16)
            )
            self.desconectar_db()
        else:
            self.conn.commit()
            self.desconectar_db()
            self.limpar_entrada_cadastro()
            self.cadastro_finalizado()
    
    def verificar_login(self):
        self.username_login = self.entrada_login_username.get()
        self.senha_login = self.entrada_senha_login.get()
        self.conectar_db()
        self.cursor.execute("SELECT * FROM Usuarios WHERE Username = ? AND Senha = ?", (self.username_login, self.senha_login))
        self.verificar_dados = self.cursor.fetchone()

        if self.username_login == '' or self.senha_login == '':
            CTkMessagebox(title='Inválido!', message='Preencha todos os campos.', icon='warning',
                        button_color='#A567BB', button_hover_color='#bc91e6', font=('Berlin Sans FB', 16))
            self.desconectar_db()
        
        elif self.verificar_dados is None:
            CTkMessagebox(title='Erro!', message='Erro: Usuário não existente! Cadastre-se!', icon='cancel',
                        button_color='#A567BB', button_hover_color='#bc91e6', font=('Berlin Sans FB', 16))
            self.desconectar_db()
        
        elif (self.username_login in self.verificar_dados and
            self.senha_login in self.verificar_dados):
            self.abrir_janela_usuario()
            self.desconectar_db()
        
        else:
            CTkMessagebox(title= 'Erro!',
                        message= 'Erro ao efetuar o login! \nTente novamente.',
                        icon= 'cancel',
                        button_color='#A567BB',
                        button_hover_color='#bc91e6',
                        font=('Berlin Sans FB', 16)
                    )
            self.desconectar_db()
            
    def criar_tabela_filme(self):
        self.conectar_db()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Filmes(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT NOT NULL, 
                id_filme INTEGER,
                FOREIGN KEY (Username) REFERENCES Usuarios(Username)
            );
        ''')
        self.conn.commit() 
        print('Tabela Filmes criada com sucesso.')
        self.desconectar_db()
        
    def adicionar_filme_principal(self):
        self.conectar_db()
        if self.marcar_filme_principal._check_state == True:
            self.cursor.execute("""
                INSERT INTO Filmes
                (Username, id_filme)
                VALUES (?, ?)""", 
                (self.nome_usuario, self.id_filme_principal)
            )
            self.conn.commit()
            
        elif self.marcar_filme_principal._check_state == False:
            self.conectar_db()
            self.cursor.execute("""
                DELETE FROM Filmes
                WHERE (Username, id_filme) = (?, ?)""",
                (self.nome_usuario,  self.id_filme_principal)
            )
            self.conn.commit()
        self.desconectar_db()
                
    def adicionar_filme_op1(self):
        self.conectar_db()
        if self.marcar_filme_op1._check_state == True:
            self.cursor.execute("""
                INSERT INTO Filmes
                (Username, id_filme)
                VALUES (?, ?)""", 
                (self.nome_usuario, self.id_filme_op1)
            )
            self.conn.commit()
            self.desconectar_db()
            
        elif self.marcar_filme_op1._check_state == False:
            self.cursor.execute("""
                DELETE FROM Filmes
                WHERE (Username, id_filme) = (?, ?)""",
                (self.nome_usuario,  self.id_filme_op1)
            )
            self.conn.commit()
        self.desconectar_db()
            
    def adicionar_filme_op2(self):
        self.conectar_db()
        if self.marcar_filme_op2._check_state == True:
            self.cursor.execute("""
                INSERT INTO Filmes
                (Username, id_filme)
                VALUES (?, ?)""", 
                (self.nome_usuario, self.id_filme_op2)
            )
            self.conn.commit()
            self.desconectar_db()
            
        elif self.marcar_filme_op2._check_state == False:
            self.cursor.execute("""
                DELETE FROM Filmes
                WHERE (Username, id_filme) = (?, ?)""",
                (self.nome_usuario,  self.id_filme_op2)
            )
            self.conn.commit()
        self.desconectar_db()
    
    def adicionar_filme_op3(self):
        self.conectar_db()
        if self.marcar_filme_op3._check_state == True:
            self.cursor.execute("""
                INSERT INTO Filmes
                (Username, id_filme)
                VALUES (?, ?)""", 
                (self.nome_usuario, self.id_filme_op3)
            )
            self.conn.commit()
            self.desconectar_db()
            
        elif self.marcar_filme_op3._check_state == False:
            self.cursor.execute("""
                DELETE FROM Filmes
                WHERE (Username, id_filme) = (?, ?)""",
                (self.nome_usuario,  self.id_filme_op3)
            )
            self.conn.commit()
        self.desconectar_db()
        
    def lista_filmes_username(self):
        self.conectar_db()
        self.cursor.execute("""
            SELECT id_filme
            FROM Filmes
            WHERE Username = ?""",
            (self.nome_usuario,)
        )
        id_filmes = [row[0] for row in self.cursor.fetchall()]
        self.desconectar_db()
        return id_filmes