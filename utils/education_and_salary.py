from utils.plotting import stacked_bar
import pandas as pd

# Definir número mínimo de empregos para considerar no gráfico
MIN_JOBS = 10

def analyze_education_and_salary(dataset):
    # Para cada nível de educação, criar um gráfico de salário médio por cargo
    education_levels = dataset["Education Level"].unique()
    for education_level in education_levels:
        # Filtrar o dataset pelo nível de educação atual
        filtered = dataset[dataset["Education Level"] == education_level]
        
        # Agrupar por cargo
        job_group = filtered.groupby("Job Title")

        # Calcular o salário médio anual por cargo
        average_salary = job_group["Salary"].mean()

        # Ordenar os cargos de forma ascendente pelo salário médio
        job_salary = average_salary.sort_values(ascending=True)

        # Filtrar para mostrar apenas cargos com mais de MIN_JOBS ocorrências
        job_counts = filtered["Job Title"].value_counts()
        valid_jobs = job_counts[job_counts > MIN_JOBS].index

        # Filtrar apenas cargos com funcionários suficientes
        job_salary = job_salary[job_salary.index.isin(valid_jobs)]

        if job_salary.empty:
            continue  # Nenhum cargo com funcionários suficientes 

        axis_x = list(job_salary.index)
        axis_y = list(job_salary.values / 12)  # Converter para salário mensal

        figure_name = f"salary_by_{str(education_level).lower().replace(' ', '_')}.png"
        label = "Salário Médio"
        title = f"Salário médio por cargo no nível de educação: {education_level}"

        stacked_bar(axis_x, axis_y, figure_name, label, title)
        print(f"Gráfico salvo em outputs/{figure_name}")