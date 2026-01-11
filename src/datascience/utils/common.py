import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from typing import Any
from pathlib import Path
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns a ConfigBox object

    Args:
        path_to_yaml (Path): Path to the yaml file

    Raises:
    ValueError: If the yaml file is empty
    e: empty file

    Returns:
        ConfigBox: ConfigBox object containing the yaml file contents
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories, verbose=True):
    """Creates a list of directories

    Args:
        path_to_directories (list): List of directory paths
        ignore_log(bool,optional) : ignore if multiple dirs is to be created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")



@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves json data

    Args:
        path (Path): Path to the json file
        data (dict): Data to be saved in json file
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"json file saved at: {path}")



@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads json file

    Args:
        path (Path): Path to the json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as json_file:
        content = json.load(json_file)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)



@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves binary data using joblib

    Args:
        data (Any): Data to be saved as binary
        path (Path): Path to the binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data using joblib

    Args:
        path (Path): Path to the binary file

    Returns:
        Any: Loaded binary data
    """
    data = joblib.load(filename=path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data