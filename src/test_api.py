import unittest
from unittest.mock import patch

from api import obter_frase_motivacional


class TestIntegracaoAPI(unittest.TestCase):

    @patch('api.requests.get')
    def test_obter_frase_com_sucesso(self, mock_get):
        mock_resposta = mock_get.return_value
        mock_resposta.status_code = 200
        mock_resposta.json.return_value = {
            "slip": {
                "id": 999,
                "advice": "Sempre escreva testes automatizados!"
            }
        }
        frase = obter_frase_motivacional()
        self.assertEqual(frase, "Sempre escreva testes automatizados!")
        mock_get.assert_called_once_with("https://api.adviceslip.com/advice")


if __name__ == '__main__':
    unittest.main()
