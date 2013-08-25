# Nairobi GNU/Linux Users Group blog
This is the repository which hosts the code for the [Nairobi GNU/Linux Users Group blog](http://nairobilug.or.ke).  We wanted a fun, nerdy and democratic way to give our community an online presence, so here we are.

## Wanna build it?
In order to build this, you need to have [Pelican](http://blog.getpelican.com/) installed.  The easiest way to do this is to use Python virtual environments; `virtualenv` will work, but it's recommended to use `virtualenv-wrapper` (a set of extensions to `virtualenv`).

For reference, a list of commonly-used distro package names is:

  - Arch Linux: `python-virtualenvwrapper`
  - Mac OS X (brew): `pyenv-virtualenv` for virtualenv and then follow the [mkvirtualenvwrapper instructions](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

If your distro isn't listed, you'll have to do a bit of homework (and then make a pull request to fix these docs).

#### Create a virtualenv
Once you have `virtualenv-wrapper` installed, create a virtual environment to hold Pelican and its dependencies:

    mkvirtualenv -p `which python2` nairobilug
    workon nairobilug

This creates a virtual environment where Python is explicitly set to version 2, and then activates it.  If you want to exit the virtual environment, you just type `deactivate`.

#### Install Pelican and friends
Use `pip` to install the list of dependencies into your virtual environment:

    pip install -r https://raw.github.com/nairobilug/nairobilug.or.ke/master/requirements.txt

#### GENERATE BLAWG
Navigate to where you cloned the [repo](http://github.com/nairobilug/nairobilug.or.ke) and then use Pelican to build it:

    pelican -s pelican.conf.py content -o output

This takes the Markdown files from the `content` folder and generates static HTML pages inside the `output` directory.  That's it.  No MySQL, no PHP, etc...

#### It works, SHIPIT!!!!11
You can use any web server to view the generated HTML.  For example, Python's builtin simple HTTP server:

    cd output
    python -m SimpleHTTPServer

And now you should see the blog at: http://localhost:8000

#### Teh THEME <>
Using the [chunk](https://github.com/nairobilug/pelican-chunk) pelican theme:

    git clone https://github.com/nairobilug/pelican-chunk chunk
    pelican-themes --install chunk

Enjoy a refreshing Diet Coke.

## Workflow for blog posts
If you're interested in writing a blog post for the site, you need to:

  - Fork the [repo](http://github.com/nairobilug/nairobilug.or.ke)
  - Hack hack hack
  - Push the changes to your repo; preferably to a topic branch, like `why-i-love-linux`
  - Make a pull request against the `master` branch

## Contact
If you have any questions, drop by #nairobilug on Freenode.  Happy blogging!
