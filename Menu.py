import sys, pygame, math, random
#From King of the Pile

class Menu():
    def __init__(self, images):
        self.images = []
        for image in images:
            #print image
            self.images += [pygame.image.load(image)]
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.originalImage = self.image
        self.width, self.height = self.image.get_size() 
        self.playing = False

    def update():
        pass
