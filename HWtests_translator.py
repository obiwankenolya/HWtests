import unittest
import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

text = 'привет'


def translate_it(from_lang, to_lang='ru'):

    params = {
        'key': API_KEY,
        'text': f'{text}',
        'lang': f'{from_lang}-{to_lang}'
        }
    response = requests.get(URL, params=params)
    translation = response.json()['text'][0]

    return translation


class TestTranslator(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_translation(self):
        self.assertEqual(translate_it('ru', to_lang='en'), 'hello')


if __name__ == '__main__':
    unittest.main()
