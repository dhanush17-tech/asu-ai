# ASU AI Chatbot
![asu ai](https://dhanush.wtf/media/semu1fgsxxb.png)

## Overview

The ASU AI chatbot is an interactive tool designed to assist users by providing information and answering queries related to Arizona State University (ASU). Whether you're a current student, prospective student, faculty member, or just curious about ASU, this chatbot leverages AI to deliver timely and relevant responses to a wide array of topics.

## Features

- **Comprehensive ASU Info**: Get details on courses, admissions, campus events, and more.
- **Easy Interaction**: Simple and intuitive interface for querying information.
- **Real-time Responses**: Fast and accurate answers to your ASU-related questions.

## Features

Built using [EmbedChain](https://embedchain.ai), [NextJS](https://nextjs.org), [Railway](https://railway.app), [React](https://react.dev)

## Getting Started

### Prerequisites

Before setting up the project, ensure you have the following installed:
- Git
- Node.js and npm
- Python 3 and pip3

### Setup Instructions

1. **Clone the Repository**

    Start by cloning the repository to your local machine:

    ```bash
    git clone https://github.com/dhanush17-tech/asu-ai.git
    ```

2. **Set Up the UI**

    Navigate to the UI directory and set up the environment:

    ```bash
    cd asu-ai/ui
    ```

    Create a `.env` file in the `ui` directory and add your OpenAI key (replace `xx--d` with your actual OpenAI key):

    ```bash
    echo OPENAI_KEY=xx--d > .env
    ```

    Install the necessary npm packages and run the development server:

    ```bash
    npm install
    npm run dev
    ```

3. **Set Up the API**

    Open a new terminal window or tab, navigate to the `api` directory within the project:

    ```bash
    cd asu-ai/api
    ```

    Install the required Python dependencies:

    ```bash
    pip3 install -r requirements.txt
    ```

    Start the API server with `uvicorn`:

    ```bash
    uvicorn main:app --reload
    ```

### Usage

After setting up both the UI and API, the ASU AI chatbot is ready to use. Open your web browser and navigate to the address provided by the `npm run dev` command to interact with the chatbot.

## Contributing

We welcome contributions! If you have suggestions or want to improve the ASU AI chatbot, please feel free to fork the repository, make your changes, and submit a pull request.

## License
MIT License

Copyright (c) 2023 Dhanush Vardhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.