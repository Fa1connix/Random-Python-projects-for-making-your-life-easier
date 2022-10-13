import keyboard
import speech_recognition
import pyaudio
import pyttsx3

file='C:/Users/the user/Documents/my_notes.txt' #You will need to replace the path with the appropriate path to the text file with / instead of \
with open(file, 'a') as file:
	file.write('\n')
	file.write('NEW CLASS!')

recognizer=speech_recognition.Recognizer()

while not keyboard.is_pressed('F10'): # Change F10 to whatever stop key you want 

	try:
		with speech_recognition.Microphone() as mic:
			recognizer.adjust_for_ambient_noise(mic, duration=0.2)
			audio=recognizer.listen(mic)

			text=recognizer.recognize_google(audio)
			text=text.lower()
			
			with open(file,'a') as file:
				file.write('\n') 
				file.write(text)
				

	except speech_recognition.UnknownValueError:
		recognizer=speech_recognition.Recognizer()
		continue 



