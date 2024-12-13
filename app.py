from flask import Flask, render_template, send_from_directory
import plotly.express as px
import pandas as pd
import plotly.io as pio

app = Flask(__name__, static_folder='static')

# Simulação de um DataFrame (Substitua pelo seu dataset real)
state_counts_df = pd.DataFrame({
    'Estado': ['CA', 'TX', 'NY', 'FL', 'WA', 'VT', 'SD', 'WY'],
    'Número de Vagas': [11859, 10528, 7367, 4520, 3000, 150, 120, 80]
})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')


@app.route('/sobre-mim')
def sobre_mim():
    return render_template('sobre_mim.html')

@app.route('/emprego360')
def emprego360():
    return render_template('emprego360.html')

@app.route('/metadados')
def metadados():
    return render_template('metadados.html')

@app.route('/tipo-contrato')
def tipo_contrato():
    return render_template('tipo-contrato.html')

@app.route('/formato-trabalho')
def formato_trabalho():
    return render_template('formato-trabalho.html')

@app.route('/localizacao')
def localizacao():
    # Criar o gráfico coroplético com Plotly
    fig = px.choropleth(
        state_counts_df,
        locations='Estado',
        locationmode="USA-states",
        color='Número de Vagas',
        hover_name='Estado',
        color_continuous_scale=px.colors.sequential.Plasma,
        labels={'Número de Vagas': 'Número de Vagas'},
        title="Distribuição de Vagas por Estado"
    )
    
    # Refinar o layout do mapa
    fig.update_geos(
        showcoastlines=True,
        coastlinecolor="Black",
        projection_type="albers usa"
    )
    fig.update_layout(
        title_font_size=18,
        title_x=0.5,
        coloraxis_colorbar=dict(
            title="Número de Vagas",
            ticks="outside"
        )
    )
    
    # Renderizar o gráfico como HTML
    graph_html = pio.to_html(fig, full_html=False)
    
    # Passar o gráfico renderizado para o template
    return render_template('localizacao.html', graph_html=graph_html)

@app.route('/nivel-experiencia')
def nivel_experiencia():
    return render_template('nivel-experiencia.html')

@app.route('/correlacao-visualizacao-aplicacao')
def correlacao_visualizacao_aplicacao():
    return render_template('correlacao-visualizacao-aplicacao.html')

@app.route('/top-10-titulos')
def top_10_titulos():
    return render_template('top-10-titulos.html')

@app.route('/top-10-vagas')
def top_10_vagas():
    return render_template('top-10-vagas.html')

@app.route('/skills-habilidades')
def skills_habilidades():
    return render_template('skills-habilidades.html')

@app.route('/download')
def download_file():
    # Essa função serve o arquivo CSV para o cliente
    return send_from_directory('static/dados', 'job_posting_linkedin_2024.csv')

# Tratamento de erro 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)