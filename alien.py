import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """فئة لتمثيل كائن فضائي واحد في الأسطول."""

    def __init__(self, ai_game, scale_factor=0.1):
        """تهيئة الكائن الفضائي وتحديد موقعه الابتدائي."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # تحميل الصورة الأصلية، ثم تغيير حجمها وتعيين خصائصها.
        original_image = pygame.image.load('images/ss.png')
        self.image = pygame.transform.scale(
            original_image,
            (int(original_image.get_width() * scale_factor),
             int(original_image.get_height() * scale_factor))
        )
        self.rect = self.image.get_rect()

        # بدء الكائن الفضائي من أعلى اليسار.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # تخزين الموضع الأفقي الدقيق للكائن الفضائي.
        self.x = float(self.rect.x)

    def check_edges(self):
        """إرجاع True إذا وصل الكائن الفضائي إلى حافة الشاشة."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """تحريك الكائن الفضائي لليمين أو لليسار."""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
