# Tasklin

Tasklin is a Python CLI for running multiple AI providers from one place. Use it to integrate AI into scripts,
pipelines, or automation, without juggling SDKs, APIs, or different tools.

---

## What it does

- Single CLI for multiple AI providers: OpenAI, Ollama, Anthropic (Claude), DeepSeek, and more.
- Returns structured JSON with output, tokens used, and execution time.
- Handles missing models, invalid API keys, and other errors.
- Lightweight and easy to integrate into workflows.

---

## Install

Clone and set up:

```bash
git clone https://github.com/jetroni/tasklin.git
cd tasklin
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Or install from PyPI:

```bash
pip install tasklin
```

(Optional) Make it globally executable:

```bash
pip install --editable .
```

---

## Usage

Pass your prompt as a positional argument:

```bash
tasklin --type openai --key MY_KEY "Process this data"
```

Self-hosted Ollama example:

```bash
tasklin --type ollama --base-url http://localhost:11434 --model codellama "Transform this input"
```

> ⚠️ Async mode is planned but not implemented yet.

---

## CLI Options

| Option       | Description                                    |
|--------------|------------------------------------------------|
| `--type`     | AI provider (openai, ollama, etc.)             |
| `--key`      | API key if required                            |
| `--model`    | Which model to use (provider-dependent)        |
| `--base-url` | Base URL for self-hosted providers             |
| `"prompt"`   | Your actual input/prompt (positional argument) |

---

## Example output

```json
{
  "provider": "openai",
  "model": "gpt-4o-mini",
  "output": "Processed result here",
  "raw": {
    ...
  },
  "tokens_used": 17,
  "duration_ms": 543
}
```

---

## Contributing

Want to help? Awesome! You can:

- Add new AI providers.
- Improve error handling.
- Tweak the CLI for your own needs.

Just fork the repo, make your changes, and open a PR — we’ll check it out. 😄

---

## PyPI

```bash
pip install tasklin
```

Check the latest releases: [https://pypi.org/project/tasklin/](https://pypi.org/project/tasklin/)

