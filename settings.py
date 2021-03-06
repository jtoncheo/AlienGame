class Settings: 
    '''Creating a class to store all settings for the Alien Invasion game.'''

    def __init__(self): 
        '''Initializing the settings'''
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #Ship settings
        self.ship_speed = 1.5

        #Adding bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,0)
        self.bullets_allowed = 3