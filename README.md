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
NMT is able to translate language to language.

NMT is using teacher forcing in the train process.

# Architecture

My architecuture is  Encoder-ecoder with attention mechanizm.
This model is created by several layers which are recurrent neural(RNN) network and word embedding layer both of them are used to by most MNT models. Usually an RNN and word embedding are used for both the encoder and decoder.
There are defferent type of RNN, a Long Short-Term Memory(LSTM) and gated reurrent unit(GRU).
In this project I used a LSTM.

![Untitled](https://user-images.githubusercontent.com/25543738/74112094-a9693c80-4b4e-11ea-8671-f725365701a7.png)


  **Embedding**
  
  Word embedding are type of word representation that is able to convert word to vector.
  After embedded word that have similar representation with word that have similar meaning.
  
  But why need a embedding?
  
  without embedding there are several problem to handle text data
  
  ・ Similarity problem

  As I mentioned after embedded word, we will have similar representation with word that have similar meaning.
  But without embedding we won't have a similar representation with each words.
  Because each word would be one-hot encoding which means each word is just defferent word even though each word has similar     meaning such as "Mother" and "Father"
  
  ・ Size problem 

  We have number of n vocaburaly, one-hot vector will have n dimentions.
  Let's say vocaburaly size is 1000000 one-hot vector will have 1000000 dimentions,
  we need a enough memory and strage otherwise we can not train model.
  Other reason is incleasing number of vocaburaly also inclease feature size vectores.
  It means there are a lot of parameter to estimate, we need more data to estimate these parameters
  if we build a good model.
  
  Word embedding able to solve those problem!
  
  
  **LSTM**
  
  Befor explane what is LSTM let me comparing basic neural network and RNN first.

  Let's say we use basic deep neural network
  there are 3 hidden layers, each hidden layer has biases and weights.
  (w1, b1), (w2, b2), (w3, b3)
  These layers are independent of each other also they don't memorize previous output.

  
  Recurrent Neural Network are type of Neural Network.
  it has memory allowing information persist.
  
  ![Untitled (3)](https://user-images.githubusercontent.com/25543738/74124555-84dd8680-4b87-11ea-8d43-0127181598d7.png)

  
  The loop is able to provide a previous information to next.
  RNN has same parameter for each input so it can reduce the complexity of parameter.
  
  But RNN has long-term dependencies problem.
  if we have a long sentence, gap is big between target word and relevent information.
  RNN unable to learn connect the information.
  
  Fortunity LSTM is able to avoid this problem.
  
  LSTM is similar with RNN
  It is desgned to avoid lomg-term dependencies problem.
  SO LSTM is able to persist long term information!
  
  As RNN has a chain of repeating module of neural network,
  this mudule has simple structure.
  It is contain a single layer such as tanh
  
  ![Untitled (4)](https://user-images.githubusercontent.com/25543738/74288775-2678eb00-4ce2-11ea-95b5-21ce20a73821.png)
  
  LSTM has also same chain structure but having a different repeating module instead of containing a single layer,
  there are able to have multiple layers.
  
  ![Untitled (8)](https://user-images.githubusercontent.com/25543738/74464230-08c59600-4e48-11ea-9f40-0847a866da6f.png)
  
  these are several gates, each geates will keep an important data in sequence or throw away if it's not important.
  
  The cell state is able to carry a relative information to next time step or even more.
  Untill cell state is gone, information is added or removed to the cell state.
  each gates are different neural network that will choose which information is important
  as I mentioned each gates are different neural network so they will learn which inormation is 
  relevent to keep or forget during training.
  
   **sigmoid**
   
   As you see the gate contains are sigmoid functions.
   sigmoid function of range of output is between 0 to 1.
   It is helpful to updata or forget data the reason is any number will get 0 if multipled by 0.
   on the other hand any number will get same number if multipled by 1 that means "try keep"
   So neural network will learn which data is important to keep or not important to foget.
   
   also we have different gates inside a LSTM
   
   **Forget gate**
   
   This gate will decide what imformation will keep or throw away.
   The information from previouse hidden state and input value are into sigmoid function.
   output value will be between 0 to 1, if closer to 0 it going to forget, however closer to 1
   it going to keep.
   
   **Input gate**
   
   The input gate recieves previous hidden state and input value, these value into sigmoid function.
   Input gata will update a value that will be between 0 or 1. 0 is not important, 1 is important.
   Also previous hidden state and input value into tahn function. this function of range of output is 
   between -1 to 1, it can help for regulation the network.
   after these section we multiple sigmoid output and tahn output.
   Then result is 1 this result is going to add to cell state as a new information however old information will gone.
   
   **Call state**
   
   Cell state has pointwise multiplication and pointwise addtion.
   After finising forget gate, there is pointwise multiplication.
   Cell state gets value which is between 0 to 1 because this value throughed a sigmoid function.
   if output value is closer to 0 dropping in the cell state.
   Then after input gate there is pointwise addition which is going to update the cell state as new relevent information.
   
   **Output gate**
   
   
   
   
   
   
   
  
  
  
  
  
  
  
  


**How NMT model works**

As I mentioned MNT model is using teacher forcing in the train process.
I provide a translation sentence into the encoder input, target sentence into the decoder input also target sentence into the decoder output(at timestep t is -1)
Model already knew what is actual value which means model will learn correct sentence quickly.

e.g.

decoder input: <START> 調子 は どう ? →　ADD　START TOKEN 

decoder output: 調子　は　どう　？ <END> →　ADD　END　TOKEN 

I give the predicted output from the previous time step as the input to decoder
The prediction will repeat until hit the <END> token or max target sequence length
  






**Dataset** : https://nlp.stanford.edu/projects/jesc/index.html

this dataset is already used sentencepiece.








