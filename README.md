# cintel-07-tdash
Interactive dashboard project for Module 7 of the Cintel course using PyShiny.

## Project Overview

This project is an interactive analytics dashboard created for **Module 7 of the Cintel course**. The dashboard uses **PyShiny**, which combines Python with the Shiny framework to build interactive web applications. It integrates data visualizations and analytics tools for dynamic, real-time interaction.

## Features

- **Interactive Dashboard**: Built using **PyShiny** for real-time data interaction and visualizations.
- **Dynamic Data Visualizations**: Supports various forms of data representation (e.g., graphs, tables).
- **Deployment on GitHub Pages**: The project is hosted on GitHub Pages for easy access and sharing.
- **Modular Design**: The project is designed with modular components, allowing easy customization and scalability.

## Tools

- Python
- Shiny for Python
- VS Code + Python Extension
- Git
- GitHub

## Setting Up a Virtual Environment (Optional but Recommended)

It's highly recommended to create a virtual environment for this project to avoid dependency conflicts with other Python projects.

### To create a virtual environment:

1. Create the virtual environment:
```bash
python -m venv .venv
```
2. Activate the virtual environment:

On Windows:
 ```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
### 4. Deactivate the virtual environment:
To deactivate your virtual environment, run:
```bash
deactivate
```
## Getting Started

To set up and run the project locally, follow these steps:

### Step 1: Clone the Repository
Clone the repository to your local machine using Git:
```bash
git clone https://github.com/Elen-tesfai/cintel-07-tdash.git
```
Change directory to the project folder:
```bash
cd cintel-07-tdash
```
### Step 2: Install Dependencies:
If a requirements.txt file is available, install the necessary Python dependencies:
```bash
pip install -r requirements.txt
```
(Optional) If there's no requirements.txt, you can manually install dependencies, such as:
```bash
pip install pyshiny flask
```
### Step 3: Run the Dashboard Locally:
On the repository is cloned and dependencies are installed, run the app locally:
```bash
python app.py
```
This will launch a local server. To view the dashboard, open the browser and navigate to the provided local address (typically http://127.0.0.1:8000/).

## Run Locally - Initial Setup (VS Code Instructions)
If using VS Code, follow these steps for an initial setup:

1. Open the project folder in VS Code.

2. Create a local project virtual environment named .venv
```bash
py -m venv .venv
```
3. Activate the virtual environment (Windows)
```bash
.venv\Scripts\Activate
```
4. Install the requirements
```bash
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
```
5. In VS Code, select the .venv interpreter:
```bash
View > Command Palette > Python: Select Interpreter, then choose .venv
```
6. Run the app
```bash
shiny run --reload --launch-browser app/app.py
```

### Step 4. Deployment on GitHub Pages:
This project is deployed on GitHub Pages. After forking and setting up the project, visit the deployed app at:
```bash
  Go to the GitHub repository and click on the Settings tab.
  Scroll down to the GitHub Pages section.
  Under Source, choose the main branch and select the docs folder (or root folder).
  After this, GitHub Pages will deploy the app, and the app can be viewed at:
```
[https://Elen-tesfai.github.io/cintel-07-tdash/](https://Elen-tesfai.github.io/cintel-07-tdash/)

### Step 5: License Information:
This project is licensed under the MIT License. For more details, see the LICENSE file in the repository.
