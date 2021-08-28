from alias import TARGET_BAT, Alias

# alias       Manage scoop aliases
# bucket      Manage Scoop buckets
# cache       Show or clear the download cache
# checkup     Check for potential problems
# cleanup     Cleanup apps by removing old versions
# config      Get or set configuration values
# create      Create a custom app manifest
# depends     List dependencies for an app
# export      Exports (an importable) list of installed apps
# help        Show help for a command
# hold        Hold an app to disable updates
# home        Opens the app homepage
# info        Display information about an app
# install     Install apps
# list        List installed apps
# prefix      Returns the path to the specified app
# reset       Reset an app to resolve conflicts
# search      Search available apps
# status      Show status and check for new app versions
# unhold      Unhold an app to enable updates
# uninstall   Uninstall an app
# update      Update apps, or Scoop itself
# virustotal  Look for app's hash on virustotal.com
# which       Locate a shim/executable (similar to 'which' on Linux)


def scoop_alias(name, body, default_args=None):
    return Alias(
        name, body, default_args=default_args, targets=[TARGET_BAT], echo_flag=True
    )


def scoop_alias_seq():
    yield scoop_alias("sci", "scoop install")
    yield scoop_alias("scun", "scoop uninstall")

    yield scoop_alias("scls", "scoop list")
    yield scoop_alias("scup", "scoop update", "*")
    yield scoop_alias("sccl", "scoop cleanup", "*")

    yield scoop_alias("sch", "scoop hold")
    yield scoop_alias("scun", "scoop unhold")

    yield scoop_alias("scca", "scoop cache")
    yield scoop_alias("sccarm", "scoop cache rm", "*")

    yield scoop_alias(
        "uuu", "scoop update * && scoop cleanup * && scoop cache rm * && rustup update"
    )


def git_alias(name, body):
    return Alias(name, body, echo_flag=True)


def git_alias_seq():
    yield git_alias("gist", "git status")
    yield git_alias("gipu", "git push")


def ytdl_alias_seq():
    yield git_alias("ytdl", "youtube-dl")


def alias_seq():
    yield from scoop_alias_seq()
    yield from git_alias_seq()
    yield Alias("ff", "far .")
    yield Alias("zzz", "echo", ["1st", "2nd", "3rd"])
    yield from ytdl_alias_seq()


def path_seq():
    yield "c:/bin"
