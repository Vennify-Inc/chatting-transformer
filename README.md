<div align="center">
  <img src="assets/logo.png" height="200">
</div>

# Chatting Transformer
### Easy text generation using state of the art NLP models.
[![License: Apache](https://img.shields.io/badge/License-Apache-green.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

Chatting Transformer is a Python library for generating text using GPT2. GPT-2 is a language model that was developed by OpenAI that specializes in generating text. At one point, Open-AI feared releasing its 1.5 billion parameter version of GPT-2, due to fears of it being misused. By using Chatting Transformer, you can implement and use this model with just two lines of code. 

## Installation



```bash
pip install chattingtransformer
```

## Basic Usage

```python
import chattingtransformer import ChattingGPT2


model_name = "gpt2" 
gpt2 = ChattingGPT2(model_name)

text = "I think therefore I" 
results = gpt2.generate_text(text) 

print(results) #outputs: *actual output here*
```
## Available Models
| Model         | Parameters   |      Size        | 
|------------------------------|------------------|-----------------|
| tiny-gpt2    |      ---      |      2.51 MB     | 
| gpt2         |      134 M    |      548  MB     | 
| gpt2-medium  |      335 M    |      1.52 GB     | 
| gpt2-large   |      774 M    |      3.25 GB     | 
| gpt2-xl      |      1.5 B    |      6.43 GB     |      


```python
import chattingtransformer import ChattingGPT2

gpt2_tiny = ChattingGPT2("tiny-gpt2")
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
import chattingtransformer import ChattingGPT2

greedy = ChattingGPT2("gpt2", method = "greedy")
beam_search = ChattingGPT2("gpt2", method = "beam-search")
generic_sampling = ChattingGPT2("gpt2", method = "generic-sampling")
top_k_sampling = ChattingGPT2("gpt2", method = "top-k-sampling")
top_p_nucleus_sampling = ChattingGPT2("gpt2", method = "top-p-nucleus-sampling")
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
import chattingtransformer import ChattingGPT2

settings =  {  
  "max_length": 100,  
  "min_length":  10,  
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
gpt2 = ChattingGPT2("gpt2",  method="custom", custom_settings=settings))
```

### Modify Select Settings 
You may only modify a subset of the settings. The rest of the parameters will use their default settings. 
```python
import chattingtransformer import ChattingGPT2

settings =  {  
  "max_length": 200,  
  "min_length": 100,   
 
}
gpt2 = ChattingGPT2("gpt2",  method="custom", custom_settings=settings))
```


## License
[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)
