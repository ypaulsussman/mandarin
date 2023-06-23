# "Chengyu Trainer AKA FourChar"

This repo is the culmination of my weekend take-home code challenge for my (_eventually offered/accepted!_) role at [ETI](https://eti.umn.edu/); it's also the first time I ever interacted with the Django ecosystem.

Here's the original pitch:

---

I've recently begun studying Mandarin; I'm currently at the stage where I can say "thank you," "sorry," "We do not eat fish in the morning," and "Teacher Zhang is from London."

One nifty linguistic aspect of Mandarin are the [Chengyu](https://en.wikipedia.org/wiki/Chengyu); since many of them incorporate at least one or two of the (_super basic_) characters I'm currently learning, I suspect they could serve as a mnemonic tool by adding extra semantic connections to assist in recall.

I'm envisioning an app that:
1) when fed 1-2 characters, returns all Chengyu that contain those characters, in listview format;
2) offers a CRUD detailview for e.g. how common a ~native speaker (_i.e. Zoe_) reckons the Chengyu to be, and an example sentence;
3) (_reach goal!_) when one such Chengyu is clicked, pings e.g. AWS Translate to return the (_likely nonidiomatic_) English equivalents of each constituent character;
4) (_reach goal!_) when one such Chengyu is clicked, scrapes 1-2 preselected webpages for examples of the Chengyu's actual, idiomatic meaning.

That feels fairly straightforward to implement in Rails, but I could also attempt it in Django.

Does...

1) definitely the first two of the above, in Django, but
2) using its default sqlite config for effectively-local-only usage, and
3) eschewing an admin profile and authz/authn

...meet the criteria you're envisioning?

(_Alternatively, I could add user-profiles and probably one of the reach features, and remotely host, but in Rails -- let me know what sounds best! If I don't hear anything in 24hrs, I'll take the safe route and kick off in Ruby._) :)

---

It was a great introduction to the power and flexibility of Django's built-in admin tools, as well as some of the nuances of Django's model and migration systems (_and how they differ from Rails'._)

`boto3` was as straightforward to integrate with AWS Translate as with the other services I'd used it for in the past; overall, the only thing keeping me from playing around with this repo more was... well, the fact that I started a new job just a couple weeks after. 🙂 
