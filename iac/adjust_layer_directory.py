import os
import shutil
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

IAC_DIRECTORY_NAME = "iac"
SOURCE_DIRECTORY_NAME = "src"
LAMBDA_LAYER_PREFIX = os.path.join("python", "src")


def adjust_layer_directory(shared_dir_name: str, destination: str):
    try:
        root_directory = Path(__file__).parent.parent
        iac_directory = os.path.join(root_directory, IAC_DIRECTORY_NAME)

        logging.info(f"Root directory: {root_directory}")
        logging.info(f"IaC directory: {iac_directory}")

        # Validar existência dos diretórios
        if not os.path.exists(root_directory):
            raise FileNotFoundError(f"Root directory not found: {root_directory}")
        if not os.path.exists(iac_directory):
            raise FileNotFoundError(f"IaC directory not found: {iac_directory}")

        # Diretórios de origem e destino
        destination_directory = os.path.join(iac_directory, destination)
        source_directory = os.path.join(root_directory, SOURCE_DIRECTORY_NAME, shared_dir_name)

        if not os.path.exists(source_directory):
            raise FileNotFoundError(f"Source directory not found: {source_directory}")

        # Excluir o diretório de destino, se existir
        if os.path.exists(destination_directory):
            logging.info(f"Removing existing destination directory: {destination_directory}")
            shutil.rmtree(destination_directory)

        # Copiar arquivos do diretório de origem para o destino
        target_path = os.path.join(destination_directory, LAMBDA_LAYER_PREFIX, shared_dir_name)
        shutil.copytree(source_directory, target_path)
        logging.info(f"Copied files from {source_directory} to {target_path}")

    except Exception as e:
        logging.error(f"Error adjusting layer directory: {e}")
        raise


if __name__ == '__main__':
    adjust_layer_directory(shared_dir_name="shared", destination="lambda_layer_out_temp")