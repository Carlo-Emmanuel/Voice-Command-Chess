import speech_recognition as sr
import pyaudio
import wave
import random
import time

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occurred, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) #uses 0.5 second of input to adjust to current noise level
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Input a chess move")
    #with mic as source:
    try:
        chessMove = recognize_speech_from_mic(recognizer, mic)
        print('Input done')
    except Exception:
        print("Something went wrong")

    # show the user the transcription
    print("You said: {}".format(chessMove["transcription"]))
    result =  "{}".format(chessMove)
    resultList = chessMove['transcription'].split(' ')
    print(resultList)

    #move piece from letter1 number1 to letter2 number2
    piece = resultList[0]
    pos1 = resultList[2]
    pos2 = resultList[4]

    print('piece:', piece)
    print('start position:', pos1)
    print('end position:', pos2)