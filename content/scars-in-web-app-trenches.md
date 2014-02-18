Title: Scars in Web App Trenches
Date: 2014-02-17 13:00
Category: Web Development
Tags: web applications, web development
Slug: scars-in-web-app-trenches
Author: Muriithi Frederick Muriuki
Summary: My experiences building web-apps and some suggestions

Hey there.

I have been developing web applications for a while now, working freelance on oDesk, and from my work, I can state I do have some experience in doing this. Now, I will not claim to be a web-app ninja, but I will try to state my case as objectively as I can, but you decide how much salt you'll take it with. Deal?

##HTML - The M is for Markup

From what I have come to understand from the gurus and ninjas in this field, HTML was built as a markup language. It was meant to give meaning to the content of the page, e.g.

* &lt; h1 &gt; is greater than &lt; h2 &gt;, which in turn is greater than &lt; h3 &gt; etc
* &lt; form &gt; represents an electronic form where you can fill in and submit data
* &lt; button &gt; and &lt; input type='button' ... &gt; represent input elements that can be used to activate certain actions like submit forms, etc
* &lt; a &gt; - the anchor tag, is meant to represent links to a different part of the page, other pages, or another site

and many others. . . (For awesome HTML, CSS and Javascript tutorials, click [here](http://htmldog.com/))

Now, if there is one thing that I have found painful in my work, it is when people make use on the anchor tag to submit forms.

Why?

I am one of those people still living in a third world country (and if things keep going the way they are, we just might have to come up with a whole new class beneath that for the country), and as such, bandwidth is expensive (I dare say, artificially so).

Now, we all know that the tag &lt; input type='submit' ... &gt; will submit any form it is in, no questions asked, but 'NOOOOOOOOO!', we have to bloat that up by getting rid of it, replacing it with a link, and then using the jQuery library to submit the form. A form submission, I tell you!

###But The Web is Javascript!

For all that have this argument, I refer you [here](http://motherfuckingwebsite.com/). Now, tell me you cannot see the content in that site. Then, riddle me this, before Javascript, jQuery, and others came along, pray tell, how were people submitting their html forms?

Now understand this <strong>I love Javascript</strong> and though I am not a jQuery ninja, I cannot argue against it's merits, but if we are going to use javascript everywhere, we might as well start killing mosquitoes with handguns, or slings, or catapults (take your pick).

##Back to the Basics

Hear me out, before you fetch the noose. I am making a simple suggestion here, based on the experience I have had with web applications, and even some plain websites.

When I land on your site, almost always, I am searching for information about your company, skill, etc. You, on the other hand, decide to make me have to struggle further to find the friggin content by putting those silly pictures, animations and shiznit in my path. Then, to insult me further, you make it so that, if I turn javascript off (It's off by default on my browser), I cannot see your content.
As if you have not hurt me enough, you make all your forms submit only via javascript/jQuery.

DEAR <deity>! I cannot count the number of times I have left websites and gone looking for other options due to this.

First, you eat away my bandwidth with silly content, then you force me to use even more of my bandwidth, just to get functionality that is already built into html.

##Collaboration

Let us view another scenario. You have to collaborate with a person in a different timezone building a web application. Now, you are a javascript, jQuery, etc ninja, and you can build anything in it. Her/him, not so much, but they are good at their PHP, Ruby, Python, C or whatever language they use on the backend.

Now, I do not know what you think, but I dare say, it is easier to pass to each other data, than force the backend to rely on the design of the frontend. Think also, of when you decide you want to change the look and feel of the website, then you have to make changes to both the front and backends, introducing new bugs, and possibly throwing away months of work debugging the data communication etc.

Now, if you had simply passed data between the frontend and backend, say using <strong>json, xml, plain text, plain html</strong> and others, then you can change the frontend any time without worrying about the backend, since the data interchange format is standardised, agreed upon, and <strong>DE</strong>fucking<strong>BUGGED!</strong>.

The backend guy/gal, can now concentrate on building and testing the backend, even with plain, unstyled, ugly, but functional html, and you can concentrate on styling (CSS) and behaviour (Javascript), without breaking the backend every time you make a tiny little change to the front end.

Now, think of your client, and how happy they are, every time they contact you to change the look and feel of the website, and you do that in a few weeks without breaking the backend, and they think you are a god!
Yeah, keep doing the shit you're doing, and that will never happen.

I'm angry, and so are you. Let me know what you think in the comments. Try to be civil, though I probably haven't.
