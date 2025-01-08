import json 
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox, simpledialog, font


class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        self.__disponivel = True

    def to_dict(self):
        return {
            'titulo': self.__titulo,
            'autor': self.__autor,
            'disponivel': self.__disponivel
        }

    @classmethod
    def from_dict(cls, data):
        livro = cls(data['titulo'], data['autor'])
        livro.__disponivel = data['disponivel']
        return livro

    def __str__(self):
        return f"{self.__titulo} por {self.__autor} - {'Disponível' if self.__disponivel else 'Indisponível'}"


class Usuario:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def calcular_dias_emprestimo(self):
        return 14

    def to_dict(self):
        return {
            'nome': self.__nome,
            'email': self.__email,
            'tipo': self.__class__.__name__
        }

    @classmethod
    def from_dict(cls, data):
        if data['tipo'] == 'UsuarioComum':
            return UsuarioComum(data['nome'], data['email'])
        elif data['tipo'] == 'UsuarioPremium':
            return UsuarioPremium(data['nome'], data['email'])
        return cls(data['nome'], data['email'])

    def __str__(self):
        return self.__nome


class UsuarioComum(Usuario):
    def calcular_dias_emprestimo(self):
        return 14  # 14 dias para usuários comuns


class UsuarioPremium(Usuario):
    def calcular_dias_emprestimo(self):
        return 30  # 30 dias para usuários premium


class Emprestimo:
    def __init__(self, livro, usuario):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = datetime.now()
        self.data_devolucao = self.data_emprestimo + timedelta(days=usuario.calcular_dias_emprestimo())

    def finalizar(self):
        self.livro.devolver()


class Biblioteca:
    def __init__(self):
        self.__livros = []
        self.__usuarios = []

    def adicionar_livro(self, livro):
        self.__livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def remover_livro(self, titulo):
        for livro in self.__livros:
            if livro.to_dict()['titulo'] == titulo:
                self.__livros.remove(livro)
                return True
        return False

    def remover_usuario(self, nome):
        for usuario in self.__usuarios:
            if usuario.to_dict()['nome'] == nome:
                self.__usuarios.remove(usuario)
                return True
        return False

    def realizar_emprestimo(self, livro, usuario):
        if livro.emprestar():
            return Emprestimo(livro, usuario)
        return None

    def carregar_dados(self):
        try:
            with open('biblioteca.json', 'r') as f:
                data = json.load(f)
                self.__livros = [Livro.from_dict(livro) for livro in data['livros']]
                self.__usuarios = [Usuario.from_dict(usuario) for usuario in data['usuarios']]
        except FileNotFoundError:
            pass

    def salvar_dados(self):
        data = {
            'livros': [livro.to_dict() for livro in self.__livros],
            'usuarios': [usuario.to_dict() for usuario in self.__usuarios]
        }
        with open('biblioteca.json', 'w') as f:
            json.dump(data, f, indent=4)

    def listar_livros(self):
        return [str(livro) for livro in self.__livros]

    def listar_usuarios(self):
        return [str(usuario) for usuario in self.__usuarios]


class BibliotecaApp:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.biblioteca.carregar_dados()

        self.root = root
        self.root.title("Biblioteca Virtual")

        # Maximiza a janela
        self.root.state('zoomed')

        # Estilo e fontes
        self.font_title = font.Font(family="Helvetica", size=20, weight="bold")
        self.font_buttons = font.Font(family="Arial", size=12)

        # Configuração da interface
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.frame, text="Biblioteca Virtual", font=self.font_title)
        self.label.pack(pady=20)

        self.listbox = tk.Listbox(self.frame, width=50, height=15, font=self.font_buttons)
        self.listbox.pack(pady=10)

        self._criar_botoes()

    def _criar_botoes(self):
        btn_adicionar_livro = tk.Button(self.frame, text="Adicionar Livro", command=self.adicionar_livro, font=self.font_buttons, bg="#4CAF50", fg="white", relief="raised")
        btn_adicionar_livro.pack(fill=tk.X, pady=5)

        btn_adicionar_usuario = tk.Button(self.frame, text="Adicionar Usuário", command=self.adicionar_usuario, font=self.font_buttons, bg="#4CAF50", fg="white", relief="raised")
        btn_adicionar_usuario.pack(fill=tk.X, pady=5)

        btn_remover_livro = tk.Button(self.frame, text="Remover Livro", command=self.remover_livro, font=self.font_buttons, bg="#f44336", fg="white", relief="raised")
        btn_remover_livro.pack(fill=tk.X, pady=5)

        btn_remover_usuario = tk.Button(self.frame, text="Remover Usuário", command=self.remover_usuario, font=self.font_buttons, bg="#f44336", fg="white", relief="raised")
        btn_remover_usuario.pack(fill=tk.X, pady=5)

        btn_emprestar = tk.Button(self.frame, text="Realizar Empréstimo", command=self.realizar_emprestimo, font=self.font_buttons, bg="#008CBA", fg="white", relief="raised")
        btn_emprestar.pack(fill=tk.X, pady=5)

        btn_listar_livros = tk.Button(self.frame, text="Listar Livros", command=self.listar_livros, font=self.font_buttons, bg="#008CBA", fg="white", relief="raised")
        btn_listar_livros.pack(fill=tk.X, pady=5)

        btn_listar_usuarios = tk.Button(self.frame, text="Listar Usuários", command=self.listar_usuarios, font=self.font_buttons, bg="#008CBA", fg="white", relief="raised")
        btn_listar_usuarios.pack(fill=tk.X, pady=5)

        btn_salvar = tk.Button(self.frame, text="Salvar Dados", command=self.biblioteca.salvar_dados, font=self.font_buttons, bg="#e7e7e7", fg="black", relief="raised")
        btn_salvar.pack(fill=tk.X, pady=5)

    def adicionar_livro(self):
        titulo = simpledialog.askstring("Título do Livro", "Digite o título do livro:")
        autor = simpledialog.askstring("Autor do Livro", "Digite o autor do livro:")
        if titulo and autor:
            livro = Livro(titulo, autor)
            self.biblioteca.adicionar_livro(livro)
            messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")

    def adicionar_usuario(self):
        nome = simpledialog.askstring("Nome do Usuário", "Digite o nome do usuário:")
        email = simpledialog.askstring("Email do Usuário", "Digite o email do usuário:")
        tipo_usuario = simpledialog.askstring("Tipo de Usuário", "Digite 'comum' ou 'premium':").lower()

        if nome and email:
            if tipo_usuario == 'comum':
                usuario = UsuarioComum(nome, email)
            elif tipo_usuario == 'premium':
                usuario = UsuarioPremium(nome, email)
            else:
                messagebox.showerror("Erro", "Tipo de usuário inválido. Use 'comum' ou 'premium'.")
                return

            self.biblioteca.adicionar_usuario(usuario)
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")

    def remover_livro(self):
        titulo = simpledialog.askstring("Remover Livro", "Digite o título do livro a ser removido:")
        if titulo:
            if self.biblioteca.remover_livro(titulo):
                messagebox.showinfo("Sucesso", "Livro removido com sucesso!")
            else:
                messagebox.showerror("Erro", "Livro não encontrado.")

    def remover_usuario(self):
        nome = simpledialog.askstring("Remover Usuário", "Digite o nome do usuário a ser removido:")
        if nome:
            if self.biblioteca.remover_usuario(nome):
                messagebox.showinfo("Sucesso", "Usuário removido com sucesso!")
            else:
                messagebox.showerror("Erro", "Usuário não encontrado.")

    def realizar_emprestimo(self):
        if not self.biblioteca._Biblioteca__livros or not self.biblioteca._Biblioteca__usuarios:
            messagebox.showerror("Erro", "Adicione livros e usuários antes de realizar um empréstimo.")
            return

        livro_index = simpledialog.askinteger("Empréstimo", "Digite o índice do livro (0 a {}):".format(len(self.biblioteca._Biblioteca__livros) - 1))
        usuario_index = simpledialog.askinteger("Empréstimo", "Digite o índice do usuário (0 a {}):".format(len(self.biblioteca._Biblioteca__usuarios) - 1))

        if livro_index is not None and usuario_index is not None:
            try:
                livro = self.biblioteca._Biblioteca__livros[livro_index]
                usuario = self.biblioteca._Biblioteca__usuarios[usuario_index]
                emprestimo = self.biblioteca.realizar_emprestimo(livro, usuario)

                if emprestimo:
                    dias_emprestimo = usuario.calcular_dias_emprestimo()
                    messagebox.showinfo("Sucesso", f"Empréstimo realizado com sucesso!\nDevolução até: {emprestimo.data_devolucao.strftime('%d/%m/%Y')}\nO usuário tem {dias_emprestimo} dias para devolver o livro.")
                else:
                    messagebox.showerror("Erro", "Livro não disponível para empréstimo.")
            except IndexError:
                messagebox.showerror("Erro", "Índice inválido.")

    def listar_livros(self):
        self.listbox.delete(0, tk.END)
        for livro in self.biblioteca.listar_livros():
            self.listbox.insert(tk.END, livro)

    def listar_usuarios(self):
        self.listbox.delete(0, tk.END)
        for usuario in self.biblioteca.listar_usuarios():
            self.listbox.insert(tk.END, usuario)


if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
