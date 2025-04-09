# Chess Tournament Manager

## Description
This is a Python-based application to manage chess tournaments. It follows the **Model-View-Controller (MVC)** design pattern for better scalability and maintainability.

## Features
- **Player Management**: Add, view, and manage players.
- **Tournament Management**: Create tournaments, manage rounds, and update match scores.
- **Automatic Match Pairing**: Generate pairings dynamically based on player scores.
- **Reports**: Generate detailed reports about players, tournaments, rounds, and matches.

## Prerequisites
- Python 3.10 or above
- pip (Python package manager)

## Setup Instructions

### 1. Clone the repository
```bash
git clone <https://github.com/Cywawiw/Projet-4>
cd <Projet-4>
```
### 2. Create and activate a virtual environment
```bash
    python -m venv venv
  ```
-Sur Windows, exécutez : `venv\Scripts\activate`  
-Sur macOS et Linux, exécutez :`source venv/bin/activate`
### 3. Install dependencies
```bash
    pip install -r requirements.txt
```
### 4. Run the application
Execute main script :
  ```bash
  python main.py
  ```
## Generate a Flake8 HTML report
### 1. Install flake8 and flake8-HTML
```bash
    pip install flake8 flake8-html
```
### 2.Create a file named .flake8 which will contain the following information
```
[flake8]
max-line-length = 119
exclude = .venv, __pycache__, migrations, data,.git,env,build,dist
format = html
output-file = flake8_rapport/index.html
```
### 3. Run flake8
```bash
    flake8 --format=html --htmldir=flake8_report
```
### 4. Open the report:
Navigate to flake8_report/index.html and open it in you browser

Propriétaire Baptiste Cutillo
