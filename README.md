# voice_translation_project


# Overview

Nowadays there are more than 6000 spoken languages in the world.
In fact we can't understand all of them, but we must involve with people who speak different language
because the society is growing globally.

Specifically We must understand the detail of sentences properly when we chat with other people
Also we know that learning different languages are needed a lot of time.

Deep learning is a powerful technique that can be used to solve this problem.
I am using NLP for text transaltion and CNN for speech recognition.

In this project, try to translate English speech to japanese speech.
Users are able to chat with Japanese speakers easily.
you can just speack your native languages (English)
you don’t need to spend time to use a dictionary to translate your language.

# Neural Machine Translation

I am using seq2seq model which is usually usu for machine translation, speech recognition and text summarization.

**Architecture**

My architecuture is  Encoder-ecoder with attention mechanizm.
This model is created by several layers which are recurrent neural(RNN) network and word embedding layer both of them are used to by most MNT models. Usually an RNN and word embedding are used for both the encoder and decoder.
There are defferent type of RNN, a Long Short-term Memory(LSTM) and gated reurrent unit(GRU).
In this project I used a LSTM







**Dataset** : https://nlp.stanford.edu/projects/jesc/index.html

this dataset is already used sentencepiece.








