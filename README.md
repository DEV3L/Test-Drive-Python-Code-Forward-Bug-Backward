# Test Drive Python: Code Forward, Bug Backward

Example repository to go with blog post on Test-Drive Python Code Forward, Bug Backward.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/DEV3L/Test-Drive-Python_Code-Forward-Bug-Backward
cd Test-Drive-Python_Code-Forward-Bug-Backward
```

2. Setup a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the dependencies:

```bash
pip install .\[dev\]
```

5. Run the main script:

```bash
python main.py
```

## Testing

### Unit Tests

```bash
pytest
```

With coverage:

```bash
pytest --cov
```

With coverage for Coverage Gutters:

```bash
pytest --cov --cov-report lcov

Command + Shift + P => Coverage Gutters: Watch
```
