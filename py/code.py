import json
import base64

def encode_value_to_base64(value):
    """
    주어진 값을 Base64로 인코딩합니다.
    
    :param value: 인코딩할 값
    :return: Base64로 인코딩된 문자열
    """
    if isinstance(value, str):
        value_bytes = value.encode('utf-8')
        base64_bytes = base64.b64encode(value_bytes)
        return base64_bytes.decode('utf-8')
    return value

def encode_json_values_to_base64(data):
    """
    JSON 객체의 모든 value 값을 Base64로 인코딩합니다.
    
    :param data: JSON 데이터 (파이썬 딕셔너리 또는 리스트)
    :return: value가 Base64로 인코딩된 JSON 데이터
    """
    if isinstance(data, dict):
        return {k: encode_json_values_to_base64(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [encode_json_values_to_base64(item) for item in data]
    else:
        return encode_value_to_base64(data)

def decode_base64_value(value):
    """
    Base64로 인코딩된 문자열을 디코딩하여 원래 문자열로 변환합니다.
    
    :param value: Base64로 인코딩된 문자열
    :return: 디코딩된 문자열
    """
    if isinstance(value, str):
        value_bytes = value.encode('utf-8')
        decoded_bytes = base64.b64decode(value_bytes)
        return decoded_bytes.decode('utf-8')
    return value

def decode_json_values_from_base64(data):
    """
    JSON 객체의 모든 Base64로 인코딩된 value 값을 디코딩합니다.
    
    :param data: Base64로 인코딩된 JSON 데이터 (파이썬 딕셔너리 또는 리스트)
    :return: Base64가 디코딩된 JSON 데이터
    """
    if isinstance(data, dict):
        return {k: decode_json_values_from_base64(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [decode_json_values_from_base64(item) for item in data]
    else:
        return decode_base64_value(data)

    # JSON value 값을 Base64로 인코딩
    encoded = encode_json_values_to_base64(data)
    print("Encoded JSON:", json.dumps(encoded, ensure_ascii=False, indent=2))

    # Base64로 인코딩된 JSON 값을 다시 디코딩
    decoded = decode_json_values_from_base64(encoded)
    print("Decoded JSON:", json.dumps(decoded, ensure_ascii=False, indent=2))