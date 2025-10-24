import httpx

login_payload = {
    "email": "courses@example.com",
    "password": "spring123"
}
login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()

print(login_response_data)
print(login_response.status_code)

get_user_headers = {"Authorization":f"Bearer {login_response_data['token']['accessToken']}"
}
get_user_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=get_user_headers)


print(get_user_response.json())
print(get_user_response.status_code)
