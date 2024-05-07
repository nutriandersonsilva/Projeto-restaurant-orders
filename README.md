# Restaurant Orders

Este projeto da Chapa Quente é uma ferramenta de construção de cardápios para facilitar a gestão de receitas e estoque do restaurante. A aplicação permite gerar cardápios considerando restrições alimentares e disponibilidade de ingredientes em estoque.

## Descrição

O projeto já possui uma estrutura inicial e sua missão é finalizar a construção, implementando testes para classes já existentes e criando novas classes para mapear pratos, gerar cardápios e gerenciar estoque de ingredientes.

## Habilidades Exercitadas

- Prática com Hashmaps utilizando as estruturas de dados Dict e Set do Python
- Conhecimentos em testes de software
- Orientação a objetos

## Requisitos Obrigatórios

### Testando classes já implementadas parte 1

Implemente testes para a classe Ingredient, que se encontra em src/models/ingredient.py. Os testes devem garantir que a classe pode ser instanciada corretamente, que o atributo de restrições alimentares é populado conforme esperado, e que os métodos mágicos __repr__, __eq__ e __hash__ funcionam como esperado.

### Testando classes já implementadas parte 2

Implemente testes para a classe Dish, localizada em src/models/dish.py. Os testes devem garantir que a classe pode ser instanciada corretamente, que os métodos da classe funcionam como esperado, que o dicionário de receita do prato retorna a quantidade correta de um ingrediente, e que erros são levantados ao criar pratos inválidos.

### Mapeamento Pratos <> Ingredientes

Implemente a classe MenuData em src/services/menu_data.py para mapear pratos e ingredientes baseados em um arquivo CSV. A classe deve ler o arquivo CSV, instanciar pratos e ingredientes conforme necessário, e conter um atributo dishes que lista todos os pratos do cardápio.

### Geração dos Cardápios

Implemente o método get_main_menu na classe MenuBuilder em src/services/menu_builder.py para gerar os cardápios. O método deve considerar restrições alimentares e disponibilidade em estoque dos ingredientes.

## Como Executar o Projeto

1. Clone este repositório
2. Navegue até a pasta do projeto e execute `pip install -r requirements.txt` para instalar as dependências
3. Execute os testes com `pytest` para garantir a correta implementação das classes existentes
4. Implemente as classes e métodos requeridos conforme descrito nos requisitos obrigatórios
5. Execute os testes novamente para verificar a implementação das novas funcionalidades

## Estrutura do Projeto

- `src/`: Pasta contendo o código-fonte da aplicação
  - `models/`: Classes para modelos de dados
  - `services/`: Lógica de negócio e serviços
  - `tests/`: Testes para as classes e funcionalidades implementadas

## Recursos Adicionais (Requisitos Bônus)

- Estoque de Ingredientes: Implemente a classe InventoryMapping em src/services/inventory_control.py para controle de estoque de ingredientes
- Cardápios baseados no Estoque: Complemente o método get_main_menu na classe MenuBuilder para considerar a disponibilidade em estoque dos ingredientes dos pratos

