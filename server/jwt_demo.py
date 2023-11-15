import jwt
import datetime

# 生成JWT
def generate_jwt(secret_key, payload):
    # 设置过期时间（可选）
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    
    # 构造头部
    header = {
        'alg': 'HS256',  # 使用 HMAC SHA-256 算法进行签名
        'typ': 'JWT'
    }

    # 构造载荷
    payload.update({'exp': expiration_time})
    
    # 生成JWT
    token = jwt.encode(payload, secret_key, algorithm='HS256', headers=header)

    return token

# 验证JWT
def verify_jwt(secret_key, token):
    try:
        # 验证JWT，并返回载荷信息
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        print('Token 已过期')
    except jwt.InvalidTokenError:
        print('无效的 Token')
    return None

# 示例用法
if __name__ == "__main__":
    # 设置密钥，密钥应该是一个安全的随机字符串，用于对JWT进行签名
    secret_key = "your_secret_key"

    # 构造要包含在JWT中的信息（payload）
    user_info = {
        'user_id': 123,
        'username': 'john_doe',
        'role': 'admin'
    }

    # 生成JWT
    jwt_token = generate_jwt(secret_key, user_info)
    print(f'Generated JWT: {jwt_token}')

    # 模拟验证JWT
    decoded_payload = verify_jwt(secret_key, jwt_token)
    if decoded_payload:
        print('Decoded Payload:', decoded_payload)
