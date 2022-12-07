## About

This is a **proof of concept** for a barebones version of a Speech Assistant ("Ok Google", "Alexa" etc.) powered by GPT-3

Currently it works in a very simple way: It listens the microphone for 5 seconds after being run and then uses that snippet to query OpenAI's API, returning the result as speech

I covered the potential applications and risks of such an application in a blogpost that can be found [here](https://github.com/thevinter/okgpt)

## Installation and Usage

For the application to work you will need to get and use your own API key from [OpenAI's Beta](https://beta.openai.com/account/api-keys)

Once you have it, substitute `<API_KEY>` with your own key and then run the program like this

```
pip install -r requirements.txt
python okgpt.py
```
