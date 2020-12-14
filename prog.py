class Book:
   def __init__(self, titulo, isbn, valor, quantidade):
      self.titulo = titulo
      self.isbn = isbn
      self.valor = valor
      self.quantidade = quantidade

   def __repr__(self):
      return "\n## Livro ##\nISBN: %s\nTitle: %s\nPreço: %s\nQuantidade: %s" % (self.isbn, self.titulo, self.valor, self.quantidade)

#Definindo variáveis essenciais no programa
saldo = 0.00
EstoqueLivros = list()

#Abrindo o arquivo e lendo os dados
f = open("estoque.txt", "r")
read = f.readlines()
f.close()

saldoTxt = open("saldo.txt", "r")
saldo = float(saldoTxt.read())

#Percorrendo as linhas e criando um novo objeto para cada linha encontrada
for x in read:
   data = x.split(',')
   book = Book(str(data[0]), int(data[1]), float(data[2]), int(data[3]))
   EstoqueLivros.append(book)

def cadastraLivro(titulo, isbn, valor, quantidade):
   #Percorre a lista verificando se o isbn ja existe na lista
   for x in EstoqueLivros:
      #Se for encontrado apenas incrementa a quantidade do livro
      if x.isbn == int(isbn):
         print("Livro já existe no estoque! Aumentando sua quantidade...")
         x.quantidade += int(quantidade)
         break
   else:
      #Se o livro nao for encontrado, insere um novo item
      book = Book(str(titulo), int(isbn), float(valor), int(quantidade))
      EstoqueLivros.append(book)

      print("\nLivro cadastrado com sucesso!")

def consultaEstoqueTitulo(titulo):
   #Percorre a lista de livros procurando pelo titulo passado
   found = next((x for x in EstoqueLivros if str(x.titulo) == str(titulo)), "\nLivro não encontrado!")

   print(found)

def consultaEstoqueISBN(isbn):
   #Percorre a lista de livros procurando pelo isbn passado
   found = next((x for x in EstoqueLivros if int(x.isbn) == int(isbn)), "\nLivro não encontrado!")

   print(found)

def venderLivro(isbn, quantidade, saldo):
   #Percorre a lista verificando se o isbn existe na lista
   for x in EstoqueLivros:
      if x.isbn == int(isbn):
         #Se existir ele verifica se a quantidade passada é maior
         #do que a quantidade no estoque
         if x.quantidade - int(quantidade) < 0:
            print("Não há estoque suficiente para a quantidade solicitada")
         else:
            #Se tiver estoque disponivel, decrementa o estoque
            #e incrementa o saldo da loja
            x.quantidade -= int(quantidade)
            saldo += int(quantidade) * x.valor
         break
   else:
      print("\nO livro solicitado não está no estoque")
   
   return saldo

def consultaSaldo():
   print("Saldo da Loja: %.2f" % saldo)

def salvarDados():
   #Abre o arquivo saldo.txt e insere o novo valor
   saldoTxt = open("saldo.txt", "w")
   saldoTxt.write(str(saldo))

   #Abre o arquivo estoque.txt e insere os livros instanciados no programa
   estoque = open("estoque.txt", "w")

   for x in EstoqueLivros:
      #Muda o formato do ohttps://www.youtube.com/watch?v=Ri-eF5PJ2X0bjeto da classe Book para inserir no arquivo.txt
      #Formato do livro no arquivo "titulo, isbn, preço, quantidade"
      data = x.titulo + ", " + str(x.isbn) + ", " + str(x.valor) + ", " + str(x.quantidade) + "\n"
      estoque.write(data)

   estoque.close()

   print("Dados salvos com sucesso!")


option=True
while option:
   print ("""
   1. Cadastrar Livro
   2. Consulta Estoque (Busca por Título)
   3. Consulta Estoque (Busca por ISBN)
   4. Vender um Livro
   5. Consultar Saldo da Loja
   6. Salvar Dados
   9. Sair
   """)

   option = input("Selecione uma opção: ") 
   if option=="1": 
      print("\n## Cadastra Livro ##")
      isbn = input("Digite o ISBN do livro: ")
      titulo = input("Digite o Titulo do livro: ")
      valor = input("Digite o Valor do livro: ")
      quantidade = input("Digite a Quantidade do livro: ")

      cadastraLivro(titulo, isbn, valor, quantidade)

   elif option=="2":
      print("\n## Consultar Estoque por Titulo ##")
      titulo = input("Digite o título do livro: ")
      consultaEstoqueTitulo(titulo)

   elif option=="3":
      print("\n## Consultar Estoque por ISBN ##")
      isbn = input("Digite o ISBN do livro: ")
      consultaEstoqueISBN(isbn) 

   elif option=="4":
      print("\n## Vender Livro ##")
      isbn = input("Digite o ISBN do livro: ")
      quantidade = input("Digite a Quantidade do livro: ")
      saldo = venderLivro(isbn, quantidade, saldo)

   elif option=="5":
      print("\n## Consulta Saldo ##")
      consultaSaldo()

   elif option=="6":
      print("\n## Salvando Dados ##")
      salvarDados()

   elif option=="9":
      print("\nFechando o programa...")
      exit()  
   else:
      print("\nOpção inválida") 

