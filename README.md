# Tasklin

![PyPI](https://img.shields.io/pypi/v/tasklin)
![Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjetroni%2Ftasklin%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&label=python)
![License](https://img.shields.io/badge/license-MIT-blue)
![Build](https://img.shields.io/github/actions/workflow/status/jetroni/tasklin/publish.yml)

Tasklin is a Python CLI for integrating multiple AI providers into scripts, pipelines, or automation workflows. It’s built for developers who want structured AI outputs for tasks, processing, or data generation, without being limited to interactive chat.

Website: [https://tasklin.dev](https://tasklin.dev)

---

## Features

* Single CLI for multiple AI providers
* Supports **OpenAI**, **Ollama**, **Anthropic (Claude)**, **DeepSeek**, and more
* Returns structured responses including tokens used and execution time
* Supports **sync** and **async** execution
* Clean error handling for missing models, invalid API keys, etc.
* Cross-platform
* Installable from **PyPI** as `tasklin`

---

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/jetroni/tasklin.git
cd tasklin
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Or install directly from PyPI:

```bash
pip install tasklin
```

(Optional) Make the CLI globally executable:

```bash
pip install --editable .
```

---

## Usage

Basic example:

```bash
tasklin "Generate a report from this data" --type openai --key MY_KEY
```

Ollama example (self-hosted):

```bash
tasklin "Run analysis" --type ollama --base-url http://localhost:11434 --model codellama
```

> ⚠️ Async mode is planned but not implemented yet.

---

## CLI Options

| Option         | Description                                    |
|----------------|------------------------------------------------|
| `--type`       | AI provider type (openai, ollama, etc.)        |
| `--key`        | API key for authenticated providers            |
| `--model`      | Model name (default varies per provider)       |
| `--base-url`   | Base URL for self-hosted providers             |
| `--async-mode` | Run asynchronously (flag, no value needed)     |
| `"prompt"`     | Your actual input/prompt (positional argument) |

---

## Response Structure

All responses are returned as a structured JSON object:

```json
{
  "provider": "openai",
  "model": "gpt-4o-mini",
  "output": "Task output here",
  "raw": {...},
  "tokens_used": 17,
  "duration_ms": 543
}
```

---

## Contributing

Contributions are welcome:

* Add new AI providers
* Improve error handling
* Enhance async execution and CLI experience

Fork the repo and submit a pull request.

---

## PyPI

Install via:

```bash
pip install tasklin
```

Latest releases: [https://pypi.org/project/tasklin/](https://pypi.org/project/tasklin/)

