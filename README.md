
# Med-BhAI

Med-BhAI is an AI-powered assistant that simplifies complex clinical notes into layman-friendly language using AWS Bedrock. It helps make medical documentation more accessible and comprehensible to non-experts such as patients or caretakers.

## Features

- 🧠 Uses Bedrock LLMs to summarize medical notes.
- 📄 Accepts both direct text input and OCR-generated content.
- 🔐 Secure interaction using AWS services and credential management.
- ⚙️ Modular utility files for prompt engineering and Bedrock API invocation.

## Project Structure

```
Med-BhAI/
├── app.py                # Main application entry point
├── aws_utility.py        # AWS credentials and session management
├── bedrock_prompts.py    # Prompt templates for LLM queries
├── bedrock_utility.py    # Interaction logic with AWS Bedrock API
├── requirements.txt      # Python dependencies
```

## Installation

1. **Clone the Repository**

```bash
git clone <repo-url>
cd Med-BhAI
```

2. **Set up a Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up AWS Credentials**

Create a `.env` file with the following:

```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1
```

Alternatively, set up an IAM role with the appropriate permissions if running in a secure environment.

## Usage

Run the main script:

```bash
python app.py
```

You will be prompted to input clinical notes. The script will use a Bedrock model (Claude or similar) to return simplified medical summaries.

## Requirements

The project depends on the following packages:

```text
streamlit==1.45.0
pytesseract==0.3.13
Pillow==11.2.1
boto3==1.38.12
python-dotenv==1.1.0
```

## Author

Developed by Varun Shelke – MS in Information Science, University of Pittsburgh.

## License

This project is licensed under the MIT License.
