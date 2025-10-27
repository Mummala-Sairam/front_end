from flask import Flask, request, jsonify
import json
app = Flask(__name__)
@app.route('/verify', methods=['POST'])
def verify():
    image = request.files.get('image')
    json_data = request.form.get('data')
    if not image or not json_data:
        return jsonify({"error": "Both image and data are required"}), 400
    filename = image.filename.lower()
    if not (filename.endswith('.jpg') or filename.endswith('.jpeg')):
        return jsonify({"error": "Only JPG or JPEG image files are allowed"}), 400
    try:
        data = json.loads(json_data)
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    verified = data.get("user_id") == "12345"
    message = "User verified successfully!" if verified else "Verification failed."
    return jsonify({
        "verified": verified,
        "message": message,
        "filename": filename
    })

if __name__ == '__main__':
    app.run(debug=True)
