import pygame
import datetime

CENTER = (767, 400)

def rotate_center(image, angle, center):
    rotated = pygame.transform.rotate(image, angle)
    rect = rotated.get_rect(center=center)
    return rotated, rect

_image_library = {}
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        image = pygame.image.load(path)
        _image_library[path] = image
    return image

pygame.init()
screen = pygame.display.set_mode((1535, 800))
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255, 255, 255))
    
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    sec_angle = -seconds * 6 + 60
    min_angle = -minutes * 6 - 54

    image_of_mickey = get_image('images/mickey_without_hands.png')
    mickey_rect = image_of_mickey.get_rect(center=CENTER)
    screen.blit(image_of_mickey, mickey_rect)

    right_hand = get_image('images/right_hand.png')
    rotated_min, rect_min = rotate_center(right_hand, min_angle, CENTER)
    screen.blit(rotated_min, rect_min)

    left_hand = get_image('images/left_hand.png')
    rotated_sec, rect_sec = rotate_center(left_hand, sec_angle, CENTER)
    screen.blit(rotated_sec, rect_sec)

    pygame.display.flip()
    clock.tick(60)