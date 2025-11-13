import typer
from pathlib import Path
from rich.console import Console
from . import core  # Import the core.py file

# --- Setup ---
app = typer.Typer(help="A simple CLI to test local Ollama agents with zero code.")
console = Console()

# --- File & Path Constants ---
# This points to "config.yaml" in the CURRENT directory
SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_FILE = SCRIPT_DIR / "templates" / "agent.yaml"

# --- This is the text for the default config file ---
DEFAULT_CONFIG_CONTENT = """
# ===============================================
#   Simple Agent Tester Config (Ollama)
# ===============================================
#
# 1. Make sure Ollama is running and you have downloaded a model
#    (e.g., run: ollama pull llama3)
#
# 2. (Optional) Set your Ollama server's URL if it's not on localhost.
# 3. Define your agent's 'role' and 'task'.
# 4. Specify the 'model' name.
#
# Then run: agent-tester run
#

connection:
  base_url: "http://localhost:11434"

agent:
  model: "llama3" # Or "mistral", "gemma:2b", etc.
  role: "You are an expert travel planner. You create concise, bulleted itineraries."
  task: "Create a 3-day weekend itinerary for a first-time visitor to Tokyo."
"""

@app.command()
def init():
    """
    Initializes the agent tester by creating a config.yaml file.
    """
    console.print(f"[bold green]Initializing Agent Tester for Ollama...[/bold green]")

    # --- Create config.yaml ---
    # We check if the Path object exists
    if CONFIG_FILE.exists():
        console.print(f"[yellow]'{CONFIG_FILE}' already exists. Skipping.[/yellow]")
    else:
        try:
            # We write the default config content directly to the file
            with open(CONFIG_FILE, "w") as f:
                f.write(DEFAULT_CONFIG_CONTENT)
            console.print(f"[green]✅ Created '{CONFIG_FILE}'[/green]")
        except Exception as e:
            console.print(f"[red]Error creating config file: {e}[/red]")
            raise typer.Exit()

    console.print(f"\n[bold magenta]Setup complete! Next steps:[/bold magenta]")
    console.print(f"1. Download and run the Ollama app from [blue]https://ollama.com[/blue]")
    console.print(f"2. In your terminal, pull a model (e.g., [bold cyan]ollama pull llama3[/bold cyan])")
    console.print(f"3. Edit [bold cyan]{CONFIG_FILE}[/bold cyan] to define your agent's role and task.")
    console.print(f"4. Run [bold cyan]agent-tester run[/bold cyan] to see the magic!")


@app.command()
def run():
    """
    Runs the agent based on the config.yaml file.
    """
    # This check now works because CONFIG_FILE is a Path object
    if not CONFIG_FILE.exists():
        console.print(f"[bold red]Error:[/bold red] '{CONFIG_FILE}' not found.")
        console.print(f"Please run [bold cyan]agent-tester init[/bold cyan] first.")
        raise typer.Exit()
        
    try:
        # This calls the execute_agent_task function from core.py
        core.execute_agent_task()
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred:[/bold red] {e}")

if __name__ == "__main__":
    app()