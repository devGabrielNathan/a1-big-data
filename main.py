import matplotlib.pyplot as plt
import pandas as pd
from utils.import_csv import import_csv
from utils.plotting import stacked_bar

if __name__ == "__main__":
    DIRECTORY = "outputs/"
    
    print("Camille")
    print("1 - Analisar idade vs salário")
    print("2 - Analisar gênero e salário")
    
    print("Leo")
    print("3 - Analisar educação e emprego ")
    print("4 - Analisar gênero e emprego")
    
    print("Gabriel")
    print("5 - Analisar entre genero e educacão")
    print("6 - Analisar idade e anos de experiencia")

    print("Itallo")
    print("7 - Analisar educação e salario")
    print("8 - Analisar anos de experiencia e salario")
    
    print("0 - Sair")

    csv: pd.DataFrame = import_csv()

    while True:
        option = input("O que deseja fazer? ")
        match option:    
            case "1":
                print("[1] Em desenvolvimento...")
            case "2":
                print("[2] Em desenvolvimento...")
            case "3":
                # Exemplo simples: Top 10 empregos por contagem
                counts = csv["Job Title"].value_counts().head(10)
                axis_x = list(counts.index)
                axis_y = list(counts.values.astype(float))
                figure_name = "educacao_emprego.png"
                label = "Contagem"
                title="Top 10 Empregos por Contagem"
                stacked_bar(axis_x, axis_y, DIRECTORY, figure_name, label, title)
                print("Gráfico salvo em outputs/educacao_emprego.png")
            case "4":
                print("[4] Em desenvolvimento...")
            case "5":
                print("[5] Em desenvolvimento...")
            case "6":
                print("[6] Em desenvolvimento...")
            case "7":
                print("[7] Em desenvolvimento...")
            case "8":
                print("[8] Em desenvolvimento...")
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")