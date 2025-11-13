<div align="center">

# 🤖 Simple Agent Tester

### *Build your first AI Agent in minutes, not hours*

<p align="center">
  <strong>A zero-code CLI tool for testing local AI agents with Ollama</strong><br>
  Perfect for beginners who want to understand AI agents without complex code
</p>


<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License">
  <img src="https://img.shields.io/badge/Ollama-Compatible-green.svg" alt="Ollama Compatible">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome">
</p>

</div>

---

## 🌟 Why This Project?

### ✅ Simple Agent Tester
- **Zero coding** - Just YAML config
- **100% local** - Privacy guaranteed
- **Free forever** - No hidden costs
- **5 minutes** to first agent
- **Production models** - Llama 3, Mistral, etc.

---

## 🚀 Quick Start

> **⏱️ Total time:** 5-10 minutes | **💻 Difficulty:** Beginner-friendly

### 📋 Step 1: Prerequisites

<details>
<summary><b>✅ Python 3.8 or higher</b> (Click to expand)</summary>

<br>

Check your Python version:
```bash
python --version
```

If you need to install Python, download it from [python.org](https://www.python.org/downloads/).

</details>

<details open>
<summary><b>✅ Install Ollama</b> (Click to expand)</summary>

<br>

Ollama lets you run powerful language models locally on your machine.

#### 🍎 **macOS**

```bash
# Option 1: Download from website
# Visit: https://ollama.com/download

# Option 2: Use Homebrew
brew install ollama

# Start Ollama
ollama serve
```

#### 🪟 **Windows**

```bash
# 1. Download installer from: https://ollama.com/download
# 2. Run the .exe file
# 3. Ollama starts automatically as a system service

# Verify installation
ollama --version
```

#### 🐧 **Linux**

```bash
# One-line installation
curl -fsSL https://ollama.com/install.sh | sh

# Start the service
ollama serve

# Optional: Run as system service
sudo systemctl start ollama
sudo systemctl enable ollama  # Start on boot
```

#### ✅ **Verify Installation**

```bash
# Check if Ollama is running
curl http://localhost:11434

# You should see: "Ollama is running"
```

</details>

<details>
<summary><b>✅ Download Your First Model</b> (Click to expand)</summary>

<br>

Pull a model to use with your agent:

```bash
# Recommended: Llama 3 (4.7GB) - Best all-rounder
ollama pull llama3
```

**Other Options:**

| Model | Size | Best For |
|-------|------|----------|
| `mistral` | 4.1GB | Speed and efficiency |
| `gemma:2b` | 1.4GB | Lightweight/low resources |
| `codellama` | 3.8GB | Code generation |
| `phi` | 1.6GB | Fast responses |

```bash
# View all installed models
ollama list
```

**💡 Tip:** Models download once and run instantly thereafter!

</details>

---

### 📦 Step 2: Install Simple Agent Tester

Choose your preferred method:

```bash
# Option 1: Install from GitHub (Recommended)
pip install git+https://github.com/YOUR-USERNAME/simple_agent_tester.git
```

```bash
# Option 2: Clone and install locally
git clone https://github.com/YOUR-USERNAME/simple_agent_tester.git
cd simple_agent_tester
pip install -e .
```

---

### 🎯 Step 3: Create Your First Agent!

<table>
<tr>
<td align="center" width="10%">

### 1️⃣

</td>
<td>

**Initialize Configuration**

```bash
agent-tester init
```

This creates `agent.yaml` in `src/simple_agent_tester/templates/`

</td>
</tr>

<tr>
<td align="center">

### 2️⃣

</td>
<td>

**Configure Your Agent**

Open `agent.yaml` and edit:

```yaml
connection:
  base_url: "http://localhost:11434"

agent:
  model: "llama3"
  role: "You are an expert travel planner. You create concise, bulleted itineraries."
  task: "Create a 3-day weekend itinerary for a first-time visitor to Tokyo."
```

</td>
</tr>

<tr>
<td align="center">

### 3️⃣

</td>
<td>

**Run Your Agent**

```bash
agent-tester run
```

</td>
</tr>
</table>

<div align="center">

### 🎉 **Congratulations! Your AI agent is now working!**

</div>

---

## 📖 What You'll Learn

<table>
<tr>
<td width="25%" align="center">

### 🧠
**Agent Fundamentals**

</td>
<td width="25%" align="center">

### ✍️
**Prompt Engineering**

</td>
<td width="25%" align="center">

### 🖥️
**Local AI Deployment**

</td>
<td width="25%" align="center">

### 🏗️
**Agent Architecture**

</td>
</tr>
<tr>
<td>

Understand the role/task paradigm that powers modern AI agents

</td>
<td>

Learn to write effective system and user prompts that get results

</td>
<td>

Run powerful models locally without cloud dependencies

</td>
<td>

Build foundation before jumping into complex frameworks

</td>
</tr>
</table>

---

## 🧠 Understanding Roles and Tasks - The Foundation of AI Agents

Before diving into examples, let's understand the **two core components** that make AI agents work: **Roles** and **Tasks**.

### 🎭 What is a Role?

A **Role** is the identity and personality you give to your AI agent. It's like hiring someone for a job - you need to define:
- Who they are
- What they're expert at
- How they should behave
- What perspective they should take

**Think of Role as the "System Prompt"** - it sets the agent's behavior for the entire conversation.

#### 📝 Anatomy of a Good Role:

```yaml
role: "You are [IDENTITY] who [EXPERTISE]. You [BEHAVIOR]."
```

**Example:**
```yaml
role: "You are an expert travel planner who specializes in budget-friendly trips. 
       You create detailed, practical itineraries with specific recommendations."
```

#### ✅ Good Role vs ❌ Bad Role:

<table>
<tr>
<th>❌ Bad Role (Too Vague)</th>
<th>✅ Good Role (Clear & Specific)</th>
</tr>
<tr>
<td>

```yaml
role: "You are helpful"
```

**Problem:** No context, no expertise, no guidance

</td>
<td>

```yaml
role: "You are a senior Python developer 
      who reviews code for readability, 
      performance, and best practices. 
      You provide constructive feedback 
      with specific examples."
```

**Why it works:** Clear identity, specific expertise, defined behavior

</td>
</tr>
</table>

#### 🎯 Role Components:

| Component | Description | Example |
|-----------|-------------|---------|
| **Identity** | Who is the agent? | "You are a professional chef" |
| **Expertise** | What are they expert at? | "specializing in Italian cuisine" |
| **Behavior** | How should they respond? | "You explain recipes step-by-step with precise measurements" |
| **Constraints** | What should they avoid? | "You don't use exotic ingredients" |

---

### 🎯 What is a Task?

A **Task** is the specific job you want your agent to complete. It's the instruction, the question, or the problem you need solved.

**Think of Task as the "User Prompt"** - it's what you actually want the agent to do right now.

#### 📝 Anatomy of a Good Task:

```yaml
task: "[ACTION] [SPECIFIC DETAILS] [CONTEXT/CONSTRAINTS]"
```

**Example:**
```yaml
task: "Create a 3-day itinerary for Tokyo for a first-time visitor 
       with a $1000 budget, focusing on cultural experiences."
```

#### ✅ Good Task vs ❌ Bad Task:

<table>
<tr>
<th>❌ Bad Task (Too Vague)</th>
<th>✅ Good Task (Specific & Clear)</th>
</tr>
<tr>
<td>

```yaml
task: "Tell me about Tokyo"
```

**Problem:** No clear objective, no constraints, too broad

</td>
<td>

```yaml
task: "Create a 3-day weekend itinerary 
      for Tokyo that includes:
      - Must-see cultural sites
      - Best local food experiences
      - Budget: $1000 total
      - Staying in Shinjuku area"
```

**Why it works:** Clear goal, specific requirements, defined constraints

</td>
</tr>
</table>

#### 🎯 Task Components:

| Component | Description | Example |
|-----------|-------------|---------|
| **Action** | What should be done? | "Create", "Analyze", "Review", "Explain" |
| **Specifics** | What exactly? | "a 3-day itinerary for Tokyo" |
| **Context** | What's the situation? | "for a first-time visitor" |
| **Constraints** | Any limitations? | "with a $1000 budget" |
| **Format** | How to present? | "as a bulleted list with times" |

---

### 🔄 How Roles and Tasks Work Together

Think of it like this:

```
ROLE = WHO is doing the work
TASK = WHAT work needs to be done
```

#### 🎬 Real-World Analogy:

Imagine you're hiring someone:

1. **Role** = Their resume and job description
   - "Senior Marketing Manager with 10 years in B2B SaaS"
   
2. **Task** = The project you assign them
   - "Create a Q4 campaign strategy for our new product launch"

#### 💡 Example: Code Review Agent

**Role (WHO):**
```yaml
role: "You are a senior software engineer who specializes in Python. 
       You review code for:
       - Readability and maintainability
       - Performance optimization
       - Security vulnerabilities
       - Best practices and design patterns
       You provide constructive feedback with specific line-by-line suggestions."
```

**Task (WHAT):**
```yaml
task: "Review this Python function and suggest improvements:
       
       def get_user_data(id):
           db = connect_db()
           user = db.query('SELECT * FROM users WHERE id = ' + str(id))
           return user"
```

**Why this works:**
- ✅ Role establishes expertise and review criteria
- ✅ Task provides specific code to review
- ✅ Agent knows exactly what to do and how to do it

---

### 🎨 Role & Task Patterns for Different Use Cases

<details>
<summary><b>📊 Data Analysis Pattern</b></summary>

```yaml
role: "You are a data scientist who specializes in business analytics. 
       You provide insights that are actionable and easy for non-technical 
       stakeholders to understand."

task: "Analyze this sales data and identify the top 3 trends that could 
       impact Q4 revenue. Provide specific recommendations."
```

</details>

<details>
<summary><b>✍️ Content Creation Pattern</b></summary>

```yaml
role: "You are a content marketing specialist who writes engaging, 
       SEO-optimized blog posts for B2B SaaS companies. Your writing is 
       clear, professional, and includes actionable takeaways."

task: "Write a 500-word blog post introduction about the benefits of 
       AI automation in customer service. Target audience: CTOs and 
       Engineering Managers."
```

</details>

<details>
<summary><b>🎓 Teaching/Tutorial Pattern</b></summary>

```yaml
role: "You are a patient programming tutor who explains complex concepts 
       using simple analogies and real-world examples. You break down 
       problems into small, manageable steps."

task: "Explain how recursion works in Python to a beginner who just learned 
       about loops. Use a simple example like calculating factorial."
```

</details>

<details>
<summary><b>🔍 Research Pattern</b></summary>

```yaml
role: "You are a research analyst who synthesizes information from multiple 
       sources into clear, well-structured summaries. You always cite key 
       facts and present balanced viewpoints."

task: "Research and summarize the current state of quantum computing, 
       focusing on practical applications that might be available in the 
       next 5 years."
```

</details>

---

### 🎯 Best Practices for Roles and Tasks

#### ✅ For Roles:

1. **Be Specific About Expertise**
   - ❌ "You are a developer"
   - ✅ "You are a senior React developer specializing in performance optimization"

2. **Define the Behavior/Style**
   - ❌ "You help with code"
   - ✅ "You provide clear explanations with code examples and explain the reasoning behind each suggestion"

3. **Set Boundaries**
   - ❌ "You answer questions"
   - ✅ "You answer questions about Python web development. For questions outside this scope, you politely redirect to appropriate resources"

4. **Include Output Format**
   - ✅ "You provide feedback as a bulleted list with 'Keep', 'Improve', and 'Fix' sections"

#### ✅ For Tasks:

1. **Use Action Verbs**
   - ✅ Create, Analyze, Review, Explain, Design, Optimize, Debug

2. **Provide Context**
   - ❌ "Write a function"
   - ✅ "Write a Python function to validate email addresses, including edge cases"

3. **Specify Constraints**
   - ✅ "Keep the response under 200 words"
   - ✅ "Use only standard library (no external dependencies)"
   - ✅ "Target audience: beginners with no coding experience"

4. **Define Success Criteria**
   - ✅ "The output should include 3 concrete examples"
   - ✅ "Prioritize solutions that don't require infrastructure changes"

---

### 🧪 Experiment and Iterate

The beauty of Simple Agent Tester is you can **experiment freely**:

1. **Try the same task with different roles:**
   ```yaml
   # Professional tone
   role: "You are a corporate business analyst..."
   
   # Casual tone
   role: "You are a friendly mentor who explains things simply..."
   ```

2. **Try different tasks with the same role:**
   - "Explain concept X"
   - "Create an example of X"
   - "Debug this X"

3. **Refine based on output:**
   - If output is too verbose → Add "Be concise" to role
   - If output lacks detail → Add "Provide detailed examples" to role
   - If output is off-topic → Make task more specific

---

### 💡 Pro Tips

1. **Start Simple, Then Refine**
   - Begin with basic role/task
   - Run the agent
   - Adjust based on output
   - Repeat until satisfied

2. **Be Conversational**
   - Write roles and tasks as if talking to a person
   - Use natural language, not commands

3. **Provide Examples in Tasks**
   ```yaml
   task: "Create a haiku about autumn. Example format:
          Line 1: 5 syllables
          Line 2: 7 syllables  
          Line 3: 5 syllables"
   ```

4. **Test Edge Cases**
   - What happens with incomplete tasks?
   - How does the agent handle ambiguity?
   - Does it stay in character (role)?

---

### 🎓 Learning Path

**Week 1:** Understand Roles
- Experiment with different role definitions
- Try the same task with 3 different roles
- Notice how outputs change

**Week 2:** Master Tasks  
- Practice writing clear, specific tasks
- Add constraints and context
- Compare vague vs. specific tasks

**Week 3:** Combine Them
- Create role-task pairs for real use cases
- Build a library of effective combinations
- Share what works!

---

Now that you understand Roles and Tasks, let's see them in action! 👇

---

## 🎯 Example Use Cases

### 💼 **Professional Use Cases**

<details>
<summary><b>📝 Content Creator Agent</b></summary>

```yaml
agent:
  model: "llama3"
  role: "You are a creative LinkedIn content writer specializing in tech and AI."
  task: "Write an engaging post about the importance of learning AI in 2025."
```

</details>

<details>
<summary><b>👨‍💻 Code Reviewer Agent</b></summary>

```yaml
agent:
  model: "codellama"
  role: "You are a senior software engineer who reviews Python code for best practices."
  task: |
    Review this function and suggest improvements:
    
    def calculate_total(items):
        total = 0
        for item in items:
            total = total + item['price']
        return total
```

</details>

<details>
<summary><b>📊 Business Analyst Agent</b></summary>

```yaml
agent:
  model: "llama3"
  role: "You are a business analyst who creates SWOT analyses."
  task: "Create a SWOT analysis for a startup building AI-powered productivity tools."
```

</details>

### 🎓 **Learning & Personal Use Cases**

<details>
<summary><b>🧑‍🏫 Personal Tutor Agent</b></summary>

```yaml
agent:
  model: "llama3"
  role: "You are a patient tutor who explains complex topics using simple analogies."
  task: "Explain how neural networks work to a 10-year-old."
```

</details>

<details>
<summary><b>✈️ Travel Planner Agent</b></summary>

```yaml
agent:
  model: "llama3"
  role: "You are an expert travel planner who creates detailed, budget-conscious itineraries."
  task: "Plan a 5-day trip to Paris for a couple with a $2000 budget."
```

</details>

<details>
<summary><b>🍳 Recipe Assistant Agent</b></summary>

```yaml
agent:
  model: "mistral"
  role: "You are a professional chef who creates recipes based on available ingredients."
  task: "Create a healthy dinner recipe using chicken, broccoli, and rice."
```

</details>

---

## 🛠️ Configuration Guide

### 🔌 Connection Settings

```yaml
connection:
  base_url: "http://localhost:11434"  # Default Ollama endpoint
```

**Common Configurations:**

| Scenario | URL |
|----------|-----|
| Default local | `http://localhost:11434` |
| Custom port | `http://localhost:8080` |
| Remote server | `http://192.168.1.100:11434` |

### 🤖 Agent Configuration

<table>
<tr>
<th width="20%">Field</th>
<th width="40%">Description</th>
<th width="40%">Example</th>
</tr>
<tr>
<td><code>model</code></td>
<td>The Ollama model to use</td>
<td><code>llama3</code>, <code>mistral</code>, <code>gemma:2b</code></td>
</tr>
<tr>
<td><code>role</code></td>
<td>The system prompt defining the agent's identity and behavior</td>
<td><code>"You are an expert Python developer"</code></td>
</tr>
<tr>
<td><code>task</code></td>
<td>The user prompt describing what you want the agent to do</td>
<td><code>"Write a function to sort a list"</code></td>
</tr>
</table>

### 📦 Available Models

<table>
<tr>
<th>Model</th>
<th>Size</th>
<th>Strengths</th>
<th>Best For</th>
</tr>
<tr>
<td><code>llama3</code> ⭐</td>
<td>4.7GB</td>
<td>Balanced, versatile</td>
<td>General tasks, recommended for beginners</td>
</tr>
<tr>
<td><code>mistral</code></td>
<td>4.1GB</td>
<td>Fast, efficient</td>
<td>Quick responses, resource-conscious</td>
</tr>
<tr>
<td><code>gemma:2b</code></td>
<td>1.4GB</td>
<td>Lightweight</td>
<td>Low-resource environments</td>
</tr>
<tr>
<td><code>codellama</code></td>
<td>3.8GB</td>
<td>Code-specialized</td>
<td>Programming, code review, debugging</td>
</tr>
<tr>
<td><code>phi</code></td>
<td>1.6GB</td>
<td>Compact, powerful</td>
<td>Fast inference, mobile/edge</td>
</tr>
</table>

**💡 Tip:** Run `ollama list` to see all locally installed models.

---

## 🐛 Troubleshooting

<details>
<summary><b>❌ "Could not connect to Ollama"</b></summary>

<br>

**Possible causes:**
- Ollama is not running
- Wrong port/URL configuration
- Firewall blocking connection

**Solutions:**
```bash
# 1. Check if Ollama is running
curl http://localhost:11434

# 2. Start Ollama
ollama serve

# 3. Check Ollama status (Linux)
sudo systemctl status ollama

# 4. Verify port in agent.yaml matches your Ollama port
```

</details>

<details>
<summary><b>❌ "Model not found"</b></summary>

<br>

**Solution:**
```bash
# Pull the model first
ollama pull llama3

# Check available models
ollama list

# Update agent.yaml with an installed model name
```

</details>

<details>
<summary><b>❌ "Command not found: agent-tester"</b></summary>

<br>

**Solutions:**
```bash
# 1. Reinstall the package
pip install -e .

# 2. Try running with Python directly
python -m simple_agent_tester.cli run

# 3. Check if pip bin directory is in PATH
pip show simple_agent_tester
```

</details>

<details>
<summary><b>❌ File path errors (config.yaml or agent.yaml not found)</b></summary>

<br>

**Solutions:**
```bash
# 1. Run from project root directory
cd simple_agent_tester

# 2. Reinitialize configuration
agent-tester init

# 3. Check file location
ls src/simple_agent_tester/templates/
```

</details>

<details>
<summary><b>❌ Slow responses</b></summary>

<br>

**Tips to improve speed:**
- Use smaller models: `gemma:2b` or `phi`
- Ensure Ollama has enough system resources
- Close other resource-intensive applications
- Keep tasks concise and specific

</details>

---

## 🗺️ Roadmap

<table>
<tr>
<td width="50%">

### 🚧 Coming Soon
- [ ] Interactive multi-turn conversations
- [ ] Custom template support
- [ ] Agent performance metrics
- [ ] Multiple agent configurations

</td>
<td width="50%">

### 🔮 Future Ideas
- [ ] Export conversation history
- [ ] Web UI (optional)
- [ ] LangChain/AutoGen integration
- [ ] Agent marketplace

</td>
</tr>
</table>

**💡 Have an idea?** [Open an issue](https://github.com/YOUR-USERNAME/simple_agent_tester/issues/new) or start a [discussion](https://github.com/YOUR-USERNAME/simple_agent_tester/discussions)!

---

## 🤝 Contributing

<div align="center">

**Contributions are welcome!** 

This project is perfect for first-time contributors and anyone learning about AI agents.

</div>

### 🎯 How to Contribute

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **✨ Make** your changes
4. **🧪 Test** thoroughly
5. **💾 Commit** your changes
   ```bash
   git commit -m 'Add amazing feature'
   ```
6. **📤 Push** to the branch
   ```bash
   git push origin feature/amazing-feature
   ```
7. **🎉 Open** a Pull Request

### 💻 Development Setup

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/simple_agent_tester.git
cd simple_agent_tester

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run tests (when available)
pytest
```

### 🎨 Areas for Contribution

- 📝 **Documentation** - Improve guides, add examples
- 🐛 **Bug fixes** - Report or fix issues
- ✨ **Features** - Implement items from the roadmap
- 🧪 **Testing** - Add unit and integration tests
- 🌍 **Translations** - Help non-English speakers
- 📖 **Tutorials** - Create learning content

---

## 📚 Learning Resources

Want to dive deeper? Check out these resources:

<table>
<tr>
<td width="50%">

### 🎓 Fundamentals
- [Ollama Documentation](https://ollama.com/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [LLM Basics](https://www.deeplearning.ai/short-courses/)

</td>
<td width="50%">

### 🚀 Advanced Topics
- [LangChain Documentation](https://python.langchain.com/)
- [AutoGen Framework](https://microsoft.github.io/autogen/)
- [AI Agent Patterns](https://www.anthropic.com/research)

</td>
</tr>
</table>

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**TL;DR:** You can use, modify, and distribute this project freely. Just keep the copyright notice.

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