# Professor Seal Bot

A multipurpose Discord bot made with pycord for a famous Data Science Youtuber's Productivity Community server hosted on Google Cloud (GCP).
Check out Tina Huang's channel [here](https://www.youtube.com/c/TinaHuang1)


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pycord and other necessary libraries.

```bash
pip install discord
pip install py-cord
pip install dotenv
pip install platform
pip install os
```

## Main libraries as of Version 1.3

```python
from platform import platform
import discord
import os
import dotenv
import random
```
## Features
### Feature 1
#### Focus mode is applied to the person who joins the voice channel and is removed when the person leaves the voice channel.
![Focus mode is applied to the person who joins the voice channel and is removed when the person leaves the voice channel.](https://github.com/HarshitSati/Professor-Seal-Bot/blob/master/assets/img/focusmode_img.png)
![Focus mode is hoisted](https://github.com/HarshitSati/Professor-Seal-Bot/blob/master/assets/img/focusmode_display.png)
### Feature 2
#### A set of random Reactions to messages in particular channels
![A set of random Reactions to messages in particular channels](https://github.com/HarshitSati/Professor-Seal-Bot/blob/master/assets/img/reaction_improve_everyday.png)
### Feature 3
#### Supports Streaming activity status for youtube and twitch
![Supports Streaming activity status for youtube and twitch](https://github.com/HarshitSati/Professor-Seal-Bot/blob/master/assets/img/status.png)
### Feature 4
#### Webhook embeds by discord
![Webhook embeds by discord](https://github.com/HarshitSati/Professor-Seal-Bot/blob/master/assets/img/webhook.png)

### Feature 5 
#### roberta based NLP context aware QUAM with `ps!context` and `ps!question`
![](https://github.com/HarshitSati/Professor-Seal-Bot/blob/master/assets/img/feature5.png)

## Setup of Virtual Environment on Linux
The virtual environment should have the libraries mentioned at the start installed.
```bash
source venv/bin/activate

nohup python3 -u [ProfessorSeal.py](http://professorseal.py/) &>> activity.log &
```
To kill the process you need to use htop to get the PID of he ProfessorSealBot process and then kill it with the `kill -9 PID` command.
```bash
htop 
kill -9 PID
```
 
## WIP
* Moderation and Moderation logs
* Huggingface API integration for NLP related tasks and moderations 
* Engagement statistics 
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
