import json
from urllib.parse import parse_qs

# A simple function to simulate marks lookup for names
def get_marks_for_name(name):
    marks_dict = {
        'X': 10,
        'Y': 20,
        'Alice': 15,
        'Bob': 18
    }
    return marks_dict.get(name, 0)  # Default to 0 if the name is not found

def handler(request):
    # Enable CORS by adding the appropriate headers
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",  # This allows CORS for all domains
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type"
    }
    
    # Parse query parameters (name=X&name=Y)
    query_params = request.query_params.get('name', [])
    
    # Get the marks for each name
    marks = [get_marks_for_name(name) for name in query_params]
    
    # Prepare the response
    response = {
        "marks": marks
    }
    
    return {
        "statusCode": 200,
        "body": json.dumps(response),
        "headers": headers
    }
    
