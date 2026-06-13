# Contador de Carros com OpenCV

Projeto simples desenvolvido em Python utilizando OpenCV para realizar a contagem de veículos em vídeo.

## Tecnologias Utilizadas

- Python
- OpenCV
- NumPy

## Instalação

Instale as dependências:

```bash
pip install opencv-python numpy
```

## Estrutura

```
Projeto/
│
├── contacarros.py
├── contacarros.mp4
└── README.md
```

## Como Executar

Execute o arquivo Python:

```bash
python contacarros.py
```

## Funcionamento

O sistema utiliza detecção de movimento para monitorar uma região específica da pista. Quando um veículo entra na área definida, ele é contabilizado uma única vez e o contador é atualizado em tempo real.

## Autor

Mateus Samuel
