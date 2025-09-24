import os
import matplotlib.pyplot as plt


def stacked_bar(axis_x, axis_y, directory, figure_name, label, title) -> None:
	output_path = os.path.join(directory, figure_name)
	plt.figure(figsize=(12,6)) # configura o tamanho da imagem
	plt.bar(axis_x, axis_y)
	plt.legend(label)
	plt.title(title)
	plt.xticks(rotation=45, ha="right") # coloca o nome dos índices de em 45 graus
	plt.tight_layout() # reposiciona o conteúdo 
	plt.savefig(output_path)
	plt.close()
