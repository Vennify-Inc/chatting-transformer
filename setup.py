# from distutils.core import setup
from setuptools import setup

import pathlib

current_location = pathlib.Path(__file__).parent
readme = (current_location / "README.md").read_text()

setup(
    name = 'chattingtransformer',
    packages = ['chattingtransformer'],
    version = '1.0.3',
    license='Apache 2.0',
    description = "GPT2 text generation with just two lines of code!",
    long_description= readme,
    long_description_content_type='text/markdown',
    author = "Vennify Inc",
    author_email = 'eric@vennify.ca',
    url = 'https://github.com/Vennify-Inc/chatting-transformer',
    keywords = ["gpt2", "artificial", "intelligence", "ai", "text", "generation",  "chatting", "vennify", "gpt", "transformer", "transformers", "nlp", "nlu", "natural", "language", "processing", "understanding"],


    install_requires=[
            'transformers>=3.1.0',
            'torch>=1.6.0',

      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        "Intended Audience :: Science/Research",
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Natural Language :: English"

      ],
    )
