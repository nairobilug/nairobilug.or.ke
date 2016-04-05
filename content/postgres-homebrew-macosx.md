Title: Using Homebrew's PostgreSQL on Mac OS X
Date: 2016-04-05 15:21
Category: Mac OS X
Tags: Postgres, Homebrew
Slug: postgres-homebrew-macosx
Author: Alan Orth
Summary: As a long-time GNU/Linux user I found it tricky to get PostgreSQL running on Mac OS X.

You're on Mac OS X and you need to use PostgreSQL, but you're used to GNU/Linux where there is usually a dedicated `postgres` system user for doing database administrator tasks. This is just a quick note to people who might have installed PostgreSQL from [Homebrew](http://brew.sh/) and find themselves scratching their head for the next step.  First, initialize the database directory and start the database daemon manually:

    $ initdb /opt/brew/var/postgres -E utf8
    $ postgres -D /opt/brew/var/postgres

**Note:** my Homebrew is installed in `/opt/brew`, so make sure to use the prefix relevant for your installation. Assuming all went well, you can now create the `postgres` superuser. In another shell:

    $ createuser --superuser postgres

After that you can do PostgreSQL admin things by connecting to the "postgres" database:

    $ psql postgres
    psql (9.3.12)
    Type "help" for help.

    postgres=#

To stop the server, issue a `^C` in the shell where you started the daemon — the daemon will receive the signal and initiate a graceful shutdown.

## Creating Other Users/Databases

Use the standard PostgreSQL command line tools to create extra users/databases, for example:

    $ createuser --pwprompt aorth
    $ createdb -O aorth --encoding=UNICODE mjanja

Notice how you don't have to _become_ the PostgreSQL system user first (ie, via `su - postgres`), you just use your normal Mac OS X user account.

This was [originally posted](https://mjanja.ch/2016/04/using-homebrews-postgresql-mac-os-x/) on my personal blog; re-posted here for posterity.
