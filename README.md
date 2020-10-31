# Chatting Transformer

<div align="center">
  <img src="assets/vennify_ai_logo.jpg" height="200">
</div>

### Easy text generation using state of the art NLP models.
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Downloads](https://pepy.tech/badge/chattingtransformer)](https://pepy.tech/project/chattingtransformer)

Chatting Transformer is a Python library for generating text using GPT2. GPT-2 is a language model that was developed by OpenAI that specializes in generating text. By using Chatting Transformer, you can implement and use this model with just two lines of code. 

## Installation

```bash
pip install chattingtransformer
```

## Basic Usage

```python
from chattingtransformer import ChattingGPT2


model_name = "gpt2" 
gpt2 = ChattingGPT2(model_name)

text = "In 10 years, AI will " 
result = gpt2.generate_text(text) 

print(result) # Outputs: In 10 years, AI will  have revolutionized the way we interact with the world...
```
## Available Models
| Model         | Parameters   |      Size        | 
|------------------------------|------------------|-----------------|
| gpt2         |      134 M    |      548  MB     | 
| gpt2-medium  |      335 M    |      1.52 GB     | 
| gpt2-large   |      774 M    |      3.25 GB     | 
| gpt2-xl      |      1.5 B    |      6.43 GB     |      


```python
from chattingtransformer import ChattingGPT2

gpt2 = ChattingGPT2("gpt2")
gpt2_medium = ChattingGPT2("gpt2-medium")
gpt2_large = ChattingGPT2("gpt2-large")
gpt2_xl = ChattingGPT2("gpt2-xl")
```

## Predefined Methods

Below are predfined methods that may be used to determine the output. 
To learn more, about these methods, please visit this [webpage](https://huggingface.co/blog/how-to-generate).

1. "greedy"
2. "beam-search"
3. "generic-sampling"
4. "top-k-sampling"
5. "top-p-nucleus-sampling"

```python
from chattingtransformer import ChattingGPT2

gpt2 = ChattingGPT2("gpt2")
text = "I think therefore I "
greedy_output = gpt2.generate_text(text, method = "greedy")
beam_search_output= gpt2.generate_text(text, method = "beam-search")
generic_sampling_output = gpt2.generate_text(text, method = "generic-sampling")
top_k_sampling_output = gpt2.generate_text(text, method = "top-k-sampling")
top_p_nucleus_sampling_output = gpt2.generate_text(text, method = "top-p-nucleus-sampling")
```


## Custom Method


Below are the default values for the parameters you may adjust to modify how the model generates text. For more information about the purpose of each parameter, please visit Hugging Face's Transformer documentation on this  [webpage](https://huggingface.co/transformers/main_classes/model.html#generative-models).
  
  max_length:  
  min_length:  
  do_sample: 
  early_stopping: 
  num_beams: 
  temperature: 
  top_k: 
  top_p: 
  repetition_penalty: 
 length_penalty: 
  no_repeat_ngram_size: 
  bad_words_ids: 



### Modify All Settings 

You have the ability to modify all of the default text generation parameters at once as shown below. 
```python
from chattingtransformer import ChattingGPT2

settings =  {  
  "do_sample": False,  
  "early_stopping": False,  
  "num_beams": 1,  
  "temperature": 1,  
  "top_k": 50,  
  "top_p": 1.0,  
  "repetition_penalty": 1,  
  "length_penalty": 1,  
  "no_repeat_ngram_size": 2,  
  'bad_words_ids': None,  
}
gpt2 = ChattingGPT2("gpt2")
text = "I think therefore I "

result = gpt2.generate_text(text, method = "custom", custom_settings = settings)

```

### Modify Length 
You may modify the min and max length of the output using parameters within the generate_text method. 
```python
from chattingtransformer import ChattingGPT2


gpt2 = ChattingGPT2("gpt2")
text = "I think therefore I "

result = gpt2.generate_text(text, min_length=5, max_length=500)
```


