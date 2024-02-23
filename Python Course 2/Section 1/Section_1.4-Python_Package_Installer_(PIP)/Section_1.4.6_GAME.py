# 1.4.6 A simple test program

# Now that pygame is finally accessible, we can try to use it in a very simple test program:

import pygame

run = True
width = 500
height = 400
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to Kire's game", True, (255, 127, 0))
# text1 = font.render("Welcome to Kire's Game", True, (255,127,0))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT \
                or event.type == pygame.MOUSEBUTTONUP \
                or event.type == pygame.KEYUP:
            run = False


# The pip install has two important additional abilities:

# it is able to update a locally installed package – e.g., if you want to make sure that you’re using the latest
# version of a particular package, you can run the following command:
#
# pip install -U package_name
#
#
# where -U means update. Note: this form of the command makes use of the --user option for the same purpose as
# presented previously;
#
# it is able to install a user-selected version of a package (pip installs the newest available version by default);
# to achieve this goal you should use the following syntax: pip install package_name==package_version
#
#
# (note the double equals sign) e.g.,
# pip install pygame==1.9.2
#
#
# If any of the currently installed packages are no longer needed, and you want to get rid of them, pip will be
# useful, too. Its uninstall command will execute all the needed steps.
#
# The required syntax is clear and simple:
#
# pip uninstall package_name
#
# so if you don't want pygame anymore, you can execute the following command:
#
# pip uninstall pygame
#
# Pip will want to know if you’re sure about the choice you're making – be prepared to give the right answer.
