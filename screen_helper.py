screenHelper = """
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
#: import partial functools.partial

ScreenManager:
    MenuScreen:
    TVScreen:
    SchreibtischScreen:
    SofaScreen:
    ControllAll:
    
    
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
                name: 'controllAll'
                text: "Alle Led's"
                icon: 'home-assistant'
                halign: 'center'
                on_tab_release: 
                    root.manager.transition.direction = 'up'
                    root.manager.current = 'controllAll'
    
            MDBottomNavigationItem:
                name: 'schreibtisch'
                text: 'Schreibtisch'
                icon: 'desktop-tower-monitor'
                on_tab_release: 
                    root.manager.transition.direction = 'up'
                    root.manager.current = 'schreibtisch'
    
            MDBottomNavigationItem:
                name: 'sofa'
                text: 'Sofa'
                icon: 'sofa-single'
                on_tab_release: 
                    root.manager.transition.direction = 'up'
                    root.manager.current = 'sofa'
    
            MDBottomNavigationItem:
                name: 'tv'
                text: 'Fernseher'
                icon: 'television-ambient-light'
                on_tab_release: 
                    root.manager.transition.direction = 'up'
                    root.manager.current = 'tv'
        
        
<ControllAll>:
    name: 'controllAll'
    RelativeLayout:
        size: root.width, root.height   
        ColorWheel:
            text: 'Sofa'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.6}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            text: '    Farbe ändern    '
            font_style: 'Button'
            font_size: '34sp'
            pos_hint: {'center_x':0.5, 'center_y':0.30}
            on_release: app.submit_color_all(colorpicker)
            
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
            id: slider_all
            pos_hint: {'center_x':0.5, 'center_y':0.20}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            on_value_normalized:
            on_touch_up: 
                app.submit_brigthness_all(slider_all)
                root.change_brightness_led(colorpicker, slider_all)
                
        MDRectangleFlatButton:
            pos_hint: {'center_x': 0.21, 'center_y':0.07}
            text: '     Off     '
            font_style: 'Button'
            font_size: '15sp'
            on_release: app.all_off()
            
        MDIconButton:
            icon: 'home'
            user_font_size: '30sp'
            size_hint: None, None
            pos_hint: {'center_x': 0.5, 'center_y': 0.05}
            on_release: 
                root.manager.transition.direction = 'down'
                root.manager.current = 'menu'
                
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: app.theme_cls.primary_color
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.07}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'schreibtisch'
                
        MDIcon:
            pos_hint: {'center_x': 1.3, 'center_y': 0.04}
            icon: 'desktop-tower-monitor'
            font_size: '20sp'
            color: (1, 1, 1, 1)
            
    AnchorLayout:
        anchor_y: 'top'
        MDToolbar:
            title: "Alle LED's"
            md_bg_color: 40/255, 40/255, 40/255, 1
            specific_text_color: 0.4, 1, 0.775, 1
            elevation: 10
            right_action_items: [["home-assistant"],["menu", lambda x: nav_drawer.set_state("open"), "Favorites"]]
        
        MDNavigationDrawer:
            id: nav_drawer
            anchor: 'right'
            state: 'open'
            RV_all:
        

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
                
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: app.theme_cls.primary_color
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.1, 'center_y':0.07}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'sofa'
                
        MDIcon:
            pos_hint: {'center_x': 0.65, 'center_y': 0.04}
            icon: 'sofa-single'
            font_size: '20sp'
            color: (1, 1, 1, 1)
            
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
            

<SchreibtischScreen>:
    name: 'schreibtisch'
    RelativeLayout:
        size: root.width, root.height
        ColorWheel:
            text: 'Schreibtisch'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.6}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            text: '    Farbe ändern    '
            font_style: 'Button'
            font_size: '34sp'
            pos_hint: {'center_x':0.5, 'center_y':0.30}
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
            id: slider_schreibtisch
            pos_hint: {'center_x':0.5, 'center_y':0.20}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            on_value_normalized:
            on_touch_up: 
                app.submit_brigthness(slider_schreibtisch, '192.168.178.26')
                root.change_brightness_led(colorpicker, slider_schreibtisch)
                
        MDIconButton:
            icon: 'home'
            size_hint: None, None
            user_font_size: '30sp'
            pos_hint: {'center_x': 0.5, 'center_y': 0.05}
            on_release: 
                root.manager.transition.direction = 'down'
                root.manager.current = 'menu'
                
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: app.theme_cls.primary_color
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.07}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'sofa'
                
        MDIcon:
            pos_hint: {'center_x': 1.3, 'center_y': 0.04}
            icon: 'sofa-single'
            font_size: '20sp'
            color: (1, 1, 1, 1)
            
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: app.theme_cls.primary_color
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.1, 'center_y':0.07}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'controllAll'
                
        MDIcon:
            pos_hint: {'center_x': 0.65, 'center_y': 0.04}
            icon: 'home-assistant'
            font_size: '20sp'
            color: (1, 1, 1, 1)
            
    AnchorLayout:
        anchor_y: 'top'
        MDToolbar:
            title: "Schreibtisch"
            icon: 'desktop-tower-monitor'
            md_bg_color: 40/255, 40/255, 40/255, 1
            specific_text_color: 0.4, 1, 0.775, 1
            elevation: 10
            right_action_items: [["desktop-tower-monitor"], ["menu", lambda x: nav_drawer.set_state("open"), "Favorites"]]
        
        MDNavigationDrawer:
            id: nav_drawer
            anchor: 'right'
            state: 'open'
            RV:
                #: set IP '192.168.178.26'
            
            
<SofaScreen>:
    name: 'sofa'            
    RelativeLayout:
        size: root.width, root.height         
        ColorWheel:
            text: 'Sofa'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.6}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            text: '    Farbe ändern    '
            font_style: 'Button'
            font_size: '34sp'
            pos_hint: {'center_x':0.5, 'center_y':0.30}
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
            id: slider_sofa
            pos_hint: {'center_x':0.5, 'center_y':0.20}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            on_value_normalized:
            on_touch_up: 
                app.submit_brigthness(slider_sofa, '192.168.178.26')
                root.change_brightness_led(colorpicker, slider_sofa)
            
        MDIconButton:
            icon: 'home'
            user_font_size: '30sp'
            size_hint: None, None
            pos_hint: {'center_x': 0.5, 'center_y': 0.05}
            on_release: 
                root.manager.transition.direction = 'down'
                root.manager.current = 'menu'
                
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: app.theme_cls.primary_color
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.1, 'center_y':0.07}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'schreibtisch'
                
        MDIcon:
            pos_hint: {'center_x': 0.65, 'center_y': 0.04}
            icon: 'desktop-tower-monitor'
            font_size: '20sp'
            color: (1, 1, 1, 1)
                
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: app.theme_cls.primary_color
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.07}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'tv'
                
        MDIcon:
            pos_hint: {'center_x': 1.3, 'center_y': 0.04}
            icon: 'television-ambient-light'
            font_size: '20sp'
            color: (1, 1, 1, 1)
            
    AnchorLayout:
        anchor_y: 'top'
        MDToolbar:
            title: "Sofa"
            icon: 'sofa-single'
            md_bg_color: 40/255, 40/255, 40/255, 1
            specific_text_color: 0.4, 1, 0.775, 1
            elevation: 10
            right_action_items: [["sofa-single"], ["menu", lambda x: nav_drawer.set_state("open"), "Favorites"]]
        
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
    
    
<RV_all>:
    viewclass: 'Button'
    data: [{'background_normal': "", 'background_color': tuple(map(float, x.split(', '))), 'on_release': partial(root.send_fave_request_all, x)} for x in root.get_faves()]
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
