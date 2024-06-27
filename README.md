---
title: PairProAI
emoji: 💻
colorFrom: purple
colorTo: indigo
sdk: streamlit
sdk_version: 1.31.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: Your AI-Powered Pair Programmer
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# PairProAI

PairProAI is a pair programming application that leverages AI to assist in various coding tasks. Whether you need code translation, improvements, simplification, test case generation, efficiency enhancement, or debugging, PairProAI has got you covered. The application is built using Streamlit and deployed on Hugging Face Spaces.

## Table of Contents
- [Features](#features)
- [Live Demo](#live-demo)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Code Translation:** Translate your code into different programming languages.
- **Code Improvements:** Enhance your existing code with best practices and optimizations.
- **Simplify Code:** Simplify complex code structures.
- **Write Test Cases:** Generate test cases for your code.
- **Improve Efficiency:** Optimize your code for better performance.
- **Debug Your Code:** Get help with debugging by providing error messages.

## Live Demo
![](https://github.com/shubhendu-ghosh-DS/PairProAI/blob/main/img/Screenshot%202024-06-27%20095509.png?raw=true)

You can try out PairProAI by visiting the live demo hosted on Hugging Face Spaces:

[PairProAI Live Demo](https://shubhendu-ghosh-pairproai.hf.space)

## Installation
To install and run the PairProAI app locally, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/shubhendu-ghosh-DS/PairProAI.git
    cd PairProAI
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your API key:**
    - Create a `.env` file in the root directory of the project.
    - Add your API key to the `.env` file:
        ```
        API_KEY=your_google_gen_ai_api_key
        ```

5. **Run the application:**
    ```sh
    streamlit run app.py
    ```

## Usage
1. Open your web browser and navigate to the local URL provided by Streamlit, typically `http://localhost:8501`.
2. You will see the PairProAI interface with the following sections:
    - **Paste your code here:** Enter the code you need help with.
    - **Choose an option:** Select the desired assistance type from the dropdown menu.
    - **Generate Solution:** Click the button to generate the solution and explanation.

### Example
1. Paste the code snippet you want to work with in the "Paste your code here" section.
2. Select an option, such as "Code Translation" or "Debug Your Code".
3. Click "Generate Solution" to get the AI-generated code and explanation.
   
![](https://github.com/shubhendu-ghosh-DS/PairProAI/blob/main/img/Screenshot%202024-06-27%20111535.png?raw=true)
![](https://github.com/shubhendu-ghosh-DS/PairProAI/blob/main/img/Screenshot%202024-06-27%20111554.png?raw=true)

## Configuration
PairProAI comes with a basic configuration that can be adjusted to your preferences. The configuration file is located at `.streamlit/config.toml`. By default, the theme is set to a light base with a primary color of `#00dba8`.

## Contributing
We welcome contributions to PairProAI! To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License
PairProAI is open-source software licensed under the [MIT License](LICENSE).

