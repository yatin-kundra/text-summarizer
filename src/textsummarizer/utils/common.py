# the function that we are going to be using throughout our code , that are peresnt in uitls/common.py
# instead of writng them again and again we write them once here and then call them when ever we need them

import os
from box.exceptions import BoxValueError
import yaml
from src.textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml : Path ) -> ConfigBox:
    """
    reads yaml file and return

    :arg
    path_to_yaml (str) : path like input

    :raises
    ValueError : if yaml is empty
    e : empty file

    :return:
    ConfigBox : configbox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"file name : {path_to_yaml} loaded succesfullu")
            return  ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories : list, verbose = True):
    """
    create list of directories.

    Args:
    path_to_directories : list of path of directories

    ignore_log (bool, optional) : ignore if multiple dirs is to be created. Defaults to False

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"created directory at {path}")


@ensure_annotations
def get_size(path : Path) -> str:
    """
    get size in KB

    Args:
    path (Path) : path of the file

    Returns:
    str : size in KB

    """

    size_in_kb = round(os.path.getsize(path/1024))
    return f"~{size_in_kb} KB"