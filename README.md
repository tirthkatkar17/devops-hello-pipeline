# DevOps End-to-End Project: Python, Docker, Pytest, Jenkins & Evidently AI

This repository implements the complete end-to-end DevOps sequence:
1. **hello.py**: Lightweight single-file Python application.
2. **VSCode Project**: Complete `.vscode/` settings, debug launches, and automated tasks.
3. **Git Version Control**: Clean repository structure tracked under Git and GitHub.
4. **Jenkins Setup**: Configured CI/CD pipeline running on port `8081`.
5. **Pull Code**: Automated Git checkout in Jenkins.
6. **Run Jenkins**: Jenkins Pipeline (`Jenkinsfile`) builds, tests, and monitors the project.
7. **Docker Engine**: Containerization runtime configuration.
8. **Lightweight Python Image**: Alpine-based Python Docker image (`python:alpine`).
9. **Dockerized App**: `Dockerfile` packaging `hello.py` into container.
10. **Pytest Suite**: Automated unit tests with output printing.
11. **Evidently AI**: Data drift, data quality, and test suite monitoring dashboard.

---

## Project Structure

```text
WS/
├── .vscode/
│   ├── settings.json       # VS Code workspace settings & test discovery
│   ├── launch.json         # Debug configurations (hello.py, pytest)
│   └── tasks.json          # One-click tasks (run, test, docker, monitor)
├── tests/
│   └── test_hello.py       # Pytest unit tests
├── hello.py                # Main application file
├── Dockerfile              # Lightweight alpine Docker container specification
├── .dockerignore           # Container build exclusions
├── Jenkinsfile             # Jenkins CI/CD declarative pipeline
├── monitor.py              # Evidently AI monitoring script
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Quick Start Commands

### 1. Run Application
```powershell
python hello.py
```

### 2. Run Pytest Suite
```powershell
pytest -v -s
```

### 3. Build & Run Docker Container
```powershell
docker build -t hello-python:latest .
docker run --rm hello-python:latest
```

### 4. Run Evidently AI Monitor
```powershell
python monitor.py
```
This generates `evidently_report.html` and `evidently_test_suite.html`.
