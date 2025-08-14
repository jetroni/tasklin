# Viora

Viora is a versatile Python CLI for leveraging multiple AI providers like OpenAI, Ollama, Anthropic (Claude), and more. It’s designed for developers and creators who want to integrate AI into their workflows, pipelines, or automation, without being limited to “chatting” with AI.

Use it to generate text, process data, or build AI-driven scripts, all directly from your terminal.
---

## Features

* Single CLI to interact with multiple AI providers
* Supports **OpenAI**, **Ollama**, **Anthropic(Claude)**, **DeepSeek** and more in the future
* Returns structured responses with tokens used and execution time
* Supports **sync** and **async** execution
* Clean error handling for missing models, invalid API keys, etc.
* Available on **PyPI** as `viora`

---

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/jetroni/viora.git
cd viora
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Or install directly from PyPI:

```bash
pip install viora
```

(Optional) Make the CLI globally executable:

```bash
pip install --editable .
```

---

## Usage

Basic usage:

```bash
viora --type openai --prompt "Hello AI"
```

Run with async mode:

```bash
viora --type openai --prompt "Hello AI" --async-mode
```

Ollama example (with base URL):

```bash
viora --type ollama --base-url http://localhost:11434 --model codellama --prompt "Hello"
```

---

## CLI Options

| Option         | Description                                       |
| -------------- | ------------------------------------------------- |
| `--type`       | AI provider type (openai, ollama)                 |
| `--prompt`     | Text prompt to send to the AI                     |
| `--key`        | API key for providers that require authentication |
| `--model`      | Model name to use (defaults vary per provider)    |
| `--base-url`   | Base URL for self-hosted providers like Ollama    |
| `--async-mode` | Run asynchronously (flag, no value needed)        |

---

## Response Structure

All responses are returned as a structured JSON object:

```json
{
  "provider": "openai",
  "model": "gpt-4o-mini",
  "output": "Hello! How can I assist you today?",
  "raw": {...},
  "tokens_used": 17,
  "duration_ms": 543
}
```

---

## Contributing

We welcome contributions!

* Add support for new AI providers
* Improve error handling
* Enhance async execution and CLI experience

Please fork the repo and submit a pull request.

---

## License

MIT License. Free to use and modify.

---

## PyPI

viora is published on PyPI. Install via:

```bash
pip install viora
```

Stay up to date with the latest releases and check the package page: [https://pypi.org/project/viora/](https://pypi.org/project/viora/)
