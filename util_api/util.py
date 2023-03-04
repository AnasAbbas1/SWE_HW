from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/compare-versions', methods=['POST'])
def compare_versions():
    try:
        version1 = request.json['version1']
        version2 = request.json['version2']
    except KeyError:
        return jsonify({'error': 'version1 and version2 are required parameters'}), 400

    if not is_valid_version(version1) or not is_valid_version(version2):
        return jsonify({'error': 'version1 and version2 must be valid version strings'}), 400

    v1_parts = version1.split('.')
    v2_parts = version2.split('.')
    for i in range(max(len(v1_parts), len(v2_parts))):
        v1_num = int(v1_parts[i]) if i < len(v1_parts) else 0
        v2_num = int(v2_parts[i]) if i < len(v2_parts) else 0
        if v1_num < v2_num:
            return jsonify({'result': -1})
        elif v2_num < v1_num:
            return jsonify({'result': 1})
    return jsonify({'result': 0})


def is_valid_version(version):
    return all(part.isdigit() for part in version.split('.'))

if __name__ == '__main__':
    app.run(debug=True)