from tests.shared_data.seed_data import LOGIN_DATA

def login_payload():
    return{
        "email":LOGIN_DATA["email"],
        "password": LOGIN_DATA["password"]
    }

def register_payload():
    return{
        "email":"d@gmail.com",
        "password":"123456",
        "role":"user",
        "firstname":"dharvi",
        "lastname":"katrodiya",
        "phone_number_country_code":"+91",
        "phone_number":"9825035999"
    }