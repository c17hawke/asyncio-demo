"""
Demo for sequential way of downloading images from
pexels.com
"""
import time
import os
from pathlib import Path
from typing import List, Optional
import requests


def download_file(photo_id: str, dirname: str) -> None:
    """download file from Pexels

    Args:
        photo_id (str): id of the photo to download
        dirname (str): directory where photos to be downloaded
    """
    pass

def download_all(list_photo_ids: List[str], dirname: Optional[str]="images_01") -> None:
    """download all photos from the given list

    Args:
        list_photo_ids (List[str]): list of photo ids to download
        dirname (str, optional): directory where photos to be downloaded. Defaults to "images_01".
    """
    pass


if __name__ == '__main__':
    # get the list of photos ids
    with open("list_photo_ids.txt", "r") as f:
        list_photo_ids = [line.rstrip() for line in f.readlines()]
    print(list_photo_ids)
    # call download all function
