# HoyoLab-Check-In
Python Script for Completing Daily HoyoLab Check-In

This script is a refactor of the script created by [canaria3406](https://github.com/canaria3406) to facilitate the daily HoyoLab Check-In.
This code is a python refactor of the [main Discord script](https://github.com/canaria3406/hoyolab-auto-sign/blob/main/src/main-discord.gs).
Additional thanks to [this Reddit post](https://www.reddit.com/r/Genshin_Impact/comments/rohk7w/quick_tutorial_for_building_your_own_hoyolab/) for serving as a Python guide.

A more detailed guide for use can be found [here](https://github.com/canaria3406/hoyolab-auto-sign/blob/main/README.md).

Follow the directions provided [here](https://github.com/Joshua-Noakes1/mei-cards#2-getting-your-hoyolab-cookies) to find your HoyoLab cookies and fill them in the profiles fields in the scripts.

In addition to the standard Python modules, this code requires the Python [requests library](https://pypi.org/project/requests/).

Daily runs of the script can be automated using [Windows Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/starting-an-executable-daily) or an equivalent.

If you wish to receive notifications of Check-In status, you will need a [Discord account](https://support.discord.com/hc/en-us/articles/360033931551-Getting-Started#h_01H4RR2GE2FAK7DZ5W3765NGVT).
Follow the directions provided [here](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID#h_01HRSTXPS5H5D7JBY2QKKPVKNA) to find your Discord ID.
Follow the directions provided [here](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) to make a Discord webhook.