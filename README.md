# MaxProfit Builder

A dynamic programming solution to maximize profit by deciding when to build Theatres (T), Pubs (P), and Commercial Parks (C) over a fixed time horizon.

The algorithm calculates the optimal construction schedule that maximizes total profit, given each building's construction time and profit per operational time unit.

## Features
- **Dynamic Programming**: Computes optimal decisions from the end of the timeline backward.
- **Configurable Buildings**: Change build times and profits in `solver/config.py`.
- **CLI Usage**: Compute max profit for any time horizon via `python main.py <time_units>`.
- **Tests Included**: Pytest-based test suite validating core scenarios.

## Project Structure
- **main.py**: CLI entry point to run the optimizer.
- **solver/config.py**: Building configuration for construction time and per-unit profit.
- **solver/optimizer.py**: Dynamic programming implementation of the optimizer.
- **solver/utils.py**: Output formatting utilities.
- **tests/test_optimizer.py**: Pytest test cases for the optimizer.

## Requirements
- **Python**: 3.11 recommended (project venv suggests 3.11)
- **Dependencies**: Listed in `requirements.txt` (primarily `pytest` for tests)

## Setup (Local Development)
1. Create and activate a virtual environment (recommended):
   - macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run
1. From the project root, run with a specified total time horizon (in time units):
   ```bash
   python main.py 13
   ```

2. Example output:
   ```text
   Max Profit = $16500
   Mix: T=2, P=0, C=0
   ```

- **Argument**: `<time_units>` must be an integer representing the total time horizon.

## How to Run Tests
1. Ensure the virtual environment is activated and dependencies are installed.
2. Run pytest from the project root:
   ```bash
   pytest -q
   ```

## Configuration
- Edit building parameters in `solver/config.py`:
  ```python
  BUILDINGS = {
      "T": {"time": 5, "profit": 1500},  # Theatre: 5 units to build, $1500 per operational time unit
      "P": {"time": 4, "profit": 1000},  # Pub: 4 units to build, $1000 per operational time unit
      "C": {"time": 10, "profit": 3000}, # Commercial Park: 10 units to build, $3000 per operational time unit
  }
  ```

- **time**: Construction time units required before the building becomes operational.
- **profit**: Profit earned per time unit after construction completes.

## How the Algorithm Works (Brief)
- The optimizer iterates from the end of the time horizon to the start.
- At each time `t`, it decides whether to:
  - **Wait** (carry over the best result from `t+1`), or
  - **Start a building** if it can finish before the horizon, then add its operational profit (`profit_per_unit * operational_time`) plus the best future profit from the finish time.
- It stores the best profit and the count of each building type in a DP table.

## Notes
- Input validation is minimal; ensure `<time_units>` is a non-negative integer.
- Changing `BUILDINGS` immediately affects computation; re-run with new parameters as needed.

## Example Scenarios (from tests)
- `maximize_profit(7)` → `Max Profit = 3000`, solution could be `T=1,P=0,C=0` or `T=0,P=1,C=0`.
- `maximize_profit(8)` → `Max Profit = 4500`, solution `T=1,P=0,C=0`.
- `maximize_profit(13)` → `Max Profit = 16500`, solution `T=2,P=0,C=0`.

## License
This project is licensed under the terms of the MIT License. See `LICENSE` for details.