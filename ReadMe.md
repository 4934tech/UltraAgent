# 🕶️ Ultra Agent

A powerful AI-powered agent with real-world capabilities.

Project led by [Olav "Olavorw" Sharma](https://github.com/olavorw) & [Sahil Chopra](https://github.com/aunncodes)

## 🖇️ Table of Contents

- [About Ultra Agent](#-about-ultra-agent)
- [Key Features](#-key-features)
- [Documentation](#-documentation)
- [Quickstart](#quickstart)
- [Contributing](#️-contributing)
- [License](#-license)
- [Contact](#-contact)
- [Acknowledgements](#-acknowledgements)

## 🧰 About Ultra Agent

With **Ultra Agent**, you can automate complex workflows, enhance decision-making, and interact seamlessly with real-world systems.

## 🌟 Key Features

- Automation of Complex Workflows: UltraAgent streamlines intricate processes, reducing manual intervention and increasing efficiency.

- Enhanced Decision-Making: By utilizing AI, UltraAgent assists in making informed decisions based on data analysis and predictive modeling.

- Real-World System Integration: UltraAgent seamlessly interacts with existing systems, ensuring smooth integration and operation.

## 📖  Documentation

Full documentation for Ultra Agent, including setup, configuration, and troubleshooting, is available on our [wiki](https://github.com/4934tech/UltraAgent/wiki).

## 🚀Quickstart

1. Clone the repository:

   You may download & extract the repository or use Git to clone it.
   ```bash
   git clone https://github.com/4934tech/ultraagent.git
   cd ultraagent
    ```
2. Configure your credentials:
   
   An OpenAI key is required for the bot. The bot by default is configured to use ElevenLabs for TTS, so you'll need one of those too. If you don't have one, you can use the [legacy TTS engine](./src/audio/tts.py) instead.
   ```bash
   cp .env.example .env
   nano .env
   ```

3. Create a virtual environment:

   We recommend using a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:
    
   If using a virtual environment, make sure it's activated.
   ```bash
   pip install -r requirements.txt
   ```

5. Run the agent:

   This will use your **default sound devices**.
   ```bash
    python main.py
    ```

## 🤝 Contributing

We welcome contributions from the community! Please read our [contributing guidelines](./Contributing.md) for more information.

## 📜 License

This project is licensed under the [GNU General Public License (GPL) v3](./License.md).

## 📞 Contact

For any questions or support, please open an issue in the GitHub repository or contact the maintainers directly.

## 🫂 Acknowledgements

- [OpenAI](https://openai.com) for making this 10x easier with their built-in function support.
- [ElevenLabs](https://eleven-labs.com) for making incredibly fast & high-quality TTS.
- [Google Speech Recognition](https://cloud.google.com/speech-to-text) for their excellent speech recognition capabilities.