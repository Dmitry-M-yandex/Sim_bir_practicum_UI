import random
import string


class GenerateRandomClient:

    @staticmethod
    def generate_last_name():
        letters = string.ascii_lowercase
        last_name = ''.join(random.choice(letters) for i in range(10))
        return last_name

    @staticmethod
    def generate_post_code():
        post_code = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        return post_code

    @staticmethod
    def post_code_to_first_name():
        post_code = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        groups = [post_code[i:i + 2] for i in range(0, len(post_code), 2)]
        first_name = ''
        for group in groups:
            num = int(group) % 26
            letter = chr(num + ord('a'))
            first_name += letter
        return first_name
