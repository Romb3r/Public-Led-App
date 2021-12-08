screenHelper = """
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
#: import partial functools.partial

ScreenManager:
    MenuScreen:
    TVScreen:
    
    
<MenuScreen>:
    name: 'menu'
    canvas.before:
        Color:
            rgb: 0/255, 117/255, 94/255
        Triangle:
            points: [0, self.size[1], self.size[0], self.size[1], 0, self.size[1]-(.4*self.size[1])]
            
        Color:
            rgb: 28/255, 155/255, 130/255
        Triangle:
            points: [0, self.size[1], self.size[0], self.size[1], self.size[0], self.size[1]-(.4*self.size[1])]
            
    
    MDLabel:
        text: 'LED Controller'
        halign: 'center'
        pos_hint: {'center_y':0.45}
        font_style: 'Button'
        font_size: '40sp'
        
    MDIcon:
        icon: 'led-strip-variant'
        font_size: '170sp'
        halign: 'center'
        pos_hint: {'center_y':0.65}
        
    BoxLayout:
        orientation: 'vertical'
        spacing: 10
        size_hint: (1, None)
            
        MDBottomNavigation:
            panel_color: (56/255, 56/255, 56/255, 1)
    
            MDBottomNavigationItem:
                name: 'tv'
                text: 'Fernseher'
                icon: 'television-ambient-light'
                on_tab_release: 
                    root.manager.transition.direction = 'up'
                    root.manager.current = 'tv'
        
        
<TVScreen>:
    name: 'tv'
    RelativeLayout: 
        size: root.width, root.height              
        ColorWheel:
            text: 'Fernseher'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.6}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            pos_hint: {'center_x':0.5, 'center_y':0.30}
            text: '    Farbe ändern    '
            font_style: 'Button'
            font_size: '34sp'
            on_release: app.submit_color(colorpicker, '192.168.178.26')
            
        MDIconButton:
            icon: 'heart'
            user_font_size: '30sp'
            pos_hint: {'center_x':0.1, 'center_y':0.85}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
            on_release: app.set_faves(color_label)
    
        MDIcon:
            icon: 'led-on'
            pos_hint: {'center_x':0.6, 'center_y':0.8}
            font_size: '45sp'
            id: color_label  
            
        MDSlider:
            id: slider_tv
            pos_hint: {'center_x':0.5, 'center_y':0.20}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            on_value_normalized:
            on_touch_up: 
                app.submit_brigthness(slider_tv, '192.168.178.26')
                root.change_brightness_led(colorpicker, slider_tv)
                
        MDIconButton:
            icon: 'home'
            size_hint: None, None
            user_font_size: '30sp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.05}
            on_release: 
                root.manager.transition.direction = 'down'
                root.manager.current = 'menu'
            
    AnchorLayout:
        anchor_y: 'top'
        MDToolbar:
            title: "Fernseher"
            icon: 'television-ambient-light'
            md_bg_color: 40/255, 40/255, 40/255, 1
            specific_text_color: 0.4, 1, 0.775, 1
            elevation: 10
            right_action_items: [["television-ambient-light"], ["menu", lambda x: nav_drawer.set_state("open"), "Favorites"]]
        
        MDNavigationDrawer:
            id: nav_drawer
            anchor: 'right'
            state: 'open'
            RV:
                #: set IP '192.168.178.26'
            
            
<RV>:
    viewclass: 'Button'
    data: [{'background_normal': "", 'background_color': tuple(map(float, x.split(', '))), 'on_release': partial(root.send_fave_request, x, IP)} for x in root.get_faves()]
    RecycleBoxLayout:
        default_size: None, dp(40)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        padding: 10
        padding_top: 20
        spacing: 5
            
        
<P>:
    Label:
        text: 'LEDs nicht erreichbar!'
        size_hint: 0.6, 0.2
        pos_hint: {'center_x':0.5, 'center_y':0.5}

"""
