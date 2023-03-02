import os
import pygame


def import_folder(path):
    surface_list = []

    for _, __, img_files in os.walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list


def import_folder_dict(path):
    surface_dict = {}

    for _, __, img_files in os.walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_dict[image.split('.')[0]] = image_surf

    return surface_dict


def get_path(path):
    absolute_path = os.path.dirname(__file__)
    full_path = os.path.join(absolute_path, path)

    return full_path
