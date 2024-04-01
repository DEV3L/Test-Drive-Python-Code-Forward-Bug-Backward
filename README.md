# python-code-blog-posts

Example repository to go with blog posts that have Python related code examples.

This workspace is a Python project setup for a Python project.

The project is also set up with GitHub Actions for continuous integration, as defined in the .github/workflows/python-app.yml file. This workflow runs tests on every push to any branch.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/DEV3L/python-code-blog-posts.git
cd python-code-blog-posts
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
