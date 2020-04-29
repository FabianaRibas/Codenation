import requests
import urls
import secrets
import json
import hashlib


class Cryptography:

    def __init__(self):
        self.file_name = 'answer.json'
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.token = secrets.codenation_token
        self.response_json = self.read_json()

    def save_json(self, response_json):
        with open(self.file_name, 'w') as answer:
            json.dump(response_json, answer)

    def read_json(self):
        with open(self.file_name, 'r') as answer:
            read_json = json.load(answer)
        return read_json

    def update_json(self, key, value):
        answer_json = self.read_json()
        answer_json[key] = value
        self.save_json(answer_json)

    # send a http get request and save json as answer.json
    def get_json(self):
        query = urls.api_get_url.format(self.token)
        response = requests.get(query)
        response_json = response.json()
        self.save_json(response_json)

    # decrypt message and update json value 'decifrado'
    def decrypt_message(self):
        encrypted_message = self.response_json['cifrado'].lower()
        rotation = self.response_json['numero_casas']
        decrypted_message = ''

        for letter in encrypted_message:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                # to go from final to beginning of the alphabet
                new_letter_position = (letter_index + rotation) % 26
                decrypted_message += self.alphabet[new_letter_position]
            else:
                decrypted_message += letter
        self.update_json('decifrado', decrypted_message)

    # generate a cryptographic summary using the sha1 algorithm and update json
    def generates_sha1(self):
        answer_json = self.read_json()
        decrypted_string = answer_json['decifrado']
        hash_object = hashlib.sha1(decrypted_string.encode())
        resume = hash_object.hexdigest()
        self.update_json('resumo_criptografico', resume)

    # send a http post request to codenation API as a answer for the problem
    def post_answer_json(self):
        query = urls.api_post_url.format(self.token)
        file = self.response_json
        response = requests.post(query, data=file, files={'answer': open(self.file_name, "rb")})
        print(response.text)


if __name__ == '__main__':
    cr = Cryptography()
    cr.get_json()
    cr.decrypt_message()
    cr.generates_sha1()
    cr.post_answer_json()
