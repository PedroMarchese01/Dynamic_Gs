# Dynamic_GS

## Global Solution — CitizenTech

**Distribuição inteligente de energia para comunidades ribeirinhas utilizando grafos.**

## Integrantes

| Nome | RM |
|---|---:|
| Augusto Valerio | 562185 |
| Pedro Marchese | 563339 |
| Mariana Oliveira | 564241 |
| Jonas Esteves | 564143 |
| Vitor Tigre | 561746 |

## Ficha da CitizenTech

| Campo | Definição |
|---|---|
| **Nome da CitizenTech** | Estação Ribeirinha — Distribuição Inteligente de Energia |
| **Cidade e bairro / território** | Comunidades ribeirinhas da Amazônia, representadas na simulação por uma rede de residências conectadas. |
| **Cidadãos beneficiados** | Moradores de comunidades ribeirinhas, lideranças comunitárias e responsáveis pelo planejamento da infraestrutura energética local. |
| **Problema** | A geração e o armazenamento de energia podem ser limitados, tornando necessário estudar como distribuir a energia disponível para atender o maior número possível de residências. |
| **Como funciona** | As residências e conexões da comunidade são representadas por um grafo. O sistema simula geração solar, armazenamento em baterias, demanda energética e distribuição por caminhos que ainda possuem capacidade disponível. |
| **O que cada parte faz** | Os modelos representam baterias, residências e o painel solar; a fábrica constrói a comunidade e o grafo; o serviço de distribuição seleciona os caminhos e administra a energia; a visualização apresenta o atendimento em tempo real. |
| **Indicadores de impacto** | Quantidade de residências atendidas, energia distribuída, energia restante nas baterias, conexões utilizadas e continuidade do atendimento durante o período simulado. |
| **ODS relacionados** | ODS 7 — Energia Acessível e Limpa; ODS 10 — Redução das Desigualdades; ODS 11 — Cidades e Comunidades Sustentáveis; ODS 13 — Ação Contra a Mudança Global do Clima. |
| **Repositório** | [github.com/PedroMarchese01/Dynamic_Gs](https://github.com/PedroMarchese01/Dynamic_Gs) |

> O projeto é uma simulação acadêmica com dados e parâmetros demonstrativos. Os resultados não substituem estudos de engenharia elétrica nem devem ser utilizados diretamente para controlar uma rede real.

---

## Sobre o projeto

O Dynamic_GS surgiu de uma preocupação com a realidade de comunidades ribeirinhas da Amazônia, onde o acesso à energia elétrica ainda pode ser limitado e manter um fornecimento constante é um grande desafio.

A nossa proposta é explorar como a tecnologia pode ajudar nesse cenário, criando uma simulação de uma comunidade que utiliza energia solar e baterias para abastecer suas residências.

Mas o foco do projeto vai além de gerar e armazenar energia. O nosso principal desafio é encontrar uma maneira de distribuir a energia disponível para o maior número possível de casas.

Para isso, utilizamos a teoria dos grafos para representar a comunidade como uma rede de distribuição. Cada residência é representada por um vértice, enquanto as conexões representam os caminhos pelos quais a energia pode chegar até ela.

Com essa estrutura, conseguimos trabalhar com diferentes situações de consumo, geração, armazenamento e limitações da rede, acompanhando em tempo real quais residências estão recebendo energia.

## Nosso objetivo

Imagine uma comunidade com 30 residências e uma quantidade limitada de energia armazenada. Como decidir quais casas receberão energia? Como aproveitar melhor as conexões existentes? E como evitar que parte da comunidade fique sem atendimento?

Essas são algumas das questões que buscamos trabalhar no Dynamic_GS.

Nosso principal objetivo é **distribuir a energia disponível de forma inteligente, buscando atender ao maior número possível de residências**.

Para isso, consideramos:

- a demanda energética individual de cada casa;
- a quantidade de energia disponível nas baterias;
- os caminhos existentes entre a fonte e as residências;
- a capacidade de transmissão de cada conexão;
- a quantidade de residências que conseguem receber energia;
- as mudanças no consumo e na geração durante a simulação.

A ideia é entender como diferentes configurações da rede e estratégias de distribuição podem melhorar o atendimento da comunidade, principalmente durante períodos sem geração solar.

---

## Como funciona o projeto

O funcionamento pode ser dividido em quatro etapas:

1. **Geração:** o painel solar produz energia de acordo com a luminosidade e o tempo de funcionamento.
2. **Armazenamento:** a energia gerada é enviada para o banco de baterias.
3. **Distribuição:** o sistema analisa o grafo, verifica os caminhos disponíveis e distribui a energia conforme a demanda das residências.
4. **Visualização:** o grafo é atualizado para mostrar quais casas receberam energia e como a distribuição está acontecendo.

Essas etapas trabalham em conjunto. Enquanto o painel produz energia, as residências continuam consumindo, e o sistema precisa administrar o que está disponível.

## Técnica escolhida

A técnica escolhida para a Global Solution foi a utilização de **grafos**.

O grafo representa a infraestrutura de distribuição da comunidade:

- as residências são representadas por vértices;
- a fonte de energia é representada pelo vértice `ENERGY_SOURCE`;
- as conexões elétricas são representadas por arestas;
- cada aresta possui uma capacidade de transmissão;
- os caminhos indicam como a energia pode chegar até cada residência.

Além do grafo, o projeto utiliza uma estratégia gulosa de priorização. Antes da distribuição, as residências são ordenadas pela demanda energética, da menor para a maior.

Essa estratégia busca atender primeiro as casas que precisam de menos energia, aumentando a possibilidade de atender uma quantidade maior de residências quando a energia disponível é limitada.

A estratégia não garante uma solução globalmente ótima para todas as configurações possíveis de rede, mas oferece uma abordagem coerente e eficiente para a simulação proposta.

## A importância dos grafos

O grafo é a parte central do Dynamic_GS. É por meio dele que representamos a infraestrutura da comunidade e analisamos como a energia pode chegar até cada residência.

Utilizamos a biblioteca NetworkX para criar e manipular essa estrutura.

### Vértices

Os vértices representam os pontos da rede.

No nosso projeto, temos:

- um vértice especial chamado `ENERGY_SOURCE`, que representa a fonte de energia;
- os vértices das residências, que representam as casas da comunidade.

Cada residência também possui informações próprias, como sua demanda energética e a quantidade de energia recebida.

### Arestas

As arestas representam as conexões entre os pontos da rede.

Elas determinam como as residências estão interligadas e quais caminhos podem ser utilizados para transportar energia.

Cada conexão possui uma capacidade de transmissão, que limita a quantidade de energia que consegue passar por ela em cada intervalo da simulação.

### Caminhos

Para que uma residência receba energia, precisa existir um caminho entre a fonte e o seu vértice.

O sistema utiliza `networkx.shortest_path()` para procurar um caminho entre a fonte e cada residência.

Antes da busca, o sistema cria um grafo residual contendo somente as conexões que ainda possuem capacidade suficiente para transportar a demanda da residência analisada.

Uma residência pode ter demanda e ainda assim não receber energia caso:

- não exista um caminho disponível;
- alguma conexão não possua capacidade suficiente;
- o banco de baterias não possua energia suficiente.

### Capacidade das conexões

Cada aresta possui uma capacidade de transmissão expressa em watts (W).

Como a demanda das residências é calculada em watt-hora (Wh), o sistema converte a capacidade da conexão de acordo com o intervalo de tempo:

```python
capacity_wh = capacity_w * interval_seconds / 3600
```

Por exemplo, uma conexão com capacidade de 1000 W consegue transmitir aproximadamente `0,277 Wh` em um intervalo de um segundo.

Isso permite comparar a capacidade de transmissão da conexão com a demanda energética de cada residência no mesmo intervalo.

## Noção de eficiência

Considere:

- `V`: quantidade de vértices;
- `E`: quantidade de arestas;
- `H`: quantidade de residências.

A ordenação das residências pela demanda possui complexidade aproximada de:

```text
O(H log H)
```

Para cada residência, o algoritmo reconstrói o grafo residual e procura um caminho utilizando a busca de menor caminho do NetworkX.

Como o grafo não possui pesos, essa busca pode ser realizada de maneira equivalente a uma busca em largura, com complexidade aproximada de:

```text
O(V + E)
```

Como a operação é repetida para as residências, a complexidade aproximada de uma rodada de distribuição é:

```text
O(H × (V + E) + H log H)
```

A memória utilizada pelo grafo e pelas estruturas auxiliares é aproximadamente:

```text
O(V + E)
```

Para o cenário padrão de 30 residências, essa abordagem é suficiente para permitir a atualização da distribuição e da visualização durante a execução.

---

## Estrutura do projeto

```text
Dynamic_Gs/
│
├── src/
│   │
│   ├── main.py
│   │
│   ├── models/
│   │   ├── battery.py
│   │   ├── battery_bank.py
│   │   ├── homes.py
│   │   └── solar_panel.py
│   │
│   ├── factory/
│   │   ├── graph_village_factory.py
│   │   └── village_factory.py
│   │
│   └── service/
│       ├── energy_distribution.py
│       └── live_village_view.py
│
├── requirements.txt
└── README.md
```

## Classes e funções

O projeto foi separado em classes para que cada parte tenha uma responsabilidade específica. Assim, a geração de energia não precisa conhecer os detalhes do grafo, e a visualização não precisa executar os cálculos de distribuição.

### 1. Models

As classes de `models` representam os elementos que fazem parte da simulação.

#### Battery — `battery.py`

Representa uma bateria individual.

É responsável por controlar a quantidade de energia armazenada e impedir que a bateria ultrapasse sua capacidade ou tente fornecer uma quantidade maior do que possui.

Principais funções:

| Método | O que faz |
|---|---|
| `charge(amount)` | Adiciona energia à bateria, respeitando sua capacidade. |
| `discharge(amount)` | Retira energia armazenada. |
| `get_energy()` | Retorna a energia atualmente armazenada. |
| `get_capacity()` | Retorna a capacidade máxima da bateria. |

Essa classe é utilizada pelo banco de baterias, que reúne várias instâncias de `Battery`.

#### BatteryBank — `battery_bank.py`

Representa o conjunto de baterias utilizado para armazenar a energia da comunidade.

Em vez de controlar cada bateria separadamente nos outros componentes, centralizamos esse gerenciamento em uma única classe.

Principais funções:

| Método | O que faz |
|---|---|
| `append_battery(battery_amount)` | Adiciona a quantidade solicitada de baterias ao banco. |
| `charge(amount)` | Distribui a energia recebida entre as baterias que ainda possuem espaço. |
| `discharge(amount)` | Retira uma quantidade de energia do banco, respeitando o total disponível. |
| `get_total_energy()` | Retorna a soma da energia armazenada em todas as baterias. |
| `get_total_capacity()` | Retorna a capacidade máxima somada de todas as baterias. |
| `get_batteries_level()` | Calcula o percentual geral de carga do banco. |
| `get_available_energy()` | Retorna a quantidade de energia disponível para distribuição. |

A classe utiliza `threading.RLock()` para proteger operações de leitura e alteração do armazenamento. Isso evita conflitos quando a thread responsável pela geração solar e a execução principal acessam o banco de baterias simultaneamente.

**Exemplo de utilização:**

```python
from src.models.battery_bank import BatteryBank

battery_bank = BatteryBank()

# Adiciona 10 baterias de 50 Wh
battery_bank.append_battery(10)

# Armazena 300 Wh
battery_bank.charge(300)

# Consulta a energia disponível
print(battery_bank.get_available_energy())

# Consulta o percentual de carga
print(battery_bank.get_batteries_level())
```

#### Home — `homes.py`

Representa cada residência da comunidade.

Cada casa possui uma demanda energética própria, que pode variar durante a simulação.

Principais funções:

| Método | O que faz |
|---|---|
| `get_energy_demand(interval_seconds)` | Calcula a demanda de energia da residência para determinado intervalo. |
| `set_energy_received(amount)` | Registra a quantidade de energia recebida pela residência. |
| `set_electricity_consumption(consumption)` | Define o consumo-base da residência. |
| `update_consumption()` | Aplica uma variação ao consumo da residência. |

Além desses métodos, os atributos da residência são utilizados para acompanhar informações como consumo, energia recebida e situação de atendimento.

Essa separação permite que cada casa tenha seu próprio comportamento, em vez de todas compartilharem uma demanda fixa.

#### SolarPanel — `solar_panel.py`

Representa o painel responsável pela geração de energia solar.

O painel calcula a energia produzida considerando sua potência, o percentual de luminosidade, sua eficiência e o tempo de funcionamento.

A energia gerada é enviada diretamente ao banco de baterias.

Principais configurações:

| Atributo | O que representa |
|---|---|
| `MAX_POWER` | Potência máxima do painel, em watts. |
| `EFFICIENCY` | Eficiência considerada na geração. |
| `light` | Percentual de luminosidade disponível. |
| `energy_target` | Banco de baterias que recebe a energia gerada. |
| `running` | Indica se o processo de geração está ativo. |
| `thread` | Referência à thread de geração. |

Principais funções:

| Método | O que faz |
|---|---|
| `turn_on()` | Inicia o processo de geração solar em uma thread. |
| `turn_off()` | Interrompe o processo de geração. |
| `capture_sun_light()` | Calcula a energia produzida e envia o resultado ao banco de baterias. |

A utilização de uma thread permite que o painel continue gerando energia enquanto o restante da simulação executa a distribuição e atualiza o grafo.

### 2. Factory

#### VillageFactory — `village_factory.py`

Responsável por construir a comunidade que será utilizada na simulação.

Essa classe reúne as residências e organiza a estrutura de conexões utilizada pelo sistema de distribuição.

Principais funções:

| Método | O que faz |
|---|---|
| `append_home(home)` | Adiciona uma residência à comunidade. |
| `append_number_of_home(number_of_home)` | Cria a quantidade solicitada de residências. |
| `generate_graph()` | Gera o grafo que representa a comunidade e suas conexões. |
| `get_homes()` | Retorna as residências criadas. |
| `update_consumptions()` | Atualiza os consumos das residências durante a simulação. |

A quantidade de residências e a organização das conexões influenciam diretamente os resultados.

O arquivo `graph_village_factory.py` cria uma estrutura inicialmente conectada e adiciona outras conexões aleatórias entre as residências.

### 3. Services

Os serviços concentram as principais regras de funcionamento do projeto.

#### EnergyDistribution — `energy_distribution.py`

Essa é uma das classes mais importantes do projeto, pois é responsável por decidir como a energia disponível será distribuída pela rede.

Ela recebe o banco de baterias e a comunidade, acessa o grafo e analisa as demandas de cada residência.

O processo de distribuição considera tanto a energia armazenada quanto os caminhos disponíveis na rede.

##### `__init__()`

Inicializa o serviço de distribuição:

- recebe o banco de baterias e a comunidade;
- obtém o grafo da comunidade;
- define a capacidade padrão das conexões;
- cria o vértice especial `ENERGY_SOURCE`;
- conecta a fonte à primeira residência;
- configura a capacidade das conexões.

##### `distribute(interval_seconds=1)`

Executa uma rodada de distribuição.

O processo acontece da seguinte maneira:

1. Obtém todas as residências da comunidade.
2. Consulta a demanda energética de cada casa.
3. Verifica a energia disponível no banco de baterias.
4. Calcula a capacidade de transmissão das conexões para o intervalo analisado.
5. Organiza as residências da menor para a maior demanda.
6. Cria um grafo residual com as conexões disponíveis.
7. Procura um caminho entre a fonte e cada residência.
8. Verifica se existe energia e capacidade suficientes.
9. Atualiza a energia recebida por cada casa.
10. Desconta do banco a energia distribuída.
11. Retorna as informações da rodada.

A estratégia utilizada é de atendimento completo: uma residência recebe toda a sua demanda no intervalo ou permanece sem atendimento naquela rodada.

##### Busca de caminhos

O projeto utiliza `networkx.shortest_path()` para procurar um caminho entre a fonte de energia e cada residência.

Antes da busca, é construída uma estrutura auxiliar com as conexões que ainda possuem capacidade suficiente para atender à demanda analisada.

Dessa forma, o algoritmo não considera apenas a quantidade de arestas do caminho, mas também a capacidade disponível nas conexões.

##### Informações retornadas

| Informação | Significado |
|---|---|
| `attended` | Quantidade de residências atendidas. |
| `total_homes` | Total de residências da comunidade. |
| `energy_delivered` | Energia total distribuída na rodada. |
| `energy_remaining` | Energia restante no banco. |
| `active_edges` | Conexões utilizadas na distribuição. |
| `paths` | Caminhos utilizados para atender às residências. |

#### LiveVillageView — `live_village_view.py`

Responsável por apresentar visualmente o que está acontecendo na comunidade.

Utiliza NetworkX para desenhar a estrutura do grafo e Matplotlib para atualizar a visualização durante a simulação.

A classe recebe o grafo, as residências e a identificação da fonte de energia.

Principais responsabilidades:

- desenhar os vértices e as arestas;
- identificar visualmente a fonte de energia;
- diferenciar residências atendidas e não atendidas;
- destacar as conexões utilizadas;
- atualizar as informações exibidas durante a execução;
- apresentar dados gerais sobre o atendimento da comunidade.

As cores dos vértices ajudam a identificar a situação da rede:

- **azul:** fonte de energia;
- **verde:** residência atendida;
- **vermelho:** residência sem energia.

A visualização é atualizada sem precisar reconstruir todo o grafo a cada rodada, mantendo as posições dos vértices e alterando as informações visuais conforme os resultados da distribuição.

### 4. Arquivo principal — `main.py`

O arquivo `main.py` é responsável por conectar todas as partes do projeto.

É nele que os componentes são criados, configurados e executados.

Suas responsabilidades incluem:

- criar o banco de baterias;
- definir a quantidade de residências;
- construir a comunidade;
- gerar o grafo;
- inicializar o painel solar;
- criar o serviço de distribuição;
- inicializar a visualização gráfica;
- controlar o modo de simulação;
- atualizar a distribuição e a visualização;
- controlar o tempo real e o tempo simulado;
- encerrar os processos quando a simulação termina.

O `main.py` não concentra os cálculos de geração, armazenamento ou distribuição. Ele coordena as classes responsáveis por cada atividade.

---

## Funcionalidades da simulação

### Geração solar e consumo simultâneos

No modo normal, o painel solar permanece ativo e produz energia de acordo com as condições de luminosidade.

Enquanto isso, as residências continuam consumindo energia, e o serviço de distribuição administra o fornecimento conforme a disponibilidade do banco de baterias.

O cálculo utiliza o tempo realmente transcorrido entre duas rodadas de distribuição, evitando que o consumo dependa da velocidade do computador.

### Simulação noturna

A simulação noturna representa um período em que não existe geração solar.

Nesse cenário, o fornecimento depende exclusivamente da energia armazenada anteriormente nas baterias.

O modo representa 12 horas simuladas em aproximadamente 120 segundos reais.

O intervalo de consumo é calculado de acordo com o tempo transcorrido e com a escala da simulação:

```python
NIGHT_TIME_SCALE = (
    NIGHT_HOURS * 3600 / NIGHT_DURATION_SECONDS
)
```

Dessa forma, a quantidade de iterações executadas não altera a duração simulada.

### Distribuição baseada em grafos

A energia não é simplesmente dividida entre as casas.

O algoritmo considera:

- os caminhos disponíveis;
- a capacidade restante das conexões;
- a demanda de cada residência;
- a energia disponível no banco.

Isso permite testar diferentes organizações da rede e observar como a conectividade influencia o resultado.

### Acompanhamento em tempo real

Durante a execução, o Matplotlib apresenta a rede e atualiza as informações de atendimento.

É possível acompanhar:

- quantas casas estão sendo atendidas;
- quantas residências estão sem energia;
- quais conexões estão sendo utilizadas;
- quanto de energia foi distribuído;
- quanto ainda está armazenado nas baterias;
- o tempo decorrido da simulação.

---

## Como modificar a simulação

As configurações principais ficam no arquivo `src/main.py`.

| Configuração | O que modifica |
|---|---|
| `NUMBER_OF_BATTERIES` | Quantidade de baterias utilizadas. |
| `NUMBER_OF_HOMES` | Quantidade de residências da comunidade. |
| `EDGE_CAPACITY_W` | Capacidade padrão de transmissão das conexões. |
| `NIGHT_HOURS` | Duração do período noturno simulado. |
| `NIGHT_DURATION_SECONDS` | Tempo real utilizado para executar a simulação noturna. |
| `NIGHT_TIME_SCALE` | Relação entre segundos reais e segundos simulados. |

### Alterando a quantidade de baterias

```python
battery_bank.append_battery(10)
```

Cada bateria possui capacidade de 50 Wh.

Nesse exemplo, o banco possui capacidade total de 500 Wh.

### Alterando a quantidade de residências

A quantidade de casas é definida pela constante:

```python
NUMBER_OF_HOMES = 30
```

Alterar esse valor permite observar como o algoritmo se comporta com comunidades de tamanhos diferentes.

### Alterando a capacidade das conexões

```python
EDGE_CAPACITY_W = 1000
```

Esse valor define a capacidade padrão das conexões que ainda não possuem uma capacidade específica.

Reduzir esse limite permite simular uma infraestrutura com maior restrição de transmissão.

Aumentá-lo permite analisar como uma rede com conexões de maior capacidade se comporta.

---

## Instalação e execução

### Requisitos

- Python 3.10 ou superior;
- pip;
- Git.

As dependências Python estão declaradas no arquivo `requirements.txt`:

```text
networkx==3.7
matplotlib==3.11.2
```

### Clonando o repositório

```bash
git clone https://github.com/PedroMarchese01/Dynamic_Gs.git
```

Entre na pasta:

```bash
cd Dynamic_Gs
```

### Criando o ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```powershell
.venv\Scripts\activate
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

### Instalando as dependências

```bash
python -m pip install -r requirements.txt
```

### Executando

Na raiz do projeto:

```bash
python -m src.main
```

O arquivo principal apresentará duas opções:

```text
1 - Simulação normal
2 - Simular uma noite (12 horas)
```

No PyCharm, caso o gráfico seja aberto somente na ferramenta **Plots** e a execução seja encerrada imediatamente, desative a opção **Show plots in tool window** nas configurações de gráficos do Python. Assim, o Matplotlib utilizará uma janela interativa separada.

---

## Tecnologias utilizadas

| Tecnologia | Aplicação no projeto |
|---|---|
| Python | Desenvolvimento da lógica e dos modelos. |
| NetworkX | Criação, manipulação e busca de caminhos nos grafos. |
| Matplotlib | Visualização e atualização gráfica da rede. |
| Threading | Execução simultânea da geração solar. |
| Git | Controle de versão do projeto. |

## CitizenTech e impacto social

Escolhemos trabalhar com a realidade das comunidades ribeirinhas porque o acesso à energia influencia diretamente o dia a dia das famílias.

A eletricidade permite estudar durante a noite, conservar alimentos, utilizar equipamentos, manter a comunicação e realizar diversas atividades que dependem de um fornecimento confiável.

Pensando nisso, queremos explorar como uma rede de distribuição bem organizada pode aproveitar melhor a energia disponível.

O Dynamic_GS utiliza a computação para estudar esse problema, simulando uma comunidade, suas conexões e suas necessidades energéticas.

A intenção é buscar estratégias que ajudem a levar energia ao maior número possível de residências, considerando que os recursos e a infraestrutura podem ser limitados.

## Considerações finais

O Dynamic_GS é uma forma de trabalhar um problema relacionado à CitizenTech por meio da programação e da teoria dos grafos.

Ao representar as residências como vértices e as conexões como arestas, conseguimos estudar como a organização da rede interfere na distribuição de energia.

Nosso foco é entender como aproveitar melhor os recursos disponíveis e encontrar maneiras de atender mais casas, principalmente em comunidades ribeirinhas que enfrentam dificuldades de acesso à eletricidade.

O projeto demonstra:

- utilização de grafos;
- busca de caminhos;
- controle de capacidade residual;
- estratégia gulosa de priorização;
- análise de eficiência;
- geração e armazenamento de energia;
- simulação temporal;
- visualização em tempo real.

---

**FIAP — Global Solution | CitizenTech**

**Dynamic_GS**
