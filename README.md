# Pipeline de Dados Climáticos

Este repositório contém um exemplo de um pipeline de dados climáticos utilizando a biblioteca Apache Airflow. O pipeline realiza a extração de informações climáticas através de uma classe `CimlaTempo`, cria uma pasta para armazenar os resultados e solicita informações climáticas através de uma tarefa Airflow.

## Pré-requisitos

Antes de executar o pipeline, você deve ter os seguintes pré-requisitos instalados:

- Python 3.9
- Apache Airflow

## Configuração do Ambiente Virtual (Linux Ubuntu)

Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto. Para criar e ativar um ambiente virtual no Linux Ubuntu com Python 3.9, siga os passos abaixo:

1. Abra o terminal.

2. Navegue até o diretório do projeto:

```bash
cd /caminho/do/seu/projeto
```

3. Execute o seguinte comando para criar um ambiente virtual:

```bash
python3.9 -m venv nome_do_ambiente
```

4. Ative o ambiente virtual:

```bash
source nome_do_ambiente/bin/activate
```

5. Com o ambiente virtual ativado, você pode instalar as dependências do projeto sem afetar o sistema global de pacotes.

6. Quando terminar de trabalhar no projeto, desative o ambiente virtual com o comando:

```bash
deactivate
```

## Instalação e Uso

1. Clone este repositório para o seu sistema local:

```bash
git clone https://github.com/SR-Dionizio/pipeline_dados_climaticos.git
```

2. Navegue até o diretório do projeto:

```bash
cd pipeline_dados_climaticos
```

3. Siga as instruções de configuração do ambiente virtual descritas acima.

4. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

5. Configure as informações de conexão e as configurações do seu ambiente Apache Airflow.

6. Execute o DAG `dados_climaticos`:

```bash
airflow dags trigger dados_climaticos
```

Isso iniciará o pipeline que extrai informações climáticas, cria uma pasta e solicita informações climáticas através do Airflow.

## Estrutura do Projeto

...


## Estrutura do Projeto

```
pipeline_dados_climaticos/
│
├── extrai_infos_clima.py
├── dags/
│   └── dados_climaticos.py
├── requirements.txt
└── README.md


- `extrai_infos_clima.py`: Contém a classe `CimlaTempo` que extrai informações climáticas.
- `dags/dados_climaticos.py`: Definição do DAG Airflow que configura o pipeline.
- `requirements.txt`: Lista de dependências do projeto.
- `README.md`: Este arquivo de documentação.
```

