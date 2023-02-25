import os
import pygame
from os import walk


def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


def find_path(relative_path):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, relative_path)
    return full_path
