# dadosLivraria
Para criar um README profissional, precisamos que ele seja claro tanto para quem quer rodar o projeto quanto para quem quer entender a arquitetura (o robô separado do dashboard).

Aqui está um modelo completo e moderno para o seu projeto:

📊 Web Scraping Dashboard: Monitoramento de Preços
Este projeto é uma ferramenta de Data Intelligence que automatiza a coleta de dados de e-commerce e os visualiza em um dashboard interativo. O diferencial deste projeto é a sua arquitetura desacoplada, onde a extração (Selenium) e a visualização (Streamlit) operam de forma independente para garantir performance e estabilidade.

🚀 Funcionalidades
Automação de Coleta: Robô em Selenium que navega por múltiplas categorias e extrai dados reais.

Processamento de Dados: Limpeza e estruturação automática com Pandas.

Dashboard Interativo: Visualização de métricas (Ticket Médio, Total de Itens) e gráficos de dispersão/barras.

Arquitetura Inteligente: Sistema de cache para carregamento instantâneo do Dashboard.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.12+

Extração: Selenium & WebDriver Manager

Análise de Dados: Pandas

Visualização: Streamlit & Plotly

Ambiente: Venv (Virtual Environment)