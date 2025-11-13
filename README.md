#  Simple Agent Tester

**Build your first AI Agent in minutes, not hours.**

        A zero-code CLI tool that lets you test and experiment with local AI agents using Ollama. Perfect for beginners who want to understand how AI agents work without getting lost in complex code.


---

## 🌟 Why This Project?

        Most AI agent tutorials throw you into the deep end with complex frameworks, API keys, and hundreds of lines of code. **Simple Agent Tester** strips away all that complexity:

        - ✅ **No coding required** - Just edit a YAML file
        - ✅ **100% local** - Your data never leaves your machine
        - ✅ **Free forever** - No API keys, no credits, no subscriptions
        - ✅ **Production-ready models** - Powered by Ollama (Llama 3, Mistral, etc.)
        - ✅ **Learn by doing** - Perfect for understanding agent fundamentals

---

## 🚀 Quick Start

### Prerequisites

#### 1. Python 3.8 or higher

        Check your Python version:
        ```bash
        python --version
        ```

        If you need to install Python, download it from [python.org](https://www.python.org/downloads/).

#### 2. Install Ollama

        Ollama is a tool that lets you run large language models locally on your machine.

**🍎 macOS**

        ```bash
        # Download and install from the website
        # Visit: https://ollama.com/download

        # Or use Homebrew
        brew install ollama
        ```

        After installation, start Ollama:
        ```bash
        ollama serve
        ```

**🪟 Windows**

        1. Download the installer from [ollama.com/download](https://ollama.com/download)
        2. Run the `.exe` file
        3. Ollama will start automatically as a system service
        4. Verify installation by opening Command Prompt and typing:
        ```bash
        ollama --version
        ```

**🐧 Linux**

        ```bash
        # Install with one command
        curl -fsSL https://ollama.com/install.sh | sh

        # Start the Ollama service
        ollama serve
        ```

        For systemd-based Linux distributions, you can also run it as a service:
        ```bash
        sudo systemctl start ollama
        sudo systemctl enable ollama  # To start on boot
        ```

#### 3. Download a Ollama Model

        Once Ollama is installed, pull your first model:

        ```bash
        # Pull Llama 3 (Recommended for beginners - 4.7GB)
        ollama pull llama3

        # Or try other models:
        ollama pull mistral      # 4.1GB - Fast and efficient
        ollama pull gemma:2b     # 1.4GB - Lightweight option
        ollama pull codellama    # 3.8GB - Best for code
        ```

        **💡 Tip:** Models are stored locally. The first download takes time, but then they're instant to use.

#### 4. Verify Ollama is Running

        ```bash
        # Check if Ollama is accessible
        curl http://localhost:11434

        # List installed models
        ollama list
        ```

        You should see a response like "Ollama is running" or a list of your installed models.

### Installation

        ```bash
        pip install git+https://github.com/Ria-Chaudhuri/simple-agent-tesetr.git
        ```

        Or clone and install locally:

        ```bash
        git clone https://github.com/Ria-Chaudhuri/simple-agent-tesetr.git
        cd simple_agent_tester
        pip install -e .
        ```

### Your First Agent (3 Steps!)

**Step 1:** 

        Initialize the configuration

        ```bash
        agent-tester init
        ```

        This creates an `agent.yaml` file in `src/simple_agent_tester/templates/`.

**Step 2:** Edit the `agent.yaml` file

        ```yaml
        connection:
        base_url: "http://localhost:11434"

        agent:
        model: "llama3"
        role: "You are an expert travel planner. You create concise, bulleted itineraries."
        task: "Create a 3-day weekend itinerary for a first-time visitor to Tokyo."
        ```

**Step 3:** Run your agent

        ```bash
        agent-tester run
        ```

        That's it! Watch your AI agent complete the task. 🎉

---

## 📖 What You'll Learn

        By using this tool, you'll understand:

        - **How AI agents work** - The role/task paradigm that powers modern agents
        - **Prompt engineering basics** - How to write effective system and user prompts
        - **Local AI deployment** - Running powerful models without cloud dependencies
        - **Agent architecture** - The foundation before jumping into complex frameworks

---

## 🎯 Example Use Cases

### 1. **Content Creator Agent**
        ```yaml
        agent:
        model: "llama3"
        role: "You are a creative LinkedIn content writer specializing in tech and AI."
        task: "Write an engaging post about the importance of learning AI in 2025."
        ```

### 2. **Code Reviewer Agent**
        ```yaml
        agent:
        model: "mistral"
        role: "You are a senior software engineer who reviews Python code for best practices."
        task: "Review this function and suggest improvements: [paste your code here]"
        ```

### 3. **Personal Tutor Agent**
        ```yaml
        agent:
        model: "llama3"
        role: "You are a patient tutor who explains complex topics using simple analogies."
        task: "Explain how neural networks work to a 10-year-old."
        ```

### 4. **Business Analyst Agent**
        ```yaml
        agent:
        model: "llama3"
        role: "You are a business analyst who creates SWOT analyses."
        task: "Create a SWOT analysis for a startup building AI-powered productivity tools."
        ```

---

## 🛠️ Configuration Guide

### Connection Settings

```yaml
connection:
  base_url: "http://localhost:11434"  # Change if Ollama runs on a different port
```

### Agent Configuration

| Field | Description | Example |
|-------|-------------|---------|
| `model` | The Ollama model to use | `llama3`, `mistral`, `gemma:2b` |
| `role` | The system prompt (agent's identity) | "You are an expert Python developer" |
| `task` | The user prompt (what you want done) | "Write a function to calculate fibonacci numbers" |

### Available Models

Common Ollama models you can use:
- `llama3` - Meta's latest, great all-rounder (Recommended)
- `mistral` - Fast and efficient
- `gemma:2b` - Lightweight option
- `codellama` - Specialized for code
- `phi` - Microsoft's small but powerful model

Run `ollama list` to see all installed models.

---

## 🎨 Features

- **🎯 Zero-Code Interface** - Configure everything through YAML
- **🎨 Beautiful Terminal Output** - Rich formatting with colors and panels
- **⚡ Streaming Responses** - See results as they're generated
- **🔒 100% Private** - All processing happens locally
- **🧪 Instant Experimentation** - Test different prompts in seconds
- **📝 Clear Error Messages** - Helpful guidance when things go wrong
- **🔄 Easy Model Switching** - Try different models with one line change

---

## 🐛 Troubleshooting

### "Could not connect to Ollama"
- Make sure the Ollama app is running
- Check if Ollama is on port 11434: `curl http://localhost:11434`
- Try restarting the Ollama application

### "Model not found"
- Pull the model first: `ollama pull llama3`
- Check available models: `ollama list`

### "Command not found: agent-tester"
- Make sure you installed the package: `pip install -e .`
- Try running with Python: `python -m simple_agent_tester.cli run`

### File path errors
- Make sure you're running commands from the project root directory
- The `init` command creates files in the correct location automatically

---

## 🚧 Roadmap

- [ ] Interactive mode for multi-turn conversations
- [ ] Support for custom templates
- [ ] Agent performance metrics
- [ ] Multiple agent configurations
- [ ] Export conversation history
- [ ] Web UI (optional)
- [ ] Integration with LangChain/AutoGen for advanced users

---

## 🤝 Contributing

Contributions are welcome! This project is perfect for:
- First-time open source contributors
- Anyone learning about AI agents
- Developers who want to improve tooling

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/Ria-Chaudhuri/simple-agent-tesetr.git
cd simple_agent_tester
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e .
```

---

## 📚 Learning Resources

Want to dive deeper into AI agents? Check out:

- [Ollama Documentation](https://ollama.com/docs) - Learn about local LLMs
- [Prompt Engineering Guide](https://www.promptingguide.ai/) - Master prompt writing
- [LangChain Documentation](https://python.langchain.com/) - Next step: Agent frameworks
- [AutoGen Documentation](https://microsoft.github.io/autogen/) - Multi-agent systems

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ria Chaudhuri**

- LinkedIn: [Connect with me](https://www.linkedin.com/in/ria-chaudhuri-62389555)
- GitHub: [@Ria-Chaudhuri](https://github.com/Ria-Chaudhuri)

---

## 🙏 Acknowledgments

- [Ollama](https://ollama.com) - For making local LLMs accessible
- [Typer](https://typer.tiangolo.com/) - For the amazing CLI framework
- [Rich](https://rich.readthedocs.io/) - For beautiful terminal output
- The open-source AI community

---

## ⭐ Star This Project

If this tool helped you build your first AI agent, give it a star! It helps others discover the project.

---

## 💬 Questions or Feedback?

- Open an [Issue](https://github.com/Ria-Chaudhuri/simple_agent_tester/issues)
- Start a [Discussion](https://github.com/Ria-Chaudhuri/simple_agent_tester/discussions)
- Connect with me on [LinkedIn](https://www.linkedin.com/in/ria-chaudhuri-62389555)

---

**Built with ❤️ to make AI agents accessible to everyone.**