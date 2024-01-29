# DORA The Voice Assitant

DORA is a very useful voice assistant which enables the desktop users to open the desktop applications easily, to make a note of important things, to relax themselves by asking 
DORA to play songs, tell jokes etc. With the increasing demand for ease of work and more efficiency, there is a need for a technology which can reduce human efforts. 
Artificial Intelligence and Machine Learning with the use of NLP have helped to achieve this. Voice assistants are used nowadays to automate almost all tasks in order to be stress free. 
Voice-based assistants are user-friendly and task-oriented, creating a more effective and enjoyable experience. 
Voice Based Virtual Assistant helps us to have a dialog with a voice interface which could create interactions that improves the user experience through their simplicity. 


The implementation detail is given in this section.
The overall system design consists of following phases:
(a) Data collection in the form of speech.
(b) Voice analysis and conversion to text
(c) Execution of Python script
(d) Generating speech from the processed text output

In the first phase, the data is collected in the form of speech through a microphone and stored as an input for the next phase for processing. The voice commands are recognized through 
google Speech Recognition module which has the ability to recognize a word or phrase and convert them into machine language. In the second phase, the input voice is continuously 
processed using the recognize_google function to convert the input Speech to text. In the next phase the converted text is analysed and processed using Python Script to identify 
the response to be given for the command by matching with keywords. Finally once the response is identified, output is generated from simple text to speech conversion using the gtts 
module and response is given through the speaker.

## Screenshots of the Voice Assistant
![1](https://github.com/sakshiisinghh/DORA-VoiceAssistant/assets/87891878/c659ca5f-7430-473a-8b4a-3461c3dfcffc)



![2](https://github.com/sakshiisinghh/DORA-VoiceAssistant/assets/87891878/d68911e5-26df-4627-96d3-6af685c67c3d)



![3](https://github.com/sakshiisinghh/DORA-VoiceAssistant/assets/87891878/80dc997b-c503-41f6-9f88-3ae9c3a4ff6a)



![4](https://github.com/sakshiisinghh/DORA-VoiceAssistant/assets/87891878/7c01d283-cebc-49bb-b0af-17cc8fa5f519)



![5](https://github.com/sakshiisinghh/DORA-VoiceAssistant/assets/87891878/eef8a993-90ce-4516-b12b-27a86adfa061)



![6](https://github.com/sakshiisinghh/DORA-VoiceAssistant/assets/87891878/dcbe7f83-167c-4b45-bfdf-23420887880e)



![7](https://github.com/sakshiisinghh/DORA-VoiceAssistant/assets/87891878/25da1aaf-b74c-4dfc-a0de-180c7eddd4a5)
