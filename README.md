# apiada
Servidor HTTP super simples para mostrar piadas ruins.
feito com SimpleHTTP server para demostrar como exercicio de [Just Python](https://justpython.style)


# up and running:

1. clone este repo: `git clone git@github.com:jfunez/apiada.git`
2. crie um virtualenv com python 3: `python3 -m venv .venv`
3. ative o virtualenv: `source .venv/bin/activate`
4. iniciar o servidor: `python main.py`
5. abra seu navegador: [http://localhost:8000](http://localhost:8000)

# piadas ruins:

um arquivo de exemplo com as piadas servidas pela api encontra-se em: `potasio.json`


# extração de piadas do reddit:

- com o venv ativado, execute: `python scrap.py <subredit url>.json`
- ex: `python scrap.py "https://www.reddit.com/r/tiodopave.json"`
- como consume a API publica, pode encontrar erros HTTP 429, espere um pouco e tente de novo mais tarde
