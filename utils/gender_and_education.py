from utils.plotting import stacked_bar
import pandas as pd

def analyze_gender_and_education(dataset):
    # Criar tabela cruzada entre gênero e educação
    cross_table = pd.crosstab(dataset["Gender"], dataset["Education Level"])
    
    # Para cada nível de educação, criar um gráfico
    for education_level in cross_table.columns:
        axis_x = list(cross_table.index)
        axis_y = list(cross_table[education_level].values.astype(float))
        
        figure_name = f"gender_by_{education_level.lower().replace(' ', '_')}.png"
        label = "Contagem"
        title = f"Distribuição de Gênero para {education_level}"
        
        stacked_bar(axis_x, axis_y, figure_name, label, title)
        print(f"Gráfico salvo em outputs/{figure_name}")