# CI/CD Pipeline Automation Project

This project was created for i2i Academy internship program. It is a standalone Python project that demonstrates automated continuous integration and continuous deployment pipelines using GitHub Actions.

## Technologies Used
* Python 3.10
* Pytest (Unit Testing)
* Selenium WebDriver (UI Testing)
* GitHub Actions (CI/CD Automation)

## Project Structure
* `tax_calculator.py`: Contains the business logic for calculating the telecom tax.
* `test_tax_calculator.py`: Unit test file for the tax calculation logic.
* `test_ui.py`: Automated UI test script running in headless mode.
* `.github/workflows/ci-cd.yml`: The GitHub Actions workflow configuration.

## Setup & Installation (Local Environment)
To run this project locally, you need to set up a virtual environment and install the dependencies.

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install pytest selenium
```

## Pipeline Steps
When code is pushed to the `main` branch, the pipeline automatically runs the following steps on an Ubuntu environment:
1. Sets up Python and installs dependencies.
2. Runs the Unit Test.
3. Runs the Selenium UI Test in headless mode.
4. Prints a deployment confirmation message to the console logs if all tests pass.

## How to Run Tests Locally
After setting up the virtual environment, run the following command in your terminal to execute all tests:
```bash
pytest
```
