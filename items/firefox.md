## Updating Mozilla Firefox on Linux | not with apt or snap

Recently I installed Mozilla Firefox on my Windows to test how a website works in different browsers. Even though my aim was to test the website, it turned into testing the newly installed Mozilla Firefox. I'm using Mozilla Firefox as my default browser at work because it comes as the default browser in Linux, and it feels heroic using Mozilla (running cmds like `firefox google.com`) after using Google Chrome everywhere.

Honestly, the new Firefox on my Windows feels like a Ferrari, but on my Linux it feels like a Maruti 800. Basically, I was using version 136 on Linux, and the latest one was 145. The very next workday I blindly executed the commands `sudo snap refresh firefox` — didn’t work — then `sudo apt update firefox` — didn’t work either. Then I got my consciousness back and realized Firefox was not installed using a package manager.

So I quickly checked `which firefox`, which showed me the softlink <softlink here> of the Firefox executable binary <hard link here>. Keeping this path not in the mind but in the terminal, I opened Firefox to download the latest version of Firefox for Linux. From here onward a gush of Linux terminal commands came to my mind. What I wanted to do was: create a backup of my current profile, windows, and tabs; create a backup of the whole Firefox folder; locate and extract the downloaded package; move the extracted stuff to the location pointed to by the hard link; check if Firefox can be invoked using the terminal; and if not, fix the softlink. (If you are a Linux guy, just think of all the commands.)

Now to the keyboard:

1. Located (cd and ls) and created the backups using <Backup Command here>

2. Located and extracted the downloaded package using `tar -xvf <Package name here>`

3. Moved (mv) the extracted files to the hard-link-pointing location

4. Checked if the newly installed Firefox was working or not (command: `firefox`). It was not working. So I again checked `which firefox`, which was soft-linking a shell script (.sh file), but my new installation didn’t have a shell script. Fixed the softlink using <softlink fixing command here>

With this done, Firefox was working — but my windows, tabs, and everything were missing.

5. I went to the previously backed-up files and copied the profile JSON <JSON file coping command here>. When I opened Firefox, it showed a Restore Session button on the opening tab, through which I got all my windows and tabs back.

That's it. Thank you!