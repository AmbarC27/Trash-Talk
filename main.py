import get_user_recording
import speech_to_text
import text_model
import text_to_speech

# get recording of user speaking  
get_user_recording.getUserRecording()

# convert user speech into text
item = speech_to_text.getUserSpeechToText('out.wav')

colour = text_model.getBinColourFromText(item)

speech = "You should pick the" + colour + "bin"

text_to_speech.textToSpeech(speech)