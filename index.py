from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample color flashcards data (use a database if needed)
color_flashcards = [
    {"id": 1, "color": "Red", "description": "The color of passion and energy."},
    {"id": 2, "color": "Blue", "description": "The color of calm and tranquility."},
    {"id": 3, "color": "Green", "description": "The color of nature and growth."},
]

# Get all color flashcards
@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify(color_flashcards)

# Get a specific color flashcard by ID
@app.route('/flashcards/<int:flashcard_id>', methods=['GET'])
def get_flashcard(flashcard_id):
    flashcard = next((card for card in color_flashcards if card['id'] == flashcard_id), None)
    if flashcard:
        return jsonify(flashcard)
    else:
        return jsonify({"message": "Flashcard not found"}), 404

# Create a new color flashcard
@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    data = request.get_json()
    if 'color' in data and 'description' in data:
        new_flashcard = {
            "id": len(color_flashcards) + 1,
            "color": data['color'],
            "description": data['description']
        }
        color_flashcards.append(new_flashcard)
        return jsonify(new_flashcard), 201
    else:
        return jsonify({"message": "Missing 'color' or 'description' in the request"}), 400

# Update a color flashcard by ID
@app.route('/flashcards/<int:flashcard_id>', methods=['PUT'])
def update_flashcard(flashcard_id):
    data = request.get_json()
    flashcard = next((card for card in color_flashcards if card['id'] == flashcard_id), None)
    if flashcard:
        if 'color' in data:
            flashcard['color'] = data['color']
        if 'description' in data:
            flashcard['description'] = data['description']
        return jsonify(flashcard)
    else:
        return jsonify({"message": "Flashcard not found"}), 404

# Delete a color flashcard by ID
@app.route('/flashcards/<int:flashcard_id>', methods=['DELETE'])
def delete_flashcard(flashcard_id):
    flashcard = next((card for card in color_flashcards if card['id'] == flashcard_id), None)
    if flashcard:
        color_flashcards.remove(flashcard)
        return jsonify({"message": "Flashcard deleted"})
    else:
        return jsonify({"message": "Flashcard not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
