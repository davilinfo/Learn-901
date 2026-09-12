import azure.cognitiveservices.speech as speechsdk
import os

speech = speechsdk.SpeechRecognizer(
    speech_config=speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), endpoint=os.getenv("SPEECH_ENDPOINT")),
    language="en-US")

audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

synthesizer = speechsdk.SpeechSynthesizer(speech_config=speechsdk.SpeechConfig(subscription=os.getenv("SPEECH_KEY"), endpoint=os.getenv("SPEECH_ENDPOINT")), audio_config=audio_config)

text = input("Enter text to synthesize: ")

synthesis_result = synthesizer.speak_text_async(text).get()
