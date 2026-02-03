import sys
import pygame
from settings import Settings
from ship import Ship
from storm import Storm
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    def __init__(self):
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width= self.screen.get_rect().width
        self.settings.screen_height= self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship=Ship(self)
        self.bullets= pygame.sprite.Group()
        # self.storm=Storm(self)
        self.alien = pygame.sprite.Group()
        self._create_fleet()
        
        self.play_button = Button(self,"Play")
        
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.check_high_score()
            self.sb.prep_ships()
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            pygame.mouse.set_visible(False)
            
    def _check_aliens_bottom(self):
        screen_rect= self.screen.get_rect()
        
        for a in self.alien.sprites():
            if a.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
        
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            self.alien.empty()
            self.bullets.empty()
            
            self._create_fleet()
            self.ship.center_ship()
            
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.alien, True,True)
        
        if collisions:
            for aliens in collisions.values():
                
                self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
        if not self.alien:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increment_speed()
            
            self.stats.level += 1
            self.sb.prep_level()
    
    def _change_fleet_direction (self):
        for a in self.alien.sprites():
            a.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_fleet_edges(self):
        for a in self.alien.sprites():
            if a.check_edges():
                self._change_fleet_direction()
                break
    
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avail_space = self.settings.screen_width - (2*alien_width)
        num_aliens_x = avail_space //  (2 * alien_width)
         
        ship_height = self.ship.rect.height
        avail_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        num_rows = avail_space_y // (2 * alien_height)
        
        for row_number in range(num_rows):
            for a in range(num_aliens_x):
                self._create_alien(a,row_number)
        
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.alien.add(alien)
        
    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                print(len(self.bullets))
        self._check_bullet_alien_collisions()
        
        
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
             self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                       
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # self.storm.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alien.draw(self.screen)
        self.sb.show_scoreboard()
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.alien.update()
        if pygame.sprite.spritecollideany(self.ship, self.alien):
            print("Ship's hit!")
            self._ship_hit()
        self._check_aliens_bottom()
            # font = pygame.font.SysFont(None, 48)
            # text = font.render("Mayday! Ship hit!!", True, (255, 0, 0))
            # rect = text.get_rect(center=self.screen.get_rect().center)
            # self.screen.blit(text, rect)
            # pygame.display.flip()
            # pygame.time.delay(1500)
        

        
    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

if __name__== "__main__":
    ai = AlienInvasion()
    ai.run_game()
    
