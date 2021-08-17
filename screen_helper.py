screenHelper = """
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
#: import OneLineListItem kivymd.uix.list.OneLineListItem
#: import ContainerSupport kivymd.uix.list.ContainerSupport
#: import partial functools.partial

ScreenManager:
    MenuScreen:
    WohnzimmerScreen:
    SchlafzimmerScreen:
    KuecheScreen:
    Faves_Wohnzimmer:
    Faves_Schlafzimmer:
    Faves_Kueche:
    
    
<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: 'LED Controller'
        pos_hint: {'center_x':0.7, 'center_y':0.57}
        font_style: 'Button'
        font_size: 30

    BoxLayout:
        orientation: 'vertical'
        spacing: 10

        MDIcon:
            icon: 'led-strip-variant'
            font_size: '170sp'
            halign: 'center' 
            
        MDBottomNavigation:
            panel_color: (56/255, 56/255, 56/255, 1)
    
            MDBottomNavigationItem:
                name: 'menu'
                text: 'Home'
                icon: 'home'
                halign: 'center'
                on_tab_release: 
                    root.manager.transition.direction = 'down'
                    root.manager.current = 'menu'
    
            MDBottomNavigationItem:
                name: 'schlafzimmer'
                text: 'Schlafzimmer'
                icon: 'bed'
                on_tab_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'schlafzimmer'
    
            MDBottomNavigationItem:
                name: 'kueche'
                text: 'Küche'
                icon: 'silverware-fork-knife'
                on_tab_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'kueche'
    
            MDBottomNavigationItem:
                name: 'wohnzimmer'
                text: 'Wohnzimmer'
                icon: 'television'
                on_tab_release: 
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'wohnzimmer'
        


<WohnzimmerScreen>:
    name: 'wohnzimmer'
    RelativeLayout                
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.9}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'faves_wohnzimmer'
                
        MDIcon:        
            icon: 'heart'
            font_size: '25'
            pos_hint: {'center_x':1.32, 'center_y':0.87}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
    
        MDIcon:
            pos_hint: {'center_x': 0.93, 'center_y': 0.90}
            icon: 'television'
            font_size: '45sp'
            color: (255/255, 214/255, 0, 1)
    
        MDLabel:
            text: 'Wohnzimmer'
            font_style: 'Button'
            font_size: 28
            size_hint: 0.5, 0.1
            pos_hint: {'center_x':0.5, 'center_y':0.96}
    
        ColorWheel:
            text: 'Wohnzimmer'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.57}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            text: 'Farbe ändern'
            font_style: 'Button'
            font_size: 24
            pos_hint: {'center_x':0.556, 'center_y':0.25}
            on_release: app.submit_color(colorpicker, '192.168.178.26')
            
        MDIconButton:
            icon: 'heart'
            font_size: '15'
            pos_hint: {'center_x':0.265, 'center_y':0.21}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
            on_release: app.set_faves(color_label)
    
        MDIcon:
            icon: 'led-on'
            pos_hint: {'center_x':0.665, 'center_y':0.25}
            font_size: '45sp'
            id: color_label  
            
        Slider:
            id: slider_wohnzimmer
            pos_hint: {'center_x':0.5, 'center_y':0.15}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            cursor_image: 'Slider.png'
            on_touch_up: 
                app.submit_brigthness(slider_wohnzimmer, '192.168.178.26')
                root.change_brightness_led(colorpicker, slider_wohnzimmer)
                
        MDIconButton:
            icon: 'home'
            user_font_size: '60'
            pos_hint: {'center_x': 0.5, 'center_y': 0.07}
            on_release: 
                root.manager.transition.direction = 'down'
                root.manager.current = 'menu'
                
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.1, 'center_y':0.07}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'kueche'
                
        MDIcon:
            pos_hint: {'center_x': 0.65, 'center_y': 0.04}
            icon: 'silverware-fork-knife'
            font_size: '20sp'
            color: (1, 1, 1, 1)
            

<SchlafzimmerScreen>:
    name: 'schlafzimmer'
    RelativeLayout
        size: root.width, root.height
                
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.9}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'faves_schlafzimmer'
                
        MDIcon:        
            icon: 'heart'
            font_size: '25'
            pos_hint: {'center_x':1.32, 'center_y':0.87}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
    
        MDIcon:
            pos_hint: {'center_x': 0.93, 'center_y': 0.90}
            icon: 'bed'
            font_size: '45sp'
            color: (255/255, 214/255, 0, 1)
    
        MDLabel:
            text: 'Schlafzimmer'
            font_style: 'Button'
            font_size: 26
            size_hint: 0.5, 0.1
            pos_hint: {'center_x':0.5, 'center_y':0.96}
    
        ColorWheel:
            text: 'Schlafzimmer'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.57}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            text: 'Farbe ändern'
            font_style: 'Button'
            font_size: 24
            pos_hint: {'center_x':0.556, 'center_y':0.25}
            on_release: app.submit_color(colorpicker, '192.168.178.26')
            
        MDIconButton:
            icon: 'heart'
            font_size: '15'
            pos_hint: {'center_x':0.265, 'center_y':0.21}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
            on_release: app.set_faves(color_label)
    
        MDIcon:
            icon: 'led-on'
            pos_hint: {'center_x':0.665, 'center_y':0.25}
            font_size: '45sp'
            id: color_label  
            
        Slider:
            id: slider_schlafzimmer
            pos_hint: {'center_x':0.5, 'center_y':0.15}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            cursor_image: 'Slider.png'
            on_touch_up: 
                app.submit_brigthness(slider_schlafzimmer, '192.168.178.26')
                root.change_brightness_led(colorpicker, slider_schlafzimmer)
                
        MDIconButton:
            icon: 'home'
            user_font_size: '60'
            pos_hint: {'center_x': 0.5, 'center_y': 0.07}
            on_release: 
                root.manager.transition.direction = 'down'
                root.manager.current = 'menu'
                
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.07}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'kueche'
                
        MDIcon:
            pos_hint: {'center_x': 1.3, 'center_y': 0.04}
            icon: 'silverware-fork-knife'
            font_size: '20sp'
            color: (1, 1, 1, 1)
            
            
<KuecheScreen>:
    name: 'kueche'
    RelativeLayout
        size: root.width, root.height
                
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.9}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'faves_kueche'
        
        MDIcon:        
            icon: 'heart'
            font_size: '25'
            pos_hint: {'center_x':1.32, 'center_y':0.87}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
    
        MDIcon:
            pos_hint: {'center_x': 0.93, 'center_y': 0.90}
            icon: 'silverware-fork-knife'
            font_size: '45sp'
            color: (255/255, 214/255, 0, 1)
    
        MDLabel:
            text: 'Küche'
            font_style: 'Button'
            font_size: 28
            size_hint: 0.5, 0.1
            pos_hint: {'center_x':0.624, 'center_y':0.96}
    
        ColorWheel:
            text: 'Küche'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.57}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            text: 'Farbe ändern'
            font_style: 'Button'
            font_size: 24
            pos_hint: {'center_x':0.556, 'center_y':0.25}
            on_release: app.submit_color(colorpicker, '192.168.178.26')
            
        MDIconButton:
            icon: 'heart'
            font_size: '15'
            pos_hint: {'center_x':0.265, 'center_y':0.21}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
            on_release: app.set_faves(color_label)
    
        MDIcon:
            icon: 'led-on'
            pos_hint: {'center_x':0.665, 'center_y':0.25}
            font_size: '45sp'
            id: color_label  
            
        Slider:
            id: slider_kueche
            pos_hint: {'center_x':0.5, 'center_y':0.15}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            cursor_image: 'Slider.png'
            on_touch_up: 
                app.submit_brigthness(slider_kueche, '192.168.178.26')
                root.change_brightness_led(colorpicker, slider_kueche)
            
        MDIconButton:
            icon: 'home'
            user_font_size: '60'
            pos_hint: {'center_x': 0.5, 'center_y': 0.07}
            on_release: 
                root.manager.transition.direction = 'down'
                root.manager.current = 'menu'
                
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.1, 'center_y':0.07}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'schlafzimmer'
                
        MDIcon:
            pos_hint: {'center_x': 0.65, 'center_y': 0.04}
            icon: 'bed'
            font_size: '20sp'
            color: (1, 1, 1, 1)
                
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.07}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'wohnzimmer'
                
        MDIcon:
            pos_hint: {'center_x': 1.3, 'center_y': 0.04}
            icon: 'television'
            font_size: '20sp'
            color: (1, 1, 1, 1)
                
        
                
                
<Faves_Wohnzimmer>:
    name: 'faves_wohnzimmer'

    BoxLayout:
        orientation: 'vertical'
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'wohnzimmer'
        
        MDLabel:
            text: 'Favoriten'
            font_style: 'Button'
            font_size: 35
            size_hint: 0.8, 0.1
            pos_hint: {'center_x':0.66, 'center_y':0.94} 
                    
        RV:
            #: set IP '192.168.178.26'
        

<Faves_Schlafzimmer>:
    name: 'faves_schlafzimmer'
            
    BoxLayout:
        orientation: 'vertical'
        
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'schlafzimmer'
        
        MDLabel:
            text: 'Favoriten'
            font_style: 'Button'
            font_size: 35
            size_hint: 0.8, 0.1
            pos_hint: {'center_x':0.66, 'center_y':0.94}
            
        RV:
            #: set IP '192.168.178.26'
        
            
<Faves_Kueche>:
    name: 'faves_kueche'
    
    BoxLayout:
        orientation: 'vertical'
        
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'kueche'            
        
        MDLabel:
            text: 'Favoriten'
            font_style: 'Button'
            font_size: 35
            size_hint: 0.8, 0.1
            pos_hint: {'center_x':0.66, 'center_y':0.94}
                    
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
