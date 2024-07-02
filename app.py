from flask import Flask, request, jsonify
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from typing import Optional

app = Flask(__name__)

items = {}


class Item(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = ""


def log_message(message, level="INFO"):
    print(f"{datetime.utcnow().isoformat()} - {level}: {message}")


@app.route('/items', methods=['POST', 'GET'])
def manage_items():
    if request.method == 'POST':
        try:
            data = request.get_json()
            Item(**data)
        except ValidationError as e:
            return jsonify({'error': e.errors()}), 400

        new_item_id = len(items)
        items[new_item_id] = {
            "id": new_item_id,
            "name": data["name"],
            "description": data.get("description", ""),
            "created_at": datetime.utcnow().isoformat()
        }
        log_message(f"Created item: {new_item_id} - {data['name']}")
        return jsonify(items[new_item_id]), 201
    return jsonify(list(items.values()))


@app.route('/items/<int:item_id>', methods=['GET', 'PUT', 'DELETE'])
def item_details(item_id):
    if item_id not in items:
        return jsonify({'error': 'Item not found'}), 404
    item_data = items[item_id]

    if request.method == 'GET':
        return jsonify(item_data)
    elif request.method == 'PUT':
        try:
            data = request.get_json()
            updated_item = Item(**data)
        except ValidationError as e:
            return jsonify({'error': e.errors()}), 400
        update_data = {}
        for key, value in updated_item.dict().items():
            if key in ['name', 'description']:
                update_data[key] = value
        item_data.update(update_data)
        log_message(f"Updated item: {item_id} - {updated_item.name}")
        return jsonify(items[item_id])
    else:
        del items[item_id]
        log_message(f"Deleted item: {item_id}")
        return jsonify({'message': 'Item deleted'}), 204


if __name__ == '__main__':
    app.run(debug=True)
