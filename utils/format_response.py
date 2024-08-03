import json

def format_response(ai_response):
    if not ai_response:
        return {"is_error": True, "error_message": "No AI Response found. Check main.py"} 

    # Split the response into lines
    ai_response = ai_response\
    .replace("```json\n", "")\
    .replace("","").replace("```", "")

    # Parse the JSON response
    parsed_data = json.loads(ai_response)

    # Access the words and clues
    compliment = parsed_data["compliment"]

    parsed_data = {
        "compliment": compliment,
    }

    return {"is_error": False, "data": parsed_data}
