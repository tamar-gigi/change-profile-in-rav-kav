import os
from flask import Flask, request, json
from flask_cors import CORS
import sys
import asyncio
from myProject.files.saveFiles import saveFiles
from myProject.cropLocation.cropLocation import startRun
from myProject.searchAndAnswer.searchAndAnswer import searchAndAnswer

app = Flask(__name__)
CORS(app)
if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


def deleteFolder():
    for di in os.listdir(f'myProject/cropLocation/imgCrop'):
        for deli in os.listdir(f'myProject/cropLocation/imgCrop/{di}'):
            if os.path.isfile(f'myProject/cropLocation/imgCrop/{di}/{deli}'):
                os.remove(f'myProject/cropLocation/imgCrop/{di}/{deli}')
    for df in os.listdir(f'myProject/files/file'):
        if os.path.isfile(f'myProject/files/file/{df}'):
            os.remove(f'myProject/files/file/{df}')


i = 0


@app.route('/upload-images', methods=['POST'])
def uploadImages():
    global i

    idCard = request.files['idCard']
    studentPermit = request.files['studentPermit']
    studentCard = request.files['studentCard']
    ravKav = request.files['ravKav']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    idNumber = request.form['idNumber']

    files1 = [idCard, studentPermit, studentCard, ravKav]
    i += 1
    # saves the received files as an image
    files = saveFiles(files1, i)
    # sends to processing functions for model
    strFiles = startRun(files)
    # sends for testing and comparison functions
    answer = searchAndAnswer(strFiles, firstName, lastName, idNumber)
    # delete folder
    deleteFolder()

    return json.dumps(answer)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
