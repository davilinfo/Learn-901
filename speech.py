import azure.cognitiveservices.speech as speechsdk
import os

speech = speechsdk.SpeechRecognizer(
    speech_config=speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), endpoint=os.getenv("SPEECH_ENDPOINT")),
    language="en-US")

audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

synthesizer = speechsdk.SpeechSynthesizer(speech_config=speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), endpoint=os.getenv("SPEECH_ENDPOINT")), audio_config=audio_config)

text = input("Enter text to synthesize: ")

synthesis_result = synthesizer.speak_text_async(text).get()


print("Now lets test speech recognition. Please say something...")

recognizer = speechsdk.SpeechRecognizer(speech_config=speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), endpoint=os.getenv("SPEECH_ENDPOINT")), audio_config=speechsdk.audio.AudioConfig(use_default_microphone=True))

def recognized(evt):
    print(f"Recognized: {evt.result.text}")

recognizer.recognized.connect(recognized)
recognizer.recognizing.connect(lambda evt: print(f"Recognizing: {evt.result.text}"))

recognizer.start_continuous_recognition_async().get()

input("Press Enter to stop recognition...")
recognizer.stop_continuous_recognition_async().get()