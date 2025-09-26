def map_education_levels(dataset):
    # mapeando os dados de educacao que possuem mesmo significado
    map_education_levels = {
        "Master's": "Master's Degree",
        "Master's Degree": "Master's Degree",
        "Bachelor's": "Bachelor's Degree",
        "Bachelor's Degree": "Bachelor's Degree",
        "phD": "PhD",
        "PhD": "PhD"
    }

    # seleciona a coluna 'Education Level' e modifica a coluna 'Education Level' com os novos valores mapeados
    dataset['Education Level'] = dataset['Education Level'].replace(map_education_levels)

    return dataset
