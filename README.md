# Agent-Demo

requires Python 3.10 or higher

## Installation
1. Make environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Set your Google API key in each directory that uses it
    ```.env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

## Usage
To run the lang-graph example, execute:
```bash
python lang-graph/main.py
```

To run the google-adk example, execute:
```bash
adk web
```

To run the crew-ai example, execute:
```bash
crewai run
```
