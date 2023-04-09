import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[3].id) 
engine.setProperty('rate', 150) 

def talk(text):

	engine.say(text)
	engine.runAndWait()
        
def take_command():
	try:      
		with sr.Microphone() as source:
			print('listening...')
			listener.adjust_for_ambient_noise(source,duration=1)
			voice = listener.listen(source)
			command = listener.recognize_google(voice, language='en-IN')
			command=command.lower()
			#if 'alexa' in command:
				#command=command.replace('alexa','')
			print(command)
	except:
		pass
	return command

def run_alexa():
	command= take_command()
	if 'play' in command:
		song = command.replace('play', '')
		talk('playing' + song)
		pywhatkit.playonyt(song)
		  
	elif 'time' in command:
		time= datetime.datetime.now().strftime('%I:%M %p')
		talk('current time is' + time)
		print(time)
		
	elif 'get info of' in command:
		person = command.replace('alexa', '')
		info = wikipedia.summary(person,1)
		talk(info)
		print(info)		
	else:
		talk('please repeat it again')

run_alexa()
