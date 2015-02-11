# Nairobi GNU/Linux Users Group Blog

This is the repository which hosts the code for the [Nairobi GNU/Linux Users Group](https://nairobilug.or.ke) blog. We wanted a fun, nerdy and democratic way to give our community an online presence, so here we are.

[![Visit our IRC channel](https://kiwiirc.com/buttons/irc.freenode.net/nairobilug.png)](https://kiwiirc.com/client/irc.freenode.net/#nairobilug)


## Wanna Build It?

In order to build this, you need to have [Pelican](http://getpelican.com/) installed. The easiest way to do this is to use Python virtual environments via [pyenv](https://github.com/yyuu/pyenv) and the [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv) plugin.

### pyenv quick install
Clone the `pyenv` and `pyenv-virtualenv` to your home folder:

```console
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
$ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
```

Add the following snippet to your shell's init script, ie  `~/.bashrc`:

```bash
# Enable pyenv
# See: https://github.com/yyuu/pyenv#basic-github-checkout
if [[ -d ~/.pyenv ]]; then
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"

    eval "$(pyenv init -)"
    # optionally enable pyenv-virtualenv
    # See: https://github.com/yyuu/pyenv-virtualenv
    if [[ -d ~/.pyenv/plugins/pyenv-virtualenv ]]; then
        eval "$(pyenv virtualenv-init -)"
    fi
fi
```

This tells your shell to initialize `pyenv` and `pyenv-virtualenv` on startup, so close and re-open your shell to activate it.

### Create a virtualenv

Once you have `pyenv` installed, create a virtual environment to hold Pelican and its dependencies:

    $ pyenv virtualenv nairobilug
    $ pyenv activate nairobilug

This creates a virtual environment and then activates it. If you want to exit the virtual environment, just type `deactivate`.


### Install Pelican & friends

Use `pip` to install the list of dependencies into your virtual environment:

    pip install -r https://raw.github.com/nairobilug/nairobilug.or.ke/master/requirements.txt


#### Preparations

The theme we're using, [pelican-alchemy](https://github.com/nairobilug/pelican-alchemy), is a "git submodule", which means it is maintained as its own separate git repository (with its own git history, project, etc). Submodules are stored in the `.gitmodules` file, and we first need to initialize and clone it before we can build.

Navigate to where you've cloned this [repo](http://github.com/nairobilug/nairobilug.or.ke) and then:

    git submodule init
    git submodule update

You only need to do the initialization the first time you build. After that, you can simply use the update command to get the latest submodule changes.


#### GENERATE teh BLAWG

Now that the theme exists, we can build:

    pelican content

This takes the Markdown files from the `content` folder and generates static HTML pages inside the `output` directory. That's it. No MySQL, no PHP, etc...


#### It Works, SHIPIT!!1

You can use any web server to view the generated HTML. For example, Python's built-in simple HTTP server:

    cd output
    python -m SimpleHTTPServer

And now you should see the blog at: [http://localhost:8000](http://localhost:8000)


## Workflow for Blog Posts

If you're interested in writing a blog post for the site, you need to:

  - Fork the [repo](http://github.com/nairobilug/nairobilug.or.ke)
  - Hack hack hack
  - Push the changes to your repo; preferably to a topic branch, like `why-i-love-linux`
  - Make a pull request against the `master` branch


## Contact

If you have any questions, drop by **#nairobilug** on Freenode. Happy blogging!
