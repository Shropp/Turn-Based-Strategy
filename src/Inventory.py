from ursina import *

class Inventory(Entity):
    def __init__(self, tile):
        """ self.background = super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = (.21, .11),
            origin = (-.5, 0.5),
            position = (.65, -.39, -.025),
            color = color.black
            )
        super().__init__(
            parent = self.background,
            model = 'quad',
            scale = (.95, .95),
            origin = (-.5, 0.5),
            position = (.05, -.05, -.05),
            texture = 'white_cube',
            texture_scale = (4,2),
            color = color.dark_gray
            ) """

        super().__init__(
            parent = camera.ui,
            model = 'quad',
            scale = (.2, .1),
            origin = (-.5, 0.5),
            position = (.65, -.4, -.025),
            texture = 'white_cube',
            texture_scale = (4,2),
            color = color.dark_gray
            )
        
        self.background = Entity(
            parent = camera.ui,
            model = 'quad',
            scale = (.22, .11),
            origin = (-.5, 0.5),
            position = (.64, -.39, -.020),
            color = color.black
        )

        self.item_parent = Entity(parent=self, scale=(1/4,1/2))
        self.tile = tile                                  


    def append(self, text, colour, pos, click_func = None):
        if text is None:
            icon = Button(
                parent = self.item_parent,
                model = 'quad',
                origin = (-.5,.5),
                color = colour,
                position = pos,                                       
                z = -.1
                )
        else:
            icon = Button(
            parent = self.item_parent,
            model = 'quad',
            origin = (-.5,.5),
            texture = text + '.psd',
            color = colour,
            position = pos,                                       
            z = -.1,
            on_click = click_func
            )
        
        if text is None or text == 'white':
            text = 'None'
        

        name = text.replace('_', ' ').title()
        icon.tooltip = Tooltip(name)
        icon.tooltip.background.color = color.color(0, 0, 0, .8)