## Updating Mozilla Firefox on Linux | not with apt or snap

Recently I installed Mozilla Firefox on my Windows to test how a website works in different browsers. Even though my aim was to test the website, it turned into testing the newly installed Mozilla Firefox. I'm using Mozilla Firefox as my default browser at work because it comes as the default browser in Linux, and it feels heroic using Mozilla (running cmds like `firefox --version`, `firefox google.com`) after using Google Chrome everywhere.

Honestly, the new Firefox on my Windows feels like a Ferrari, but on my Linux it feels like a Maruti 800. Basically, I was using version 136 on Linux, and the latest one was 145. The very next workday I blindly executed the commands `sudo snap refresh firefox` & `snap list | grep firefox` — didn’t work — then `sudo apt update firefox` & `sudo apt list --installed | grep mozilla` — didn’t work either. Then I got my consciousness back and realized Firefox was not installed using a package manager.

So I quickly checked `which firefox`, which showed me the softlink `/usr/bin/firefox`, then found the path to Firefox executable binary (`/lib/...` in `/usr/bin/firefox -> /lib/firefox/firefox*`) using `ll /usr/bin/firefox`. Keeping this path not in the mind but in the terminal, I opened Firefox to download the latest version of Firefox for Linux. From here onward a gush of Linux terminal commands came to my mind. What I wanted to do was: create a backup of my current profile, windows, and tabs; create a backup of the whole Firefox folder; locate and extract the downloaded package; move the extracted stuff to the location pointed to by the hard link; check if Firefox can be invoked using the terminal; and if not, fix the softlink. (If you are a Linux guy, just think of all the commands.)

Now to the keyboard:

1. Killed all the running processes of firefox using `kill -9 firefox`.

2. Located (`cd /lib/firefox/` and `ls`) and created the backups of firefox main files using `sudo mv /lib/firefox /lib/firefox-old`.

3. Located and created the backups using `cp -rv ~/.mozilla/firefox ~/.mozilla/firefox.backup` since profile info was stored in `.mozilla` directory in the home directory.

4. Located and extracted the downloaded package using `tar -xvf firefox-145.0.tar.xz`. Moved (`sudo mv firefox/ /lib/firefox`) the extracted files to the `/lib/..` dir.

5. Checked if the newly installed Firefox was working or not (command: `firefox`). It was not working. So I again checked `which firefox`, which was soft-linking a shell script (`.sh` file), but my new installation didn’t have a shell script. Fixed the softlink using `sudo ln -sf /lib/firefox/firefox /usr/bin/firefox`

With this done, Firefox was working — but my windows, tabs, and everything were missing. So I killed all the processes of firefox again and

5. Went to the previously backed-up files and copied the profile JSON `cp ~/.mozilla/firefox.backup/wzhpg0kg.default-release/sessionstore-backups/recovery.jsonlz4 ~/.mozilla/firefox/wzhpg0kg.default-release/sessionstore.jsonlz4`. After this when I opened Firefox, it showed a 'Restore Session' button on the opening tab, through which I got all my windows and tabs back.

That's it. Thank you!