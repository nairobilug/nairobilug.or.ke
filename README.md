# Nairobi GNU/Linux Users Group blog

This is the repository which hosts the code for the [Nairobi GNU/Linux Users Group](https://nairobilug.or.ke) blog. We wanted a fun, nerdy and democratic way to give our community an online presence, so here we are.

![Screenshot](/screenshot@2x.png?raw=true "Screenshot")

## How to build

In order to build this, you need to have [Pelican](http://getpelican.com/) installed. The easiest way to do this is in a Python [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/). We recommend using [pyenv](https://github.com/yyuu/pyenv) with [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv) to set one up.

### pyenv quick install

Luckily, pyenv has an automatic installer, [pyenv-installer](https://github.com/yyuu/pyenv-installer). Refer to the pyenv [README](https://github.com/yyuu/pyenv#installation) if you prefer a manual process. The recommended way:

    $ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

### Create a virtualenv

Once you have pyenv installed, create a virtual environment to hold Pelican and its dependencies:

    $ pyenv virtualenv nairobilug
    $ pyenv activate nairobilug

This creates a virtual environment and then activates it. If you want to exit the virtual environment, just type `$ deactivate`.

### Clone the repo

If you haven't already, clone this repo (or your version of it):

    $ git clone --recurse-submodules https://github.com/nairobilug/nairobilug.or.ke

### Install Pelican & friends

Use `pip` to install the list of dependencies (including Pelican) into your virtual environment:

    $ pip install -r requirements.txt

### Generate the blog

Now that the dependencies exists, we can build:

    $ pelican content

This takes the Markdown files from the `content` directory and generates static HTML pages inside the `output` directory. That's it. No MySQL, no PHP, etc...

### View the results

You can use any web server to view the generated HTML. For example, Python's built-in simple HTTP server:

    $ cd output
    $ python -m SimpleHTTPServer

And you should see the blog if you visit [http://localhost:8000](http://localhost:8000).

### Get help

If you're having trouble, you can ask for help by creating [an issue](https://github.com/nairobilug/nairobilug.or.ke/issues/new). :smile:

## Workflow for blog posts

If you're interested in writing a blog post for the site, you need to:

  - Fork the [nairobilug/nairobilug.or.ke](http://github.com/nairobilug/nairobilug.or.ke) repository
  - Write a blog post using Markdown in the `content` directory
  - Push the changes to a topic branch, like `why-i-love-linux`, on *your* fork of the repository
  - Make a [pull request](https://help.github.com/articles/using-pull-requests/) against the `master` branch of nairobilug/nairobilug.or.ke

## Contact

If you have any questions, drop by **#nairobilug** on Freenode, or our [mailing list](https://groups.google.com/group/nairobi-gnu). Happy blogging!

[![Visit our IRC channel](https://kiwiirc.com/buttons/irc.freenode.net/nairobilug.png)](https://kiwiirc.com/client/irc.freenode.net/#nairobilug)
