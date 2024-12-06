# cintel-07-tdash
Interactive dashboard project for Module 7 of the Cintel course using PyShiny.

# PyShiny Basic Dashboard (Penguins)

## Tools

- Python
- Shiny for Python
- VS Code + Python Extension
- Git
- GitHub

## Try in the Browser

Go to PyShiny Templates at <https://shiny.posit.co/py/templates/>.
Go to Dashboards / Basic Dashboard.

- <https://shiny.posit.co/py/templates/dashboard/>

## Reference App with Detailed Instructions

For more detailed instructions, see <https://github.com/denisecase/pyshiny-penguins-dashboard-express>.
That project README.md has more detailed instructions, including reminders for Mac and Linux. 

## Get the Code

Fork this project into your own GitHub account.
Clone **your** GitHub repo down to your local machine.
IMPORTANT: Use your GitHub **username** in place of denisecase.
[GitHub CLI](https://cli.github.com/) may work better on some machines.

```shell
git clone https://github.com/denisecase/cintel-07-tdash
```

## Run Locally - Initial Start

After cloning your project down to your Documents folder, open the project folder for editing in VS Code.

Create a local project virtual environment named .venv, activate it, and install the requirements.

When VS Code asks to use it for the workspace, select Yes.
If you miss the window, after installing, select from the VS Code menu, View / Command Palette, and type "Python: Select Interpreter" and select the .venv folder.

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands (for Windows - the activate command is slightly different Linux/Mac).

```shell
py -m venv .venv
.venv\Scripts\Activate
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
```

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
shiny run --reload --launch-browser app/app.py
```

Open a browser to <http://127.0.0.1:8000/> and test the app.

## Run Locally - Subsequent Starts

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
.venv\Scripts\Activate
shiny run --reload --launch-browser app/app.py
```

While the app is running, the terminal is fully engaged and cannot be used for other commands. 
To kill the terminal, click the trashcan icon in the VS Code terminal window. 

## After Changes, Export to Docs Folder

Export to docs folder and test GitHub Pages locally.

Open a new terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands. 
Remember to activate the environment first. 

```shell
.venv\Scripts\Activate
shiny static-assets remove
shinylive export app docs
py -m http.server --directory docs --bind localhost 8008
```

Open a browser to <http://[::1]:8008/> and test the Pages app.

## Push Changes back to GitHub

Open a terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands.

```shell
git add .
git commit -m "Useful commit message"
git push -u origin main
```

## Enable GitHub Pages

Go to your GitHub repo settings and enable GitHub Pages for the docs folder.

## Project Overview

This project is an interactive analytics dashboard built for **Module 7 of the Cintel course**. The dashboard leverages **PyShiny**, a Python framework for building interactive web applications. It incorporates real-time data visualizations and analytics to provide a dynamic user experience.

## Features

- **Interactive Dashboard**: Developed using **PyShiny**, which supports real-time data interaction and visualizations.
- **Dynamic Data Visualizations**: Includes graphs and tables for data presentation.
- **Deployment on GitHub Pages**: Hosted on **GitHub Pages** for easy access and sharing.
- **Modular Design**: The app's modular structure allows for easy customization and scalability.

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
### Deactivate the virtual environment:
To deactivate the virtual environment, run:
```bash
deactivate
```
## Getting Started

To set up and run the project locally, follow these steps:

### Step 1: Clone the Repository
Clone the repository to the local machine using Git:
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
If there's no requirements.txt, manually install dependencies, such as:
```bash
pip install pyshiny flask
```
### Step 3. Deployment on GitHub Pages:
This project is deployed on GitHub Pages. After forking and setting up the project, visit the deployed app at:
```bash
  Go to the GitHub repository and click on the Settings tab.
  Scroll down to the GitHub Pages section.
  Under Source, choose the main branch and select the docs folder (or root folder).
  After this, GitHub Pages will deploy the app, and the app can be viewed at:
```
[https://Elen-tesfai.github.io/cintel-07-tdash/](https://Elen-tesfai.github.io/cintel-07-tdash/)

### Step 4: License Information
This project is licensed under the [MIT License](LICENSE). For more details, please refer to the LICENSE file in the repository.

## Conclusion

This project provides an interactive analytics dashboard using **PyShiny**, offering dynamic visualizations and real-time data interaction. It is deployed on GitHub Pages, making it easily accessible for sharing and further development. The modular design of the app ensures flexibility and scalability for future enhancements. Contributions and adaptations to the project are encouraged.

## Check out my deployed app!
You can view the deployed version of my app here: [Check out my deployed app!](https://tinyurl.com/Elen-app)