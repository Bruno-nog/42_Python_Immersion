import json
import random
from datetime import datetime
import math as m
from typing import Any, Dict, List, Optional, Union, Sequence


class Humano:
    def __init__(
        self,
        nome: str,
        idade: int = 40,
        cidade: str = "São Paulo",
        active: bool = True,
    ) -> None:
        self.nome: str = nome
        self.idade: int = idade
        self.cidade: str = cidade
        self.active: bool = active
        self.criado_em: datetime = datetime.now()
        self.contador: int = 0

    def processar_dados(
        self,
        dados: List[Any],
        filtro: Optional[List[Any]] = None
    ) -> List[str]:
        """Processa os dados e retorna o resultado"""
        resultados: List[str] = []

        for item in dados:
            if filtro and item not in filtro:
                continue
            if not isinstance(item, str):
                item = str(item)
            item = item.strip()
            if len(item) > 0:
                resultados.append(item.upper())
                self.contador += 1
            else:
                print("Item vazio encontrado!")

        return resultados

    def calcular_estatisticas(
        self,
        numeros: Sequence[float]
    ) -> Optional[Dict[str, float]]:
        """Calcula algumas estatísticas básicas"""
        if len(numeros) == 0:
            return None

        soma: float = sum(numeros)
        media: float = soma / len(numeros)
        variancia: float = sum((x - media) ** 2 for x in numeros) / len(numeros)
        desvio_padrao: float = m.sqrt(variancia)

        return {
            "soma": soma,
            "media": media,
            "variancia": variancia,
            "desvio_padrao": desvio_padrao,
        }


def gerar_relatorio(
    dados: Union[List[Any], Dict[str, Any]],
    nome_arquivo: str,
    formato: str = "json"
) -> bool:
    """Gera um relatório com base nos dados fornecidos."""
    if formato not in ("json", "csv", "txt"):
        raise ValueError(f"Formato inválido: {formato}")

    seq = dados if isinstance(dados, list) else [dados]

    if formato == "json":
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            json.dump(seq, f, indent=4)
    elif formato == "csv":
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            header = ",".join(seq[0].keys()) if seq and isinstance(seq[0], dict) else ""
            f.write(header + "\n")
            for item in seq:
                if isinstance(item, dict):
                    linha = ",".join(str(v) for v in item.values())
                    f.write(linha + "\n")
    else:  # txt
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            for item in seq:
                f.write(str(item) + "\n")

    print(f"Relatório gerado com sucesso! Arquivo: {nome_arquivo}")
    return True


def calculo_de_resultado(
    a: int,
    b: int,
    c: int,
    d: int = 10,
    e: Optional[int] = None,
    f: bool = False
) -> float:
    resultado: float = 0.0

    if a > 0 and b > 0 and c > 0:
        if f:
            if e is not None:
                resultado = a * b * c * d * e
            else:
                resultado = a * b * c * d
        else:
            for i in range(a):
                for j in range(b):
                    for k in range(c):
                        if i % 2 == 0 and j % 2 == 0 and k % 2 == 0:
                            resultado += 1
                        elif i % 3 == 0 and j % 3 == 0 and k % 3 == 0:
                            resultado += 2
                        else:
                            resultado += 0.5

    return resultado


def gerar_grafico(dados: Any) -> None:
    """Placeholder para função de gráfico."""
    pass


# constantes
X: int = 100
Y: int = 200
z: int = X + Y

LISTA_DE_ITENS: List[str] = [
    "item1",
    "item2",
    "item3",
    "item4",
    "item5"
]


if __name__ == "__main__":
    numeros: List[int] = [random.randint(1, 100) for _ in range(50)]
    projeto: Humano = Humano(nome="Teste", idade=25)
    estatisticas = projeto.calcular_estatisticas(numeros)
    dados_processados = projeto.processar_dados(
        ["a", "b", "c", "", "d", 1, 2, 3]
    )

    print(f"Contador: {projeto.contador}")
    print(f"Estatísticas: {estatisticas}")
    print(f"Dados processados: {dados_processados}")

    gerar_relatorio(estatisticas or [], "relatorio.json")

    for _ in range(10):
        pass
