# gpt_arxiv_summary

Run using the following command:

```bash
poetry run python run.py --pdf_path <path to pdf> --out_path <path to output directory>
```

Example.
    
```bash
poetry run python run.py --pdf_path ./papers/soccertrack.pdf --out_path ./outputs
```

```bash
poetry run python run.py --pdf_path ./papers/2111.12340.pdf --out_path ./outputs
```

## Requirements

You need to have API keys for the following services:

* OpenAI GPT
* Deep L

Make sure to add them to the `.env` file like this,

```
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>
DEEPL_AUTH_KEY=<YOUR_DEEPL_AUTH_KEY>
```

The requirements are listed in `pyproject.toml` and can be installed using `poetry install`.

## If it doesn't work

Write an issue and I'll try to fix it.