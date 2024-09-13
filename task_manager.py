import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import json
from typing import List, Dict

app = typer.Typer()
console = Console()

TASKS_FILE = "tasks.json"

def load_tasks() -> List[Dict]:
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks: List[Dict]):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def display_tasks(tasks: List[Dict]):
    table = Table(title="Task Manager", box=box.ROUNDED)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Task", style="magenta")
    table.add_column("Status", style="green")

    for i, task in enumerate(tasks, start=1):
        status_emoji = "✅" if task["completed"] else "🕒"
        table.add_row(str(i), task["description"], status_emoji)

    console.print(Panel(table))

@app.command()
def add(description: str):
    """Add a new task"""
    tasks = load_tasks()
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    console.print(f"Task added: {description}", style="bold green")

@app.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
    display_tasks(tasks)

@app.command()
def complete(task_id: int):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]["completed"] = True
        save_tasks(tasks)
        console.print(f"Task {task_id} marked as completed ✅", style="bold green")
    else:
        console.print(f"Invalid task ID: {task_id}", style="bold red")

@app.command()
def remove(task_id: int):
    """Remove a task"""
    tasks = load_tasks()
    if 1 <= task_id <= len(tasks):
        removed_task = tasks.pop(task_id - 1)
        save_tasks(tasks)
        console.print(f"Task removed: {removed_task['description']}", style="bold red")
    else:
        console.print(f"Invalid task ID: {task_id}", style="bold red")

if __name__ == "__main__":
    app()