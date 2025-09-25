import pandas as pd 
import matplotlib.pyplot as plt
from os import makedirs, path

def salary_by_age(dataset):

    try:
        dataset = dataset[['Age','Salary']]
        
        dataset = dataset.dropna(subset=['Salary'])

        bins = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
        
        labels = ['20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64']
        
        dataset['Age Group'] = pd.cut(dataset['Age'], bins=bins, labels=labels, right=False)
        
        salario_medio_por_faixa = dataset.groupby('Age Group', observed=True)['Salary'].mean()

        fig, ax = plt.subplots(figsize=(12, 6))

        ax.set_facecolor('#e5e5e5')
        
        fig.set_facecolor('#f0f0f0') 

        salario_medio_por_faixa.plot(kind='bar', color='skyblue')
        
        plt.title("Salário Médio por Faixa Etária")
        plt.xlabel('Faixa Etária')
        plt.ylabel('Salário Médio(Valor anual)')
        
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        plt.tight_layout()

        makedirs("outputs", exist_ok=True)
        plt.savefig("outputs/salary_by_age.png")
        plt.close()
        print(f"Gráfico salvo em outputs/salary_by_age.png")

    except Exception as e:
        print(f"Ocorreu um erro ao importar o CSV: {e}")