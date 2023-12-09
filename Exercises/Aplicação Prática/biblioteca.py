class Usuario:
    def __init__(self, cpf, senha):
        self.cpf = cpf
        self.senha = senha

def realizar_cadastro():
    print("Cadastro de usuário:")
    cpf_usuario = input("Digite seu CPF como nome de usuário: ")

    while True:
        senha_usuario = input("Digite sua senha: ")
        confirma_senha = input("Confirme sua senha: ")

        if senha_usuario == confirma_senha:
            return Usuario(cpf=cpf_usuario, senha=senha_usuario)
        else:
            print("Senhas divergentes. Tente novamente.")

def realizar_login(usuarios):
    tentativas = 3
    while tentativas > 0:
        cpf_usuario = input("Digite seu CPF: ")
        senha_usuario = input("Digite sua senha: ")

        for usuario in usuarios:
            if cpf_usuario == usuario.cpf and senha_usuario == usuario.senha:
                print(f"Bem-vindo(a), {usuario.cpf}!")
                return True

        print("CPF ou senha incorretos. Tente novamente.")
        tentativas -= 1

    print("Número máximo de tentativas excedido. Saindo...")
    return False

def main():
    print("Seja bem-vindo(a) à biblioteca")

    usuarios = []  # Lista para armazenar os usuários cadastrados

    while True:
        print("[ 1 ] Tenho conta")
        print("[ 2 ] Não tenho uma conta")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Realizar login
            login_sucesso = realizar_login(usuarios)

            if login_sucesso:
                break  # Continua para a próxima seção ou finaliza o programa
        elif opcao == "2":
            # Realizar cadastro
            novo_usuario = realizar_cadastro()
            usuarios.append(novo_usuario)
            print("Cadastro realizado com sucesso! Faça login para continuar.")
        else:
            print("Opção inválida. Digite '1' para Tenho conta ou '2' para Não tenho uma conta.")

if __name__ == "__main__":
    main()

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class No:
    def __init__(self, livro):
        self.livro = livro
        self.esquerda = None
        self.direita = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        if no is None:
            return 0
        return no.altura

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y

    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esquerda) - self.altura(no.direita)

    def inserir(self, raiz, livro):
        if raiz is None:
            return No(livro)

        if livro.titulo < raiz.livro.titulo:
            raiz.esquerda = self.inserir(raiz.esquerda, livro)
        elif livro.titulo > raiz.livro.titulo:
            raiz.direita = self.inserir(raiz.direita, livro)
        else:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

        balanceamento = self.fator_balanceamento(raiz)

        if balanceamento > 1:
            if livro.titulo < raiz.esquerda.livro.titulo:
                return self.rotacao_direita(raiz)
            else:
                raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
                return self.rotacao_direita(raiz)

        if balanceamento < -1:
            if livro.titulo > raiz.direita.livro.titulo:
                return self.rotacao_esquerda(raiz)
            else:
                raiz.direita = self.rotacao_direita(raiz.direita)
                return self.rotacao_esquerda(raiz)

        return raiz

    def buscar(self, raiz, titulo):
        if raiz is None or raiz.livro.titulo == titulo:
            return raiz

        if titulo < raiz.livro.titulo:
            return self.buscar(raiz.esquerda, titulo)
        elif titulo > raiz.livro.titulo:
            return self.buscar(raiz.direita, titulo)
        else:
            return raiz

    def buscar_livro(self, titulo):
        no_encontrado = self.buscar(self.raiz, titulo)
        if no_encontrado:
            return no_encontrado.livro
        else:
            return None

class Biblioteca:
    def __init__(self):
        self.arvore_avl = AVL()

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.arvore_avl.raiz = self.arvore_avl.inserir(self.arvore_avl.raiz, livro)

    def buscar_livro(self, titulo):
        no_encontrado = self.arvore_avl.buscar_livro(titulo)
        if no_encontrado:
            return no_encontrado
        else:
            return None

# Exemplo de uso:
biblioteca = Biblioteca()
biblioteca.adicionar_livro("DOM QUIXOTE", "Miguel de Cervantes")
biblioteca.adicionar_livro("CEM ANOS DE SOLIDÃO", "Gabriel García Márquez")
biblioteca.adicionar_livro("CRIME E CASTIGO", "Fiódor Dostoiévski")
biblioteca.adicionar_livro("A REVOLUÇÃO DOS BICHOS", "George Orwell")
biblioteca.adicionar_livro("O GRANDE GATSBY", "F. Scott Fitzgerald")
biblioteca.adicionar_livro("O PEQUENO PRÍNCIPE", "Antoine de Saint-Exupéry")
biblioteca.adicionar_livro("A ARTE DA GUERRA", "Sun Tzu")
biblioteca.adicionar_livro("O NOME DO VENTO", "Patrick Rothfuss")
biblioteca.adicionar_livro("MAUS", "Art Spiegelman")
biblioteca.adicionar_livro("NORWEGIAN WOOD", "Haruki Murakami")
biblioteca.adicionar_livro("O HOBBIT", "J.R.R. Tolkien")
biblioteca.adicionar_livro("O PODER DO HÁBITO", "Charles Duhigg")
biblioteca.adicionar_livro("O SILMARILLION", "J.R.R. Tolkien")
biblioteca.adicionar_livro("O ALQUIMISTA", "Paulo Coelho")
biblioteca.adicionar_livro("A METAMORFOSE", "Franz Kafka")
biblioteca.adicionar_livro("OS MISERÁVEIS", "Victor Hugo")
biblioteca.adicionar_livro("A CABANA", "William P. Young")
biblioteca.adicionar_livro("OS TRÊS MOSQUETEIROS", "Alexandre Dumas")
biblioteca.adicionar_livro("O ESTRANGEIRO", "Albert Camus")
biblioteca.adicionar_livro("A SANGUE FRIO", "Truman Capote")
biblioteca.adicionar_livro("ORGULHO E PRECONCEITO", "Jane Austen")
biblioteca.adicionar_livro("ENSAIO SOBRE A CEGUEIRA", "José Saramago")
biblioteca.adicionar_livro("A MENINA QUE ROUBAVA LIVROS", "Markus Zusak")
biblioteca.adicionar_livro("O CÓDIGO DA VINCI", "Dan Brown")
biblioteca.adicionar_livro("A ILHA DO TESOURO", "Robert Louis Stevenson")
biblioteca.adicionar_livro("O MÉDICO", "Noah Gordon")
biblioteca.adicionar_livro("A SOCIEDADE DO ANEL", "J.R.R. Tolkien")
biblioteca.adicionar_livro("A BÍBLIA SATÂNICA", "Anton LaVey")
biblioteca.adicionar_livro("A TORRE NEGRA", "Stephen King")
biblioteca.adicionar_livro("O EXORCISTA", "William Peter Blatty")
biblioteca.adicionar_livro("A MENINA DO VALE", "Bel Pesce")
biblioteca.adicionar_livro("O GUIA DO MOCHILEIRO DAS GALÁXIAS", "Douglas Adams")
biblioteca.adicionar_livro("DRÁCULA", "Bram Stoker")
biblioteca.adicionar_livro("O RETRATO DE DORIAN GRAY", "Oscar Wilde")
biblioteca.adicionar_livro("GUERRA E PAZ", "Fiódor Dostoiévski")
biblioteca.adicionar_livro("A ODISSÉIA", "Homero")
biblioteca.adicionar_livro("A QUEDA DE GONDOLIN", "J.R.R. Tolkien")
biblioteca.adicionar_livro("A DIVINA COMÉDIA", "Dante Alighieri")
biblioteca.adicionar_livro("A REVOLTA DE ATLAS", "Ayn Rand")
biblioteca.adicionar_livro("O CEMITÉRIO", "Stephen King")
biblioteca.adicionar_livro("CREPÚSCULO", "Stephenie Meyer")
biblioteca.adicionar_livro("O DIÁRIO DE ANNE FRANK", "Anne Frank")
biblioteca.adicionar_livro("DUNA", "Frank Herbert")
biblioteca.adicionar_livro("A ORIGEM", "Dan Brown")
biblioteca.adicionar_livro("OS PILARES DA TERRA", "Ken Follett")
biblioteca.adicionar_livro("O MORRO DOS VENTOS UIVANTES", "Emily Brontë")
biblioteca.adicionar_livro("O CONDE DE MONTE CRISTO", "Alexandre Dumas")
biblioteca.adicionar_livro("O SENHOR DOS ANÉIS", "J.R.R. Tolkien")
biblioteca.adicionar_livro("O PEQUENO PRÍNCIPE", "Antoine de Saint-Exupéry")

while True:
    titulo_livro = input("Digite o nome do livro que deseja buscar: ").upper()
    livro_encontrado = biblioteca.buscar_livro(titulo_livro)

    if livro_encontrado:
        print(f"Livro encontrado: {livro_encontrado.titulo} - {livro_encontrado.autor}")
        break
    else:
        print("Livro não encontrado. Tente novamente.")




