# FleetCommandBot
Shitty bot for Star Trek Fleet Command

Capabilities:
- Collect base resources
- Collect timed reward crates
- Upgrade buildings (disabled - no handling for lack of resources yet)
- Do research (disabled - can't differentiate between orange 'Go' buttons yet)
- Ask for help
- Provide help

How-to:
- Mirror client to PC
- Replace images in /images/ folder with your own screenshots (use Windows rectangular snipping tool). Why? your resolution/colors/scaling might be different to mine, and the code might not find the elements on your screen.  
- The pyautogui library will try finding on your screen the elements you screenshotted.
- Run main.py

Tips:
- When running be careful to only run a single instance at a time.
- If you change the file names, also change the references in the code
- If it's having trouble locating the images in the correct spot, or can't find them at all, take another screenshot of the element and try playing with the confidence values in the code
- The element's background matters if it's translucent, like for the timed rewards button. Try putting your location in the same spot as when you're taking the screenshot of the element
- If it doesn't work, it's because I hardcoded everything
- If your device is too slow, increase the sleep values in the code
