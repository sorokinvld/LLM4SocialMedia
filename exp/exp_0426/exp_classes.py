import md_classes
import pl_classes

from pl_classes import TikTok, Youtube, Snap, Instagram
from md_classes import Llava, Gemini, GPT4
import time
import pyautogui

class Bot:
    def __init__(self, interest, platform, model):
        self.interest = interest
        self.platform = platform  # Assuming TikTok class is defined elsewhere
        self.model = model      # Model object with a simple_strategy method

    def open_platform(self):
        self.platform.open_and_position_browser()

    def experiment(self, n):
        self.open_platform()
        for i in range(n):
            screen_shot_name = pl_classes.take_screen_shot(self.platform)
            print(f"{i}th loop, captured {i + 1} picture")
            
            decision = self.model.simple_strategy(screen_shot_name, self.interest)
            if "yes" in decision.lower():
                print(f'{self.model.name} decides to stay on this content...\n')
                time.sleep(30)
            else:
                print(f'Scrolling down to new content...')
            
            pyautogui.press('down')
            time.sleep(1)

    @staticmethod
    def run_experiment(interest, platform, model, n):
        bot = Bot(interest,platform, model)
        bot.experiment(n)

class Spatial_Bot:
    def __init__(self, interest, platform, model):
        self.interest = interest
        self.platform = platform  # Assuming TikTok class is defined elsewhere
        self.model = model      # Model object with a simple_strategy method

    def open_platform(self):
        self.platform.open_and_position_browser()

    def experiment(self, n):
        success = 0
        self.open_platform()
        categories = set(self.model.ask_general(self.interest))
        
        for i in range(n):
            screen_shot_name = pl_classes.take_screen_shot(self.platform)
            print(f"{i+1}'th loop, taken {i+1} picture")
            category = self.model.spacial_strategy(screen_shot_name, self.interest, *categories)

            if any(cat.lower() in category.lower() for cat in categories):
                print(f"{category} presented, stay for 10s")
                time.sleep(10)
                pyautogui.press('down')
                time.sleep(1)
            elif self.interest in category.lower():                           
                print(f"{category} presented, stay for 30s")
                time.sleep(30)
                pyautogui.press("down")
                time.sleep(1)
                success += 1
            else:
                pyautogui.press("down")
                time.sleep(1)

            if i >= 10:
                success_rate = success / (i + 1)
                if success_rate > 0.3:
                    print(f"{category} presented, stay for 5s")
                    time.sleep(5)
                if success_rate > 0.5:
                    pyautogui.press('down')
                    time.sleep(1)
                else:
                    print(f"{category} presented, stay for 10s")
                    time.sleep(10)
                    pyautogui.press('down')
                    time.sleep(1)
    def run_experiment(interest, platform, model, n):
        bot = Spatial_Bot(interest,platform, model)
        bot.experiment(n)
# class Spacial_Bot:
#     def __init__(self, interest, platform, model):
#         self.interest = interest
#         self.platform = platform  # Assuming TikTok class is defined elsewhere
#         self.model = model      # Model object with a simple_strategy method

#     def open_platform(self):
#         self.platform.open_and_position_browser()

#     def experiment(self, n):
#         success = 0
#         self.open_platform()
#         cate1, cate2, cate3, cate4, cate4, cate5 = self.platform.ask_general()
#         categories = [cate1, cate2, cate3, cate4, cate5]
#         for i in range(n):
#             if i<10:
#                 screen_shot_name = pl_classes.take_screen_shot(self.platform)
#                 print(f"{i}'th loop, taken {i+1} picture")
#                 category = self.model.spacial_strategy(screen_shot_name, self.interest, cate1, cate2, cate3, cate4, cate4, cate5)
#                 if any(cat.lower() in category.lower() for cat in categories):
#                     print(f"{category} presented, stay for 10s")
#                     time.sleep(10)
#                     pyautogui.press('down')
#                     time.sleep(1.5)
#                 elif self.interest in category.lower():                           
#                     print(f"{category} presented, stay for 30s")
#                     time.sleep(30)
#                     pyautogui.press("down")
#                     time.sleep(1.5)
#                     success+=1
#                 else:
#                     pyautogui.press("down")
#                     time.sleep(1.5)
#             else:
#                 screen_shot_name = pl_classes.take_screen_shot(tiktok)
#                 print(f"{i}'th loop, taken {i+1} picture")
#                 category = self.model.spacial_strategy(screen_shot_name, self.interest, cate1, cate2, cate3, cate4, cate4, cate5)
#                 if any(cat.lower() in category.lower() for cat in categories):
#                     success_rate = success/i
#                     if success_rate > 0.3:
#                             print(f"{category} presented, stay for 5s")
#                             time.sleep(5)
#                             pyautogui.press('down')
#                             time.sleep(1.5)
#                     if success_rate >0.5:
#                             pyautogui.press('down')
#                             time.sleep(1.5)
#                     else:
#                             print(f"{category} presented, stay for 10s")
#                             time.sleep(10)
#                             pyautogui.press('down')
#                             time.sleep(1.5)
                    
#                 elif self.interest in category.lower():
#                     print(f"{category} presented, stay for 30s")
#                     time.sleep(30)
#                     pyautogui.press("down")
#                     time.sleep(1.5)
#                     success+=1
#                 else:
#                     pyautogui.press("down")
#                     time.sleep(1.5)
            