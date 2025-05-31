# CodeBuddy

CodeBuddy helps developers use language models to analyze projects. [(Read more)](docs/OVERVIEW.md)

## Usage

**Before running, take care of configuring the script to connect to the language model APIs.</br>By default the script is configured to work with [LM Studio](https://lmstudio.ai/) server.**

For information regarding the command line interface, run:
```bash
python3 codebuddy.py --help
```
Clone the repository and run its analysis:

```bash
python3 codebuddy.py --clone https://github.com/dev-vsp/codebuddy.git project
```

A list of actions that this command performs:

1. Cloning the "codebuddy" repository and place it in the "project" directory
2. Connecting to the language model using the default configuration
3. Analyzing a cloned repository
4. Once the analysis is complete, the report will be saved in the repository directory

Re-analyze the cloned repository with API changes:
```bash
python3 codebuddy.py --api http://192.168.10.10:1234 project
```

Run in [Docker](https://docker.com/):
```bash
docker run codebuddy --help
```

Refer to the [documentation](docs/OVERVIEW.md) for detailed information on installation, configuration and use.

## License

The project is distributed under the MIT license.
See the [LICENSE](LICENSE) file for details.
