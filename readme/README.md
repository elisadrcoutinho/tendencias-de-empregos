# Projeto: Análise de Dados do LinkedIn - Abril 2024

## Introdução
Este projeto foi desenvolvido para analisar dados de postings de empregos no LinkedIn nos Estados Unidos, referentes a um único dia. Nosso objetivo foi explorar informações como tipos de contrato, formatos de trabalho (remoto ou presencial), localização geográfica e muito mais. Através de uma análise de dados detalhada e visualizações gráficas claras, buscamos extrair insights relevantes. Além disso, desenvolvemos um website interativo para apresentar os resultados de maneira acessível.

---

## Estrutura do Projeto

### Arquivos Principais:
- **`Analise_Linkedin_2024.ipynb`**: Contém o código usado para a análise exploratória de dados e geração dos gráficos.
- **`app.py`**: Arquivo principal para rodar o servidor Flask que alimenta o website.
- **`requirements_jupyter.txt`**: Lista de dependências necessárias para executar o projeto no Jupyter.
- **`requirements_python.txt`**: Lista de dependências necessárias para executar o projeto do website.
- **`static/`**: Diretório com arquivos estáticos (CSS, ícones, imagens e gráficos).
- **`templates/`**: Diretório com os arquivos HTML usados no website.
- **`job_posting_linkedin_2024.csv`**: Base de dados utilizada para a análise.

### Website:
- Desenvolvido com Flask, o website inclui:
  - **Home Page**: Introdução ao projeto.
  - **Seções Específicas**: Apresentação dos insights e gráficos com descrições detalhadas.
  - **Download de Dados**: Opção para baixar o arquivo de dados original.

---

## Requisitos do Sistema

- **Python**: Versão 3.8 ou superior.
- **Bibliotecas Necessárias**:
  - Flask
  - pandas
  - numpy
  - seaborne	
  - matplotlib	.pyplot
  - os

---

## Como Executar o Projeto

### Para Executar o Website:
1. Clone este repositório para sua máquina:
   ```bash
   git clone https://github.com/elisadrcoutinho/tendencias-de-empregos.git
   cd tendencias-de-empregos
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements_python.txt
   ```

3. Execute o website:
   ```bash
   python app.py
   ```

4. Acesse o website no navegador em: [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Para Executar a Análise de Dados:
1. Instale as dependências necessárias:
   ```bash
   pip install -r requirements_jupyter.txt
   ```

2. Abra o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. No navegador, abra o arquivo `Analise_Linkedin_2024.ipynb`.

4. Execute as células do notebook para realizar a análise e visualizar os gráficos gerados.

---

## Funcionalidades do Projeto

- **Análise Exploratória**: Explora padrões e insights relevantes nos dados de empregos.
- **Visualizações Gráficas**: Gráficos de fácil interpretação criados com Matplotlib.
- **Interatividade**: Apresentação dos resultados em um website responsivo e intuitivo.
- **Download de Dados**: Permite aos usuários baixar o dataset original para análises futuras.

---

## Estrutura do Website

### Páginas Principais:
- **Home Page**: Apresentação geral do projeto.
- **Seções de Análise**:
  - Tipos de Contrato.
  - Formato de Trabalho (remoto ou não).
  - Localização Geográfica.
  - Habilidades Exigidas.
- **Download**: Opção de baixar o dataset original.

### Recursos:
- Visualizações geradas dinamicamente.
- Interface responsiva para dispositivos móveis e desktop.
- Navegação intuitiva entre as análises.

---

## Como Contribuir

Se deseja contribuir com o projeto:
1. Faça um fork do repositório.
2. Crie uma branch com sua funcionalidade ou melhoria (`git checkout -b minha-nova-funcionalidade`).
3. Faça commit das suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie um pull request para revisão.

Em caso de dúvidas, abra uma *issue* ou entre em contato diretamente.

---

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---

## Contato

**Elisa Coutinho**
- LinkedIn: [https://www.linkedin.com/in/elisadrummondrc](https://www.linkedin.com/in/elisadrummondrc)
- GitHub: [https://github.com/elisadrcoutinho](https://github.com/elisadrcoutinho)
