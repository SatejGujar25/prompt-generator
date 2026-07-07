# Prompt Generator

An AI-powered Python library for generating, refining, scoring, translating, and exporting high-quality prompts using the **CRAFT Prompt Engineering Framework**.

---

## ✨ Features

- AI-powered prompt generation
- CRAFT framework-based prompt creation
- Prompt quality scoring using AI
- Prompt refinement for improved clarity and effectiveness
- Prompt translation into multiple languages
- Export prompts as UTF-8 text files
- Clean and beginner-friendly API
- Modular and scalable architecture

---

## 🚀 Version

Current Version: **v1.0.0**

### Included Features

- Generate Prompt
- Score Prompt
- Refine Prompt
- Translate Prompt
- Export Prompt (.txt)

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/SatejGujar25/prompt-generator.git
```

Move into the project directory

```bash
cd prompt-generator
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

## ⚙️ Requirements

- Python 3.10+
- Groq API Key

---

## 📂 Project Structure

```
AI_Prompt/
│
├── prompt_generator/
│   ├── __init__.py
│   ├── generator.py
│   ├── llm.py
│   ├── craft.py
│   ├── scorer.py
│   ├── refiner.py
│   ├── translator.py
│   └── exporter.py
│
├── examples/
│
├── README.md
├── LICENSE
├── requirements.txt
└── pyproject.toml
```

## 📖 API

### PromptGenerator

| Method | Description |
|----------|-------------|
| `gen_prompt(n)` | Generates one or more prompts |
| `Score()` | Evaluates prompt quality |
| `Refine_prompt()` | Improves an existing prompt |
| `Translate(language)` | Translates the prompt |
| `Export(filename)` | Exports prompt to a UTF-8 text file |

---

## 🧠 Framework

Prompt Generator internally uses the **CRAFT Prompt Engineering Framework**.

- **C** – Context
- **R** – Role
- **A** – Action
- **F** – Format
- **T** – Task

The generated prompt is returned as a natural paragraph while internally preserving all CRAFT components.

---

## 📌 Roadmap

### ✅ Version 1.0

- Prompt Generation
- Prompt Scoring
- Prompt Refinement
- Prompt Translation
- TXT Export

## 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Satej Gujar**

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.