import json
from aws_utility import initialize_bedrock_client

from bedrock_prompts import get_bedrock_prompt


def summarize_with_bedrock(clinical_notes, prompt_style):
    bedrock = initialize_bedrock_client()
    prompt = get_bedrock_prompt(prompt_style, clinical_notes)

    body = {
        "inferenceConfig": {
            "max_new_tokens": 1000
        },
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = bedrock.invoke_model(
        modelId="amazon.nova-pro-v1:0",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body)
    )

    result = json.loads(response['body'].read())
    return result['output']['message']['content'][0]['text']
