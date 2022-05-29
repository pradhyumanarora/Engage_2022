# Engage_2022

# Setup
Clone the repository  using the command:
```
$ git clone https://github.com/pradhyumanarora/Engage_2022.git
$ cd Engage_2022
```

Create a virtual environment to install dependencies in and activate it:
```
python -m venv VIRTUAL
cd VIRTUAL
./Scripts/activate
```
Copy the folder ```project``` inside which backend and frontend folders reside and pase in VIRTUAL folder.

Then install the dependencied: 
```
cd project
pip install -r requirements.txt
```
# Activating Backend
To run backend and trained models head over to image_process.
Copy the absolute path of ```emotion_classifier.h5`` and paste in place of
```classifier = load_model(r"C:\Users\Lenovo\Desktop\Engage_2022-main\Engage_2022-main\virtual\project\image_process\emotion_classifier.h5")```

Copy the absolute path of ```haarcascade_frontalface_default.xml`` and paste in place of
```haar_cascade = cv2.CascadeClassifier("E:\VS_Code\Engage\FinalProject\Engage\project\image_process\haarcascade_frontalface_default.xml")```

To activate and run Django server run the following command:
```
python manage.py runserver
```

# Activating your frontend 
Open a new terminal and Install ```node_modules``` to run React-App
```
cd frontend
npm install
```
After Installation give :
```
npm start
``` 
to run the React Server.

Open [http://localhost:3000](http://localhost:3000) to view it in your browser.
Click on Login and you will be redirected to http://localhost:3000.
Use Capture buttom to capture your image You will be able to see your detected mood and Youtube Suggested Playlist on the WebPage.

# To Run Flask Application
In the active Virtual Environment navgate to Flask folder  and run :
```python app.py```
Open the link to see the  running application
