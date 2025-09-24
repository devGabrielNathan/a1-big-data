from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from utils.plotting import stacked_bar

def  analyze_education_vs_job(dataset, min_jobs: int = 5) -> None:

    # Criar tabela cruzada entre emprego e nível de educação
    cross_table = pd.crosstab(dataset["Job Title"], dataset["Education Level"])

    for education in cross_table.columns:

        # Filtrar apenas empregos que têm mais pessoas que min_jobs
        filtered_data = cross_table[cross_table[education] > min_jobs]
        
        # Se não há dados após o filtro, pular este nível de educação
        if filtered_data.empty:
            print(f"Nenhum emprego com mais de {min_jobs} pessoas para o nível de educação: {education}")
            continue
        
        axis_x = list(filtered_data.index)  # Emprego (filtrado)
        axis_y = list(filtered_data[education].values.astype(float))

        figure_name = f"analyze_{education.lower().replace(' ', '')}_by_job.png"
        label = "Quantidade de Pessoas"
        title = f"Quantidade de Pessoas por Emprego com Nível de Educação: {education}"

        stacked_bar(axis_x, axis_y, figure_name, label, title)
        print(f"Gráfico salvo em outputs/{figure_name}")