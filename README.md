## Multi-Plaform Motion Detection App

Python GUI application apt to detect motion captured by your computer camera using openCV and PIL. When something appears at cam, app start saving pics in the script dir.

### Prerequisites

1. Install Python https://www.python.org/downloads/  (python 3)

2. Install libs:

```
pip install opencv-python
pip install pillow
```


### Run

From cli type something like:

```
python3 cv2_to_detect_motion.py 
```

*Note*: If you plan to use this app in area with natural light (day-night shiftings), you have to relaunch the script to update initial picture (via cron eg.).

### Authors

* **Ardit Sulce** - *Initial work* - Udemy (https://www.udemy.com/course/the-python-mega-course/)

See also the list of [contributors] who participated in this project.

- art3mHQ - *gui, some adjustments*
