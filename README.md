# LION VIGNENERE CIPHER

A simple script to encrypt and decrypt [Vignere Things](https://en.wikipedia.org/wiki/Vigenère_cipher)

## usage

```bash
$python lion-vigenere.py [text] <options>
```

| Option |                                         Function                                         | Required |
|:------:|:----------------------------------------------------------------------------------------:|:--------:|
|  text  |                              The text to decrypt or encrypt                              |   True   |
|    k   |                       The key to use to decrypt or encrypt the text                      |  Varies  |
|    e   |  Changes mode to encrypt, if you don't specify   the -k option a random key is generated |   False  |