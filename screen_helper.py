screenHelper = """
#: import SlideTransition kivy.uix.screenmanager.SlideTransition
#: import partial functools.partial

ScreenManager:
    MenuScreen:
    TVScreen:
    SchreibtischScreen:
    SofaScreen:
    ControllAll:
    Faves_TV:
    Faves_Schreibtisch:
    Faves_Sofa:
    Faves_All:
    
    
<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: 'LED Controller'
        halign: 'center'
        pos_hint: {'center_y':0.85}
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
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.94}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'faves_all'
    
        MDIcon:
            halign: 'center'
            pos_hint: {'center_y': 0.90}
            icon: 'home-assistant'
            font_size: '45sp'
            color: (255/255, 214/255, 0, 1)
    
        MDLabel:
            text: "Alle LED's"
            font_style: 'Button'
            font_size: '36sp'
            halign: 'center'
            pos_hint: {'center_y':0.96}
    
        ColorWheel:
            text: 'Sofa'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.6}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            text: '      Farbe ändern      '
            font_style: 'Button'
            font_size: '34sp'
            pos_hint: {'center_x':0.5, 'center_y':0.28}
            on_release: app.submit_color_all(colorpicker)
            
        MDIconButton:
            icon: 'heart'
            user_font_size: '30sp'
            pos_hint: {'center_x':0.265, 'center_y':0.9}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
            on_release: app.set_faves(color_label)
    
        MDIcon:
            icon: 'led-on'
            pos_hint: {'center_x':0.665, 'center_y':0.85}
            font_size: '45sp'
            id: color_label  
            
        Slider:
            id: slider_all
            pos_hint: {'center_x':0.5, 'center_y':0.18}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            cursor_image: 'Slider.png'
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
            user_font_size: '50sp'
            size_hint: None, None
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
                root.manager.current = 'schreibtisch'
                
        MDIcon:
            pos_hint: {'center_x': 1.3, 'center_y': 0.04}
            icon: 'sofa-single'
            font_size: '20sp'
            color: (1, 1, 1, 1)
        

<TVScreen>:
    name: 'tv'
    RelativeLayout: 
        size: root.width, root.height              
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.94}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'faves_tv'
    
        MDLabel:
            halign: 'center'
            pos_hint: {'center_y':0.96}
            text: 'Fernseher'
            font_style: 'Button'
            font_size: '36sp'
    
        MDIcon:
            halign: 'center'
            pos_hint: {'center_y': 0.90}
            icon: 'television-ambient-light'
            font_size: '45sp'
            color: (255/255, 214/255, 0, 1)
    
        ColorWheel:
            text: 'Fernseher'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.6}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            pos_hint: {'center_x':0.5, 'center_y':0.28}
            text: '      Farbe ändern      '
            font_style: 'Button'
            font_size: '34sp'
            on_release: app.submit_color(colorpicker, '192.168.178.26')
            
        MDIconButton:
            icon: 'heart'
            user_font_size: '30sp'
            pos_hint: {'center_x':0.265, 'center_y':0.9}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
            on_release: app.set_faves(color_label)
    
        MDIcon:
            icon: 'led-on'
            pos_hint: {'center_x':0.665, 'center_y':0.85}
            font_size: '45sp'
            id: color_label  
            
        Slider:
            id: slider_tv
            pos_hint: {'center_x':0.5, 'center_y':0.18}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            cursor_image: 'Slider.png'
            on_touch_up: 
                app.submit_brigthness(slider_tv, '192.168.178.26')
                root.change_brightness_led(colorpicker, slider_tv)
                
        MDIconButton:
            icon: 'home'
            size_hint: None, None
            user_font_size: '50sp'
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
                root.manager.current = 'sofa'
                
        MDIcon:
            pos_hint: {'center_x': 0.65, 'center_y': 0.04}
            icon: 'sofa-single'
            font_size: '20sp'
            color: (1, 1, 1, 1)
            

<SchreibtischScreen>:
    name: 'schreibtisch'
    RelativeLayout:
        size: root.width, root.height
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.94}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'faves_schreibtisch'
    
        MDIcon:
            halign: 'center'
            pos_hint: {'center_y': 0.90}
            icon: 'desktop-tower-monitor'
            font_size: '45sp'
            color: (255/255, 214/255, 0, 1)
    
        MDLabel:
            text: 'Schreibtisch'
            font_style: 'Button'
            font_size: '36sp'
            halign: 'center'
            pos_hint: {'center_y':0.96}
    
        ColorWheel:
            text: 'Schreibtisch'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.6}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            text: '      Farbe ändern      '
            font_style: 'Button'
            font_size: '34sp'
            pos_hint: {'center_x':0.5, 'center_y':0.28}
            on_release: app.submit_color(colorpicker, '192.168.178.26')
            
        MDIconButton:
            icon: 'heart'
            user_font_size: '30sp'
            pos_hint: {'center_x':0.265, 'center_y':0.9}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
            on_release: app.set_faves(color_label)
    
        MDIcon:
            icon: 'led-on'
            pos_hint: {'center_x':0.665, 'center_y':0.85}
            font_size: '45sp'
            id: color_label  
            
        Slider:
            id: slider_schreibtisch
            pos_hint: {'center_x':0.5, 'center_y':0.18}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            cursor_image: 'Slider.png'
            on_touch_up: 
                app.submit_brigthness(slider_schreibtisch, '192.168.178.26')
                root.change_brightness_led(colorpicker, slider_schreibtisch)
                
        MDIconButton:
            icon: 'home'
            size_hint: None, None
            user_font_size: '50sp'
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
                root.manager.current = 'sofa'
                
        MDIcon:
            pos_hint: {'center_x': 1.3, 'center_y': 0.04}
            icon: 'sofa-single'
            font_size: '20sp'
            color: (1, 1, 1, 1)
            
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
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
            
            
<SofaScreen>:
    name: 'sofa'
    RelativeLayout:
        size: root.width, root.height   
        MDIconButton:
            icon: 'arrow-right-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.9, 'center_y':0.94}
            on_release: 
                root.manager.transition.direction = 'left'
                root.manager.current = 'faves_sofa'
    
        MDIcon:
            halign: 'center'
            pos_hint: {'center_y': 0.90}
            icon: 'sofa-single'
            font_size: '45sp'
            color: (255/255, 214/255, 0, 1)
    
        MDLabel:
            text: 'Sofa'
            font_style: 'Button'
            font_size: '36sp'
            halign: 'center'
            pos_hint: {'center_y':0.96}
    
        ColorWheel:
            text: 'Sofa'
            id: colorpicker
            size_hint: 0.8, 0.8
            pos_hint: {'center_x': 0.5, 'center_y':0.6}
            on_touch_up: root.change_color(colorpicker)
            
        MDRectangleFlatButton:
            text: '      Farbe ändern      '
            font_style: 'Button'
            font_size: '34sp'
            pos_hint: {'center_x':0.5, 'center_y':0.28}
            on_release: app.submit_color(colorpicker, '192.168.178.26')
            
        MDIconButton:
            icon: 'heart'
            user_font_size: '30sp'
            pos_hint: {'center_x':0.265, 'center_y':0.9}
            text_color: (255/255, 15/255, 99/255, 1)
            theme_text_color: 'Custom'
            on_release: app.set_faves(color_label)
    
        MDIcon:
            icon: 'led-on'
            pos_hint: {'center_x':0.665, 'center_y':0.85}
            font_size: '45sp'
            id: color_label  
            
        Slider:
            id: slider_sofa
            pos_hint: {'center_x':0.5, 'center_y':0.18}
            size_hint: 0.7, 0.1
            min: 0
            max: 255
            step: 5
            value: 255
            orientation: 'horizontal'
            cursor_image: 'Slider.png'
            on_touch_up: 
                app.submit_brigthness(slider_sofa, '192.168.178.26')
                root.change_brightness_led(colorpicker, slider_sofa)
            
        MDIconButton:
            icon: 'home'
            size_hint: None, None
            user_font_size: '50sp'
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
                root.manager.current = 'schreibtisch'
                
        MDIcon:
            pos_hint: {'center_x': 0.65, 'center_y': 0.04}
            icon: 'desktop-tower-monitor'
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
                root.manager.current = 'tv'
                
        MDIcon:
            pos_hint: {'center_x': 1.3, 'center_y': 0.04}
            icon: 'television-ambient-light'
            font_size: '20sp'
            color: (1, 1, 1, 1)
                
            
<Faves_TV>:
    name: 'faves_tv'

    BoxLayout:
        orientation: 'vertical'
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.1, 'center_y':0.5}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'tv'
                    
        RV:
            #: set IP '192.168.178.26'
        

<Faves_Schreibtisch>:
    name: 'faves_schreibtisch'
            
    BoxLayout:
        orientation: 'vertical'
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.1, 'center_y':0.5}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'schreibtisch'
            
        RV:
            #: set IP '192.168.178.26'
        
            
<Faves_Sofa>:
    name: 'faves_sofa'
    
    BoxLayout:
        orientation: 'vertical'
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.1, 'center_y':0.5}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'sofa'            
                    
        RV:
            #: set IP '192.168.178.26'
            
<Faves_All>:
    name: 'faves_all'
    
    BoxLayout:
        orientation: 'vertical'
        MDIconButton:
            icon: 'arrow-left-bold-box'
            user_font_size: '45sp'
            text_color: (255/255, 198/255, 0/255, 1)
            theme_text_color: 'Custom'
            pos_hint: {'center_x':0.1, 'center_y':0.5}
            on_release: 
                root.manager.transition.direction = 'right'
                root.manager.current = 'controllAll'            
                    
        RV_all:
            
            
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
