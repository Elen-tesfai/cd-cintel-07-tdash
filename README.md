# cintel-07-tdash
Interactive dashboard project for Module 7 of the Cintel course using PyShiny.

## Project Overview

This project is an interactive analytics dashboard created for **Module 7 of the Cintel course**. The dashboard uses **PyShiny**, which combines Python with the Shiny framework to build interactive web applications. It integrates data visualizations and analytics tools for dynamic, real-time interaction.

## Features

- **Interactive Dashboard**: Built using **PyShiny** for real-time data interaction and visualizations.
- **Dynamic Data Visualizations**: Supports various forms of data representation (e.g., graphs, tables).
- **Deployment on GitHub Pages**: The project is hosted on GitHub Pages for easy access and sharing.
- **Modular Design**: The project is designed with modular components, allowing easy customization and scalability.
## Setting Up a Virtual Environment (Optional but Recommended)

It's highly recommended to create a virtual environment for this project to avoid dependency conflicts with other Python projects.

### To create a virtual environment:

1. Create the virtual environment:
   ```bash
   python -m venv venv
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
Once you're done, you can deactivate the virtual environment:
deactivate

## Getting Started

To set up and run the project locally, follow these steps:

### Step 1: Clone the Repository
Clone the repository to your local machine using Git:
```bash
git clone https://github.com/Elen-tesfai/cintel-07-tdash.git

Change directory to the project folder
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
Once you’ve cloned the repository and installed the dependencies, you can run the app locally:
```bash
python app.py
```
This will launch a local server. To view the dashboard, open your browser and navigate to the provided local address.

### Step 4. Deployment on GitHub Pages:
This project is deployed on GitHub Pages. After forking and setting up the project, you can visit the deployed app at:

  Go to your GitHub repository and click on the Settings tab.
  Scroll down to the GitHub Pages section.
  Under Source, choose the main branch and select the docs folder (or root folder).
  After this, GitHub Pages will deploy the app, and you can view it at:

[https://Elen-tesfai.github.io/cintel-07-tdash/](https://Elen-tesfai.github.io/cintel-07-tdash/)

### Step 5: License Information:
This project is licensed under the MIT License. For more details, see the LICENSE file in the repository.