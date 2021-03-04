import logging
import logging.config
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

from chattingtransformer.settings import POSSIBLE_METHODS

from chattingtransformer.settings import get_settings


class ChattingGPT2():
    """
    # An easy to use class for state-of-the-art text generation.

    Key Features:
        1. Initialize a GPT2 model with just one line of code.
        2. Generate text in a single line of code with the your GPT2 model
        3. Select 1 of 4 GPT2 models.
        4. Fully customizable text generation parameters
    """

    valid_models = [
                    "gpt2",
                    "gpt2-medium",
                    "gpt2-large",
                    "gpt2-xl"]


    __is_valid = False

    def __init__(self, model_name="gpt2"):

        # show only happytransformer logs
        handler = logging.StreamHandler()
        handler.addFilter(logging.Filter('chattingtransformer'))
        logging.basicConfig(
            format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
            datefmt='%m/%d/%Y %H:%M:%S',
            level=logging.INFO,
            handlers=[handler]
        )
        self.logger = logging.getLogger(__name__)

        if model_name not in self.valid_models:
            self.logger.error("Please enter a valid model name. "
                              "For example, \"gpt2\" or \"gpt2-xl\"")

        else:
            self.logger.info("Loading \"%s\"...", model_name)
            self._generation_tokenizer = AutoTokenizer.from_pretrained(model_name)
            pad_token_id = self._generation_tokenizer.eos_token_id
            self._generation_model = AutoModelForCausalLM.from_pretrained(model_name,
                                                                          pad_token_id=pad_token_id)
            self.logger.info("Done loading \"%s\"", model_name)
            self._device = torch.device(
                "cuda" if torch.cuda.is_available()
                else "cpu"
            )

            if self._device == 'cuda':
                self._generation_model.to(self._device)
            self.logger.info("Using model: %s", self._device)


            self.__is_valid = True


    def __check_gen_text_is_val(self, text, method):
        if not self.__is_valid:
            self.logger.error("Please enter a valid model name. "
                              "For example, \"gpt2\" or \"gpt2-xl\"")
            return False
        elif not isinstance(text, str):
            self.logger.error("Please enter a int for the max_length parameter")
            return False
        elif len(text) == 0:
            self.logger.error("The text input must have at least one character")
            return False
        elif method not in POSSIBLE_METHODS:
            self.logger.error("Please enter a valid method name, for example \"top-k-sampling\"")
            return False

        return True

    def generate_text(self, text, combine=True, method="top-k-sampling", custom_settings=None, min_length=20, max_length=60):
        """
        :param text: starting text that the model uses to generate text with.
        :param: combine: if true, the starting text will be concatenated with the output.
        :param method: either one of 1/5 preconfigured methods, or "custom" to indicate custom settings
        :param custom_settings: if method == "custom", then custom settings may be provided in the form of
              a dictionary. Refer to the README to see potential parameters to add.
              Parameters that are not added to the dictionary will keep their default value.

        :return: Text that the model generates.
        """

        is_valid = self.__check_gen_text_is_val(text, method)

        if is_valid:
            settings = get_settings(method, custom_settings, self.logger)
            input_ids = self._generation_tokenizer.encode(text, return_tensors="pt")
            output = self._generation_model.generate(input_ids,
                                                     min_length=min_length,
                                                     max_length=max_length,
                                                     do_sample=settings['do_sample'],
                                                     early_stopping=settings['early_stopping'],
                                                     num_beams=settings['num_beams'],
                                                     temperature=settings['temperature'],
                                                     top_k=settings['top_k'],
                                                     top_p=settings['top_p'],
                                                     repetition_penalty=settings['repetition_penalty'],
                                                     length_penalty=settings['length_penalty'],
                                                     no_repeat_ngram_size=settings['no_repeat_ngram_size'],
                                                     bad_words_ids=settings['bad_words_ids'],
                                                     )
            result = self._generation_tokenizer.decode(output[0], skip_special_tokens=True)
            final_result = self.__gt_post_processing(result, text, combine)

            return final_result

        else:
            return ""


    def __gt_post_processing(self, result, text, combine):
        """
        A method for processing the output of the model. More features will be added later.

        :param result: result the output of the model after being decoded
        :param text:  the original input to generate_text
        "parm combine: if true, returns  text and result concatenate together.
        :return: returns to text after going through  post-processing
        """

        if combine:
            return result

        return result[len(text):]

