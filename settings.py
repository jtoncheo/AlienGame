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