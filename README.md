<p align="center">
    <a href="https://github.com/MarshalX/tgcalls">
        <img src="https://user-images.githubusercontent.com/32808683/111091141-62473b00-8508-11eb-9c05-3e0fd4a21af3.png" alt="pytgcalls logo" />
    </a>
    <br>
    <b>A simple and elegant client that allows you to make group voice calls quickly and easily.</b>
    <br>
    <a href="https://github.com/pytgcalls/pytgcalls/tree/master/example">
        Examples
    </a>
    •
    <a href="https://pytgcalls.github.io/">
        Documentation
    </a>
    •
    <a href="https://pypi.org/project/py-tgcalls/">
        PyPi
    </a>
    •
    <a href="https://t.me/pytgcallsnews">
        Channel
    </a>
    •
    <a href="https://t.me/pytgcallschat">
        Chat
    </a>
</p>


# PyTgCalls

[![pre-commit.ci status][pre-commit.ci-badge]][pre-commit.ci]
[![PyPI](https://img.shields.io/pypi/v/py-tgcalls.svg?style=flat)](https://pypi.org/project/py-tgcalls/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-tgcalls)](https://www.python.org/)
[![GitHub](https://img.shields.io/github/license/pytgcalls/pytgcalls)](https://github.com/pytgcalls/pytgcalls/blob/master/LICENSE)
![OS](https://img.shields.io/badge/platform-Linux%20%7C%20WSL2.0%20%7C%20Windows%20%7C%20macOS-lightgrey)
[![Node Version](https://img.shields.io/badge/node-%3E%20%3D%2015.0.0%20-brightgreen)](https://nodejs.org/it/)
![Architectures](https://img.shields.io/badge/architectures-x86__64%20%7C%20arm64v8%20%7C%20win__amd64%20%7C%20darwin__x64-blue)
[![Downloads](https://pepy.tech/badge/py-tgcalls)](https://pepy.tech/project/py-tgcalls)

This project allow to make Telegram group call with MTProto Api using Pyrogram and WebRTC, this is possible thanks to the power of NodeJS's WebRTC library and [@evgeny-nadymov]

## What are the supported clients?
The supported client for now is Pyrogram and Telethon, but we accept
also other clients, you can open a pull request with the edits

## How to install?
Here's how to install the PyTgCalls lib, the commands are given below:

``` bash
# With Git
pip install git+https://github.com/pytgcalls/pytgcalls -U

# With PyPi (Raccomended)
pip install py-tgcalls -U
```

## Conversion command (Video)
From file to raw format
``` bash
ffmpeg -i {INPUT_FILE} -f rawvideo -pix_fmt yuv420p {OUTPUT_FILE}
```

## Conversion commands

From file to raw format
``` bash
ffmpeg -i {INPUT_FILE} -f s16le -ac 1 -ar {BITRATE} {OUTPUT_FILE}
```

From stream link to raw format
``` bash
ffmpeg -y -i {STREAM_LINK} -f s16le -ac 1 -ar {BITRATE} {OUTPUT_FILE}
```

From youtube video/live-stream to raw format
``` bash
ffmpeg -i "$(youtube-dl -x -g "{YOUTUBE_LINK}")" -f s16le -ac 1 -ar {BITRATE} {OUTPUT_FILE}
```

## Credits

Big thanks to [@evgeny-nadymov] for allowing us to use their code from [telegram-react] and thanks
to [alemidev] for helping to rebuild this library

This library is based on [tgcallsjs] developed [@AndrewLaneX] and pyservercall by [@Laky-64]

[pre-commit.ci-badge]: https://results.pre-commit.ci/badge/github/pytgcalls/pytgcalls/master.svg
[pre-commit.ci]: https://results.pre-commit.ci/latest/github/pytgcalls/pytgcalls/master
[@evgeny-nadymov]: https://github.com/evgeny-nadymov/
[@AndrewLaneX]: https://github.com/AndrewLaneX/
[telegram-react]: https://github.com/evgeny-nadymov/telegram-react/
[tgcallsjs]: https://github.com/tgcallsjs/tgcalls
[pyservercall]: https://github.com/pytgcalls/pyservercall/
[@Laky-64]: https://github.com/Laky-64/
[alemidev]: https://github.com/alemidev/
