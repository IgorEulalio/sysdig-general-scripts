import sys
import json
import os

FILEPATH = os.getenv('FILEPATH', "./controls.json")

def get_score_by_id(file_path, search_id):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data['data']:
                if item['id'] == search_id:
                    return item['score']
        return "ID not found."
    except FileNotFoundError:
        return "File not found."
    except json.JSONDecodeError:
        return "Error decoding JSON."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <search_id> [<search_id> ...]")
        sys.exit(1)
    
    search_ids = sys.argv[1:]  # This will take all arguments after the script name
    file_path = FILEPATH
    
    for search_id in search_ids:
        score = get_score_by_id(file_path, search_id)
        print(f"{search_id}: {score}")