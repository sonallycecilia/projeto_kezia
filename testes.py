def autenticar_usuario(self):
        self.username_login = self.username_login_entry.get()
        self.senha_login = self.senha_login_entry.get()
        print(f'Usuário: {self.username_login}\nSenha: {self.senha_login}')
        
        # Verificando se os dados de entrada estão vazios
        if self.username_login == '' or self.senha_login == '':
            CTkMessagebox(
                title='Sistema de login',
                icon='cancel',
                message='ERRO!!!\nPreencha todos os campos',
            )
        else:
            self.conectar_banco()
            self.cursor.execute(
                """SELECT * FROM Usuarios WHERE (Username=? AND senha=?)""",
                (self.username_login, self.senha_login))
            self.verifica_dados = self.cursor.fetchone()
            
            if self.verifica_dados is not None:
                self.abrir_janela_usuario()
                print('pqp')
                self.limpa_entry_login()
            else:
                CTkMessagebox(
                    title='Erro de Login',
                    icon='cancel',
                    message='Usuário não encontrado.'
                            '\nPor favor verifique seus dados ou cadastre-se novamente.'