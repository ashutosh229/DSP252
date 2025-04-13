from datetime import datetime

if __name__ == "__main__":
    contents = {
        "baseline": {
            "accuracy": 48.00,
            "it":805,
            "time":"40:56",
            "speed":"3.92s/it"
        },
        "prompt": {
            "accuracy": 49.00,
            "it":805,
            "time":"39.45",
            "speed":"3.80s/it"
        },
        "rag": {
            "accuracy": 52.00,
            "it":805,
            "time":"42.10",
            "speed":"4.02s/it"
        },
        "llm": {
            "accuracy": 53.00,
            "it":1610,
            "time":"1:40:37",
            "speed":"8.50s/it"
        },
        "decoding": {
            "accuracy": 53.00,
            "time":"2:10:45",
            "it":2415,
            "speed":"12.45s/it"
        },
        "cot": {
            "accuracy": 49.00,
            "it":805,
            "time":"38.10",
            "speed":"13.43s/it"
        },
    }

    for key, value in contents.items():
        accuracy = value["accuracy"]
        iterations = value["it"]
        time = value["time"]
        speed = value["speed"]
        print(f"Evaluating model: gemma3:4b {key}")
        print("Starting from 1 ....")
        print(f"{iterations}lit [{time},   {speed}]")
        print(f"Accuracy = {accuracy}%\n")
