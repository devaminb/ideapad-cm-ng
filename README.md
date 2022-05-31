# `ideapad-cm` rewrite

> :warning: **USE AT YOUR OWN RISK!**

:computer: A rewrite of `ideapad-cm` in Python with improved systemd
and GNOME 3 integration.

## Motivation

`ideapad-cm` is a popular Bash script that I have used for years to
enable and disable battery conservation mode when I use GNU/Linux on
my Lenovo IdeaPad laptop.

Unfortunately, the script was taken down by its original author, and it
was never maintained or improved.

The 3 main features that were missing in the original project, in my
opinion, are:
- Script configuration as a systemd service. This will make it easy to
autostart at boot;
- Script integration with the desktop environment. I usually use
GNOME 3 (or one of its forks), and it would be better to be able to
enable and disable the script directly from the user graphical
interface (as we do in Windows using Lenovo Vantage);
- Easy installation. You needed to clone the repository locally, and
manually add it to PATH. The script was added to Arch's AUR, but I don't
personally use Arch that much. `gnome-shell-extension-ideapad` has the
same problem, as manual configuration steps are still needed after
installing the GNOME extension.

For the 3 reasons described above, I decided to rewrite the script
in Python. I chose Python because it's the only scripting language,
except Bash, that I'm familiar with.

Many other tools seem to exist (if you search "lenovo battery" on GitHub
for example), but I don't currently need any advanced feature. I'm
only mixing two tools: `ideapad-cm` and `gnome-shell-extension-ideapad`.

Both tools are licensed under GPLv3, so I'm free to adapt their code
(with attribution and releasing this project under the same license).

I will keep the CLI compatible with the original `ideapad-cm` CLI. This
way, you can simply uninstall the old tool (or remove it from PATH), and
install my new tool. If you have existing scripts that call `ideapad-cm`,
you don't need to change anything. The basic interface will be the same.

I'm building this tool for my own personal use. Use it at your own risk.
