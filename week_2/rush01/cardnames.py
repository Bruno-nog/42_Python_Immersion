def toupper(name: str) -> str:
    return name.upper()

def fit_junior(name: str) -> str:
   if (name.find("JUNIOR")):
        return name.replace("JUNIOR", "JR")

def fit_filho(name: str) -> str:
    if (name.find("FILHO")):
        return name.replace("FILHO", "FL")

def fit_neto(name: str) -> str:
   if (name.find("NETO")):
        return name.replace("NETO", "NT")

def fit_pinto(name: str) -> str:
    if (name.find("PINTO")):
        return name.replace("PINTO", "P")
    
def fit_prep(name: str) -> str:
    stopwords = [" DA ", " DE ", " DOS ", " DAS "]
    for word in stopwords:
        if word in name:   
            name = name.replace(word, " ")
    return name

def name_chop(name: str) -> str:
    if len(name) > 26:
        list_name = []
        list_name.append(name.split(" "))
        for arg in list_name:
            name_1 = arg[0]
            name_2 = arg[-1]
        return (name_1 + " " +name_2)
    else:
        return (name)


if __name__ == "__main__":
    names = [
        "Maria Fernanda Oliveira da Silva Albuquerque Costa",
        "Carlos Eduardo dos Santos Albuquerque Pereira",
        "Ana Beatriz de Souza Lima Ferreira Gomes",
        "José Antônio Rodrigues de Almeida Carvalho",
        "Isabela Cristina dos Anjos Figueiredo Neto",
        "Luiz Fernando de Oliveira Marques da Costa",
        "Fernanda Gabriela Mendes de Souza Albuquerque",
        "Pedro Henrique Rodrigues da Silva Ferreira",
        "Cláudia Patrícia de Moraes Santos Oliveira",
        "Raimundo Nonato de Almeida Santos Carvalho",
        "Beatriz Helena de Albuquerque Rocha Mendes",
        "Ricardo Vinícius de Souza Pereira dos Reis",
        "Mariana Luísa Fernandes de Oliveira Albuquerque",
        "Antônio Carlos de Assis Rodrigues da Cunha",
        "Guilherme Augusto de Souza Lima Ferreira Gomes",
        "Cecília Maria de Almeida Santos Rodrigues",
        "Bruno Henrique Carvalho de Souza Albuquerque",
        "Helena Cristina Figueiredo de Oliveira Machado",
        "Patrícia Luiza de Albuquerque Santos Carvalho",
        "Francisco Antônio de Oliveira Mendes da Rocha",
        "Eduarda Beatriz de Moraes Rodrigues Figueiredo",
        "Vitor Hugo de Oliveira Costa dos Anjos Pereira",
        "Gabriela Fernanda de Souza Lima Rodrigues Neto",
        "Rodrigo Antônio de Almeida Costa dos Santos",
        "Letícia Maria de Oliveira Figueiredo Carvalho",
        "Matheus Vinícius dos Reis de Souza Albuquerque",
        "Julia Coelho Brandao'"
    ]

    funcs = [toupper, fit_pinto, fit_junior, fit_filho, fit_neto, fit_prep, name_chop]
    for name in names:
        result = name
        for f in funcs:
            result = f(result)
        print(result)