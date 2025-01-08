# Biblioteca Virtual - Sistema de Empréstimos

Este projeto é uma aplicação de biblioteca virtual implementada em Python, utilizando conceitos de Orientação a Objetos (OO), serialização de objetos, e interfaces gráficas com a biblioteca `tkinter`.

## Critérios Aplicados

### 1. **Orientação a Objetos** (OO):
A aplicação utiliza a **orientação a objetos** para organizar e modelar o sistema de biblioteca. Os principais conceitos de OO foram aplicados, como:

#### **Herança**:
- As classes `UsuarioComum` e `UsuarioPremium` herdam de uma classe base `Usuario`. Ambas as subclasses modificam o comportamento de `calcular_dias_emprestimo`, com a diferença de que usuários premium têm mais dias para devolver os livros.

#### **Polimorfismo**:
- O método `calcular_dias_emprestimo` é polimórfico, pois é implementado de forma diferente para usuários comuns e premium. Dependendo do tipo de usuário, o número de dias de empréstimo varia.

#### **Encapsulamento (total)**:
- O encapsulamento é totalmente aplicado nas classes, com atributos privados (ex: `self.__titulo`, `self.__autor`) e o uso de métodos getter/setter quando necessário. A interação com os dados dos objetos é feita por meio de métodos públicos, como `to_dict()` e `from_dict()`.

### 2. **Serialização de Objetos**:
- Os objetos da biblioteca (`Livro` e `Usuario`) são **serializados** e **desserializados** para o formato JSON, permitindo que os dados sejam salvos em um arquivo (`biblioteca.json`) e carregados novamente quando a aplicação for iniciada. 
- O método `to_dict()` é usado para converter os objetos em dicionários, enquanto `from_dict()` reconstrói os objetos a partir dos dados lidos do arquivo.

### 3. **Interface Gráfica**:
- A aplicação utiliza a biblioteca `tkinter` para criar uma interface gráfica (GUI) que permite a interação do usuário com o sistema de biblioteca. 
- A interface oferece opções para adicionar/remover livros e usuários, realizar empréstimos, listar livros/usuários, e salvar os dados em um arquivo.
- A interface foi projetada para ser fácil de usar e maximizada na tela, com botões para cada ação importante e feedback ao usuário via caixas de mensagem.

## Estrutura do Código

### Classes Principais

1. **Livro**:
   - Representa um livro da biblioteca.
   - Métodos importantes: `emprestar()`, `devolver()`, `to_dict()`, `from_dict()`.
   
2. **Usuario**:
   - Representa um usuário da biblioteca (comum ou premium).
   - Métodos importantes: `calcular_dias_emprestimo()`, `to_dict()`, `from_dict()`.
   
3. **UsuarioComum** e **UsuarioPremium**:
   - Subclasses de `Usuario` que definem regras diferentes de empréstimo (usuários comuns têm 14 dias e usuários premium têm 30 dias).

4. **Emprestimo**:
   - Representa o empréstimo de um livro a um usuário.
   - Métodos importantes: `finalizar()`.

5. **Biblioteca**:
   - Gerencia livros, usuários e empréstimos.
   - Métodos importantes: `adicionar_livro()`, `adicionar_usuario()`, `remover_livro()`, `remover_usuario()`, `realizar_emprestimo()`, `carregar_dados()`, `salvar_dados()`.

6. **BibliotecaApp**:
   - Interface gráfica que utiliza `tkinter` para interação com o usuário.
   - Métodos importantes: `adicionar_livro()`, `adicionar_usuario()`, `remover_livro()`, `remover_usuario()`, `realizar_emprestimo()`, `listar_livros()`, `listar_usuarios()`.

### Fluxo Principal

1. **Carregar Dados**:
   - Ao iniciar o aplicativo, os dados de livros e usuários são carregados de um arquivo JSON, se disponível.
   
2. **Interação com o Usuário**:
   - A interface gráfica permite ao usuário adicionar ou remover livros e usuários, realizar empréstimos, e listar os itens da biblioteca.
   
3. **Salvar Dados**:
   - Após as alterações, os dados são salvos de volta no arquivo JSON para persistência.

## Como Rodar o Código

1. Certifique-se de ter o Python 3 instalado em sua máquina.
2. Instale a biblioteca `tkinter` se necessário.
3. Clone ou baixe o código-fonte.
4. Execute o arquivo Python:
   
   ```bash
   python biblioteca_virtual.py
5. A interface gráfica será aberta, e você poderá começar a usar o sistema de biblioteca.

## Exemplo de Uso

1. Adicione livros e usuários.
2. Realize um empréstimo selecionando um livro e um usuário.
3. Visualize a lista de livros e usuários na interface.
4. Salve os dados para garantir que as informações sejam persistidas.

## Conclusão

Este sistema implementa os conceitos fundamentais de Orientação a Objetos, oferecendo uma maneira eficiente de gerenciar uma biblioteca com funcionalidades de empréstimos e armazenamento persistente de dados.