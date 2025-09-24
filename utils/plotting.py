from os import makedirs, path
import matplotlib.pyplot as plt


def stacked_bar(axis_x, axis_y, figure_name, label, title, directory="outputs") -> None:
	makedirs(directory, exist_ok=True)
	output_path = path.join(directory, figure_name)
	
	plt.figure(figsize=(12,6)) # configura o tamanho da imagem
	plt.bar(axis_x, axis_y)
	plt.legend(label)
	plt.title(title)
	plt.xticks(rotation=45, ha="right") # coloca o nome dos índices em 45 graus
	plt.tight_layout() # reposiciona o conteúdo 
	plt.savefig(output_path)
	plt.close()
