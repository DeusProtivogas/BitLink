# Url shortener

A script to help get shorter links for a provided url, and to calculate number of clicks on a link.

### main.py

The main script.

Necessary data: user's API key (Obtained from the Bitly website); the link to a website.

On launch: Checks whether the provided link is shortened (here called 'Bitlink') or not.

To launch: While in the folder with the script, write in the console:
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
![img.png](img.png)

If the provided link is a Bitlink, the script prints number of clicks on the link over the last 30 days.
![img_2.png](img_2.png)

##### is_bitlink

Checks whether the provided link is shortened or not.

##### count_clicks

Obtains the number of clicks for the short url and prints the amount of clicks on that link in the previous 30 days.

##### shorten_link

Shortens the provided link