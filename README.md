
### Commands

- **Add a new task:**
  ```bash
  python task_manager.py add "Your task description"
  ```

- **List all tasks:**
  ```bash
  python task_manager.py list
  ```

- **Mark a task as completed:**
  ```bash
  python task_manager.py complete <task_id>
  ```

- **Remove a task:**
  ```bash
  python task_manager.py remove <task_id>
  ```

## Data Storage

Tasks are stored in a JSON file named `tasks.json`. This file will be created in the same directory as the script if it does not exist.
