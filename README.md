# Stream Scan

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A real-time scanner for LLM prompts designed to detect and mitigate potential risks before they are processed. This tool helps ensure that prompts are safe, appropriate, and free of malicious content.

## Features

- **Keyword Detection**: Flags prompts containing sensitive keywords
- **Prompt Injection Analysis**: Identifies common prompt injection techniques
- **Readability Metrics**: Scores prompts based on clarity and coherence
- **Toxicity Analysis**: Optional integration with Perspective API
- **Modular Architecture**: Easily extend with custom analyzers

## Installation

```bash
git clone https://github.com/aka76bm/stream-scan.git
cd stream-scan
pip install -e .
```

## Usage

```python
from stream_scan.scanner import StreamScanner

scanner = StreamScanner()
result = scanner.scan("Your prompt here")

if result.is_valid:
    print("Prompt is safe!")
else:
    print(f"Issues found: {result.flags}")
```

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
