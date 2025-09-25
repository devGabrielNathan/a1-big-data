import pandas as pd
from utils.education_and_job import analyze_education_vs_job
from utils.import_csv import import_csv
from utils.gender_and_education import analyze_gender_and_education
from utils.salary_by_age import salary_by_age

if __name__ == "__main__":
    
    print("Camile")
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

    dataset: pd.DataFrame = import_csv()

    while True:
        option = input("O que deseja fazer? ")
        match option:    
            case "1":
                salary_by_age(dataset)
            case "2":
                print("[2] Em desenvolvimento...")
            case "3":
                analyze_education_vs_job(dataset)
            case "4":
                print("[4] Em desenvolvimento...")
            case "5":
                analyze_gender_and_education(dataset)
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