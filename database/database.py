
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
                Username TEXT NOT NULL, 
                Numero INTEGER NOT NULL,
                Senha TEXT NOT NULL, 
                Confirmar_senha TEXT NOT NULL
            );
        ''') #cria comandos sql no python de forma organizada
        self.conn.commit() #coloca os dados na tabela
        print('Tabela criada com sucesso.')
        self.desconectar_db()

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
        #verficar se já existe um usuário cadastrado
        self.cursor.execute("""
        SELECT COUNT(*) FROM Usuarios WHERE Username = ?""", 
        (self.username_cadastro,)
        )
        self.count_username = self.cursor.fetchone()[0]
        
        try:
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
            elif (len(self.username_cadastro) < 4):
                CTkMessagebox(title= 'Nome de usuário inválido!',
                              message= 'O username deve conter mais de 4 caracteres.', 
                              icon= 'warning', 
                              button_color='#A567BB', 
                              button_hover_color='#bc91e6',
                              font=('Berlin Sans FB', 16)
                )
            elif (self.count_username > 0):
                CTkMessagebox(title= 'Nome de usuário inválido!',
                              message= 'Esse nome já está em uso. Tente novamente.',
                              icon= 'warning', 
                              button_color='#A567BB',
                              button_hover_color='#bc91e6',
                              font=('Berlin Sans FB', 16)
                )    
            elif (len(self.senha_cadastro_cadastro) < 6):
                CTkMessagebox(title= 'Senha inválida!',
                              message= 'A senha deve conter mais de 5 caracteres.', 
                              icon= 'warning',
                              button_color='#A567BB', 
                              button_hover_color='#bc91e6',
                              font=('Berlin Sans FB', 16)
                )
            elif (len(self.numero_cadastro) < 11):
                CTkMessagebox(title= 'Número com formato inválido!',
                              message= 'Digite apenas números no formato: \n(xx) xxxxx-xxxx', 
                              icon= 'warning',
                              button_color='#A567BB', 
                              button_hover_color='#bc91e6',
                              font=('Berlin Sans FB', 16)
                )
            elif (self.senha_cadastro != self.confirmar_senha_cadastro):
                CTkMessagebox(title= 'Erro!',
                    message= 'As senhas não são as mesmas! \nVerifique novamente.',
                    icon= 'cancel', 
                    button_color='#A567BB',
                    button_hover_color='#bc91e6',
                    font=('Berlin Sans FB', 16)
                )
              
            else:
                self.conn.commit()
                self.cadastro_finalizado()
                self.desconectar_db() 

        except:
            CTkMessagebox(title= 'Erro!',
                message= 'Erro ao cadastrar. Tente novamente!', 
                icon= 'cancel', 
                button_color='#A567BB', 
                button_hover_color='#bc91e6',
                font=('Berlin Sans FB', 16)
            )
            self.desconectar_db() 
    
    def verificar_login(self):
        self.username_login = self.entrada_login_username.get()
        self.senha_login = self.entrada_senha_login.get()
        self.conectar_db()
        self.cursor.execute("""SELECT * FROM Usuarios WHERE
                            (Username = ? AND Senha = ?)""",
                            (self.username_login, self.senha_login))
        self.verificar_dados = self.cursor.fetchone() #percorrer a tabela de usuários
        self.verificar_dados = self.cursor.fetchone() #percorrer a tabela de usuários
        
        try:
            if (self.username_login == '' or self.username == '' ):
                CTkMessagebox(title= 'Inválido!',
                              message= 'Preencha todos os campos.', 
                              icon= 'warning',
                              button_color='#A567BB',
                              button_hover_color='#bc91e6',
                              font=('Berlin Sans FB', 16)
                )
            elif (self.username_login in self.verificar_dados and
                self.senha_login in self.verificar_dados):
                self.abrir_janela_login()
                self.desconectar_db()
                
        except:
            CTkMessagebox(title= 'Erro!',
                message= 'Usuario não cadastrado!', 
                icon= 'cancel', 
                button_color='#A567BB', 
                button_hover_color='#bc91e6',
                font=('Berlin Sans FB', 16)
            )
            self.desconectar_db()
  