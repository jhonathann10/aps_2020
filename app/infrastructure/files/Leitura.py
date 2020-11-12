import csv
import pandas as pd

class Leitura:

    @staticmethod
    def read_file(path: str, file_name: str, extension: str = 'txt', header_names: list = None) -> pd.DataFrame:
        """
            Função para ler o arquivo e criar um pandas DataFrame.
        """

        file_path = f"{path}/{file_name}.{extension}"
        pdf = pd.read_csv(file_path, header=0, skiprows=1,
                          names=header_names)
        return pdf