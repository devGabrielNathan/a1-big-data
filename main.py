import os
from time import sleep
import pandas as pd
from utils.clear_terminal import clear_terminal
from utils.menu import menu
from utils.education_and_job import analyze_education_vs_job
from utils.import_csv import import_csv
from utils.gender_and_education import analyze_gender_and_education
from utils.salary_by_age import salary_by_age

if __name__ == "__main__":

    dataset: pd.DataFrame = import_csv()

    while True:

        clear_terminal()

        menu()

        option = input("O que deseja fazer? ")

        clear_terminal()

        match option:    
            case "1":
                salary_by_age(dataset)
            case "2":
                analyze_education_vs_job(dataset)
            case "3":
                analyze_gender_and_education(dataset)
            case "4":
                print("[4] Em desenvolvimento...")
            case "0":
                print("Saindo...")
                break
            case _:
                print("Opção inválida. Tente novamente.")
                continue

        sleep(2)