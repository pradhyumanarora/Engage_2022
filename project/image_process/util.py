
dict_of_links = {
    "Sad": "https://youtu.be/A-sfd1J8yX4",
    "Happy": "https://youtu.be/pRbxlpvXw2s",
    "Angry": "https://youtu.be/4dNIsfYdig8",
    "Disgust": "https://youtu.be/MvHVzOREGUQ",
    "Surprise": "https://youtube.com/playlist?list=PLLd27tZalu3zRpolGDrklbbS1T-L5Lc7g",
    "Fear": "https://youtu.be/Cs2Nt6Fbm14",
    "Calm": "https://youtu.be/lunFIc-8r8o",
}
def getYouTubeLinks(emotion):
    emotion = emotion.capitalize()
    return dict_of_links[emotion]

