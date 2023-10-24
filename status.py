import sys
import json

def generate_status_json(status):
    status_map = {"status": status}
    return json.dumps(status_map, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py [Success|Warn|Error]")
        sys.exit(1)

    status = sys.argv[1]

    if status not in ["Success", "Warn", "Error"]:
        print("Invalid status. Please use Success, Warn, or Error.")
        sys.exit(1)

    result_json = generate_status_json(status)
    print(result_json)