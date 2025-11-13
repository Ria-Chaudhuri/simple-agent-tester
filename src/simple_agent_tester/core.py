import yaml
import ollama
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from pathlib import Path

console = Console()

AGENT_FILE= Path(__file__).parent/ "templates" / "agent.yaml"

def execute_agent_task():
    """
    Loads config and executes the agent task using Ollama.
    """
    # --- 1. Read the config.yaml file ---
    with open(AGENT_FILE, "r") as f:
        config = yaml.safe_load(f)

    # --- 2. Get Connection Config ---
    # Get the connection block, or an empty dict as a default
    connection_config = config.get("connection", {})
    # Get base_url, or use the default if not specified
    base_url = connection_config.get("base_url", "http://localhost:11434")

    # --- 3. Get Agent Config ---
    agent_config = config.get("agent")
    if not agent_config:
        console.print("[bold red]Error: 'agent' section not found in config.yaml.[/bold red]")
        return

    # Get agent values
    role = agent_config.get("role")
    task = agent_config.get("task")
    model = agent_config.get("model")

    if not role or not task or not model:
        console.print("[bold red]Error: 'role', 'task', and 'model' must be defined in config.yaml.[/bold red]")
        return

    # --- 4. Display the running task ---
    console.print(Panel(
        f"[bold]Host:[/bold] {base_url}\n"
        f"[bold]Model:[/bold] {model}\n"
        f"[bold]Role:[/bold] {role}\n"
        f"[bold]Task:[/bold] {task}",
        title="[bold magenta]🚀 Starting Agent Task (Ollama)[/bold magenta]",
        expand=False
    ))

    # --- 5. Run Ollama Task ---
    try:
        # Create a client that points to the specified host
        client = ollama.Client(host=base_url)

        messages = [
            {"role": "system", "content": role},
            {"role": "user", "content": task}
        ]

        with console.status("[bold green]Agent is thinking...", spinner="dots") as status:
            # Check if Ollama is running and accessible
            try:
                client.list()
            except Exception:
                console.print(f"[bold red]Error: Could not connect to Ollama at {base_url}[/bold red]")
                console.print("Please make sure the Ollama application is running and accessible.")
                return

            # Run the chat completion
            response = client.chat(
                model=model,
                messages=messages
            )

        result = response['message']['content']
        
        # --- 6. Print the result ---
        console.print(Panel(
            Markdown(result),
            title="[bold green]✅ Agent Result[/bold green]",
            border_style="green"
        ))

    except Exception as e:
        console.print(f"[bold red]Error during Ollama call:[/bold red] {e}")
        console.print(f"Make sure you have pulled the model: [bold cyan]ollama pull {model}[/bold cyan]")