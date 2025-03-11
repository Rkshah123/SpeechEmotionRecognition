import numpy as np
import librosa
from tensorflow import keras
import webbrowser


def make_predictions(file):
    cnn_model = keras.models.load_model(
        "models/cnn_model.h5"
    )
    lstm_model = keras.models.load_model(
        "models/lstm_model.h5"
    )
    prediction_data, prediction_sr = librosa.load(
        file,
        res_type="kaiser_fast",
        duration=3,
        sr=22050,
        offset=0.5,
    )

    mfccs = np.mean(
        librosa.feature.mfcc(y=prediction_data, sr=prediction_sr, n_mfcc=40).T, axis=0
    )
    x = np.expand_dims(mfccs, axis=1)
    x = np.expand_dims(x, axis=0)
    predictions = lstm_model.predict_classes(x)

    emotions_dict = {
        "0": "neutral",
        "1": "calm",
        "2": "happy",
        "3": "sad",
        "4": "angry",
        "5": "fearful",
        "6": "disgusted",
        "7": "surprised",
    }

    for key, value in emotions_dict.items():
        if int(key) == predictions:
            label = value

    print("This voice sounds", predictions, label)
    
    print("Do you want to see video of your emotion.!")
    choice = input('Type YES or NO in Capital --  ')
    
    if choice=='YES':
        
        if label == 'neutral':
            print("Wait .! We are searching a video for your emotion.!")
            url = 'https://www.youtube.com/watch?v=kRauhbZqJCY'
            webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
            webbrowser.get('chrome').open(url)
            
        elif label == 'calm':
            print("Wait .! We are searching a video for your emotion.!")
            url = 'https://www.youtube.com/watch?v=Zljg2ptExHc'
            webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
            webbrowser.get('chrome').open(url)
        
        elif label == 'happy':
            print("Wait .! We are searching a video for your emotion.!")
            url = 'https://www.youtube.com/watch?v=srYPJYgDaj8'
            webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
            webbrowser.get('chrome').open(url)
            
        elif label == 'sad':
            print("Wait .! We are searching a video for your emotion.!")
            url = 'https://www.youtube.com/watch?v=EvDQBIisG7c'
            webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
            webbrowser.get('chrome').open(url)
            
        elif label == 'angry':
            print("Wait .! We are searching a video for your emotion.!")
            url = 'https://www.youtube.com/watch?v=7D3zpOBRN9c'
            webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
            webbrowser.get('chrome').open(url)
            
        elif label == 'fearful':
            print("Wait .! We are searching a video for your emotion.!")
            url = 'https://www.youtube.com/watch?v=fcLl-DZGLZ8'
            webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
            webbrowser.get('chrome').open(url)
         
        elif label == 'disgusted':
            print("Wait .! We are searching a video for your emotion.!")
            url = 'https://www.youtube.com/watch?v=UM7ydNEK68w'
            webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
            webbrowser.get('chrome').open(url)
        
        else :
            print("Wait .! We are searching a video for your emotion.!")
            url = 'https://www.youtube.com/watch?v=JNQU-4YEnm4'
            webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
            webbrowser.get('chrome').open(url)
        
    else :
        print("Ok Bye.!")
    
if __name__ == "__main__":
    work_rec = "recordings/findahappyplace.wav"
    make_predictions(file=work_rec)