import ollama


def analyze_with_llm(
    user_input,
    ml_prediction,
    confidence
):

    try:

        if ml_prediction == 1:
            threat_label = "Malicious"

        else:
            threat_label = "Benign"

        prompt = f"""
Analyze the following cybersecurity event.

Event:
{user_input}

Machine Learning Prediction:
{threat_label}

Confidence Score:
{confidence}%

Return response in this format:

Threat Category:
Severity:
Technical Explanation:
Recommended Mitigation:
"""

        response = ollama.chat(

            model='tinyllama',

            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )

        return response['message']['content']

    except Exception as error:

        return f"LLM analysis failed: {error}"