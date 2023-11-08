# Url shortener

A script to help get shorter links for a provided url, and to calculate number of clicks on a link.
## Environment

### Requirements
Python3 should be already installed. Requires libraries:
```
request
```
```
python-dotenv
```
Both can be installed by running
```
pip install -r requirements.txt
```

### Environment variables
- BITLY_TOKEN

1. Put `.env` file near `main.py`.
2. `.env` contains text data without quotes.

## Run

While in the folder with the script, write in the console:
```
python3 main.py {URL}
```
Examples:
```
python3 main.py https://dvmn.org/
```
```
python3 main.py https://bit.ly/3PRF6SI
```
The script checks whether the link provided is shortened or not.

If not, it obtains and prints a shortened link.

![image](https://github.com/DeusProtivogas/BitLink/assets/28997966/b05d76fb-c107-47b7-becf-6fee85939977)


If the provided link is a Bitlink, the script prints number of clicks on the link over the last 30 days.

![image](https://github.com/DeusProtivogas/BitLink/assets/28997966/8af07bfd-f453-4865-b7bc-4d5312d54228)


## Code description

### main.py

The main script.

Necessary data: user's API key (Obtained from the Bitly website); the link to a website.

On launch: Checks whether the provided link is shortened (here called 'Bitlink') or not.

##### is_bitlink

Checks whether the provided link is shortened or not.

##### count_clicks

Obtains the number of clicks for the short url and prints the amount of clicks on that link in the previous 30 days.

##### shorten_link

Shortens the provided link
