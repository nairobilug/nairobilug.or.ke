Title: Simultaneously pushing to two remotes in a git repository
Date: 2015-05-10 16:40
Category: Linux
Tags: linux, git
Slug: pushing-two-git-remotes
Author: Alan Orth
Summary: Pushing to two git remotes at once using multiple push URLs for a single remote

Sometimes you need to push commits to two remotes in a git repository — either for a cheap "backup" of sorts, or for some public / private repository scheme you may have in your organization, etc.

Let's say you have a repository hosted on GitHub *and* BitBucket (hey, GitHub is king today, but you never know!). You could add a remote for each and push to them individually:

    $ git push github
    $ git push bitbucket

This works fine but it's a bit manual. Also, assuming you want both remotes to essentially be mirrors of each other, there's a better way.

### A better way
If you're using any relatively modern version of git (1.9?) you can manipulate the remote to include two push URLs. Instead of adding a second remote, you simply add a second push URL to the existing remote.

For example, adding a BitBucket URL to the remote called "origin":

    $ git remote set-url origin --add git@bitbucket.org:alanorth/repo.git

After that the remote looks like this:

    $ git remote -v
    origin  git@github.com:alanorth/repo.git (fetch)
    origin  git@github.com:alanorth/repo.git (push)
    origin  git@bitbucket.org:alanorth/repo.git (push)

Now there are two push URLs, so every time you push it will go to both remotes, while pull or update operations will only come from the URL labeled "fetch".

You're welcome. ;)

This was [originally posted](https://mjanja.ch/2015/05/simultaneously-pushing-to-two-remotes-in-a-git-repository/) on my personal blog; re-posted here for posterity.
