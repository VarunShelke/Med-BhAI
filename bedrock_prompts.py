def get_bedrock_prompt(prompt_style, notes):
    if prompt_style == "qna_style":
        return f"""
        Please summarize this clinical note using a Q&A format to help a layperson understand it clearly. Do not include technical terms without explaining what they are. Following is the format:

        - What is the condition or concern?
        - What tests or symptoms are mentioned?
        - What is the diagnosis (in simple terms)?
        - What is the treatment plan or next step?
        
        Clinical Note:
        {notes}
        """
    elif prompt_style == "structured_style":
        return f"""
        Read the following clinical note and provide a simplified summary in bullet points. Make it easy to understand for someone without a medical background. Include:

        - What the issue is
        - What tests or observations were done
        - What the diagnosis or concern is
        - What the treatment or next steps are

        Clinical Note:
        {notes}
        """
    elif prompt_style == "friendly":
        return f"""
        Imagine you're explaining the clinical note below to a patient’s family member who has no medical background. Use simple, friendly language and short paragraphs.

        Clinical Note:
        {notes}
        """
    elif prompt_style == "layman":
        return f"""
        Summarize the following clinical note in a way that a non-medical person can easily understand. Avoid using medical jargon. Focus on what's happening, what the patient should know, and any treatments or precautions.

        Clinical Note:
        {notes}
        """
    return None
