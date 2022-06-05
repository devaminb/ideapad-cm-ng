# `ideapad-cm` next generation

> ⛔ **I stopped using GNU/Linux. I will not continue working on this script.** ⛔

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://github.com/devaminb/ideapad-cm-rewrite/graphs/commit-activity)
![GitHub last commit](https://img.shields.io/github/last-commit/devaminb/ideapad-cm-rewrite)
[![GitHub license](https://img.shields.io/github/license/devaminb/ideapad-cm-rewrite)](https://github.com/devaminb/ideapad-cm-rewrite/blob/main/LICENSE)
[![HitCount](https://hits.dwyl.com/devaminb/ideapad-cm-rewrite.svg?style=flat)](http://hits.dwyl.com/devaminb/ideapad-cm-rewrite)

![CLI Demo](cli.gif "ideapad-cm demonstration")

> ⚠️ **USE AT YOUR OWN RISK!**

💻 A rewrite of `ideapad-cm` in Python with improved systemd
and GNOME 3 integration.

## Should you use it?

If you use a Lenovo IdeaPad laptop and a GNU/Linux distribution, then
you definitely need to install this tool!

Battery conservation mode always keeps your battery charged around
60%. Your battery will last longer.

## Installation

The easiest installation method is to use
[pipx](https://github.com/pypa/pipx). Make sure to run `pipx ensurepath`
after installing pipx.

```shell
pipx install ideapad-cm
```

## Usage

As of version 0.1.3, only 3 commands are supported.

### `ideapad-cm enable`

This command enables the battery conservation mode.

### `ideapad-cm disable`

This command disables the battery conservation mode.

### `ideapad-cm status`

This command lets you know if the battery conservation mode is enabled
or disabled.

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

## Contributing [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](https://makeapullrequest.com)
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE)
file for details.
