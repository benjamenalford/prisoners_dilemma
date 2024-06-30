# the prisoner's dilemma

![Trolley Problem](assets/image/trolly.gif)

## ok, not really

after another run through of the good place and all of the greatness that is the trolley problem episode in season 2, I decided that I should get around to crossing the last few things off my list.

This isn't <i>the [trolley problem](https://en.wikipedia.org/wiki/Trolley_problem) </i>, it's the [prisoner's dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma). it's smaller and I wanted to try some things out before moving on to the trolley.

I'm not going to explain the problem: the articles are there. you can read them, you made it this far. This has been studied every which way, the only thing educational here should be the code.

at the moment, it's just the basic version of the prisoner's dilemma.  I'm going to move up to the iterated version but have to implement state checking and some semblance of morality scale.

( I was asked about why I was doing this and promptly told to quit talking because this was all pointless and no one was listening.  )

## goals
- Remake a common problem and variations of
- use the data for training a neural network, naive bayes, and logistic regression model for comparisons.
- make the computer play the iterated version.
- implement a feedback loop to train the models while playing the iterated version.
- identify parameters which are common to the trolley problem ( morality) and create a relative abstraction of n+ traits that are common to both.
- stay busy.

## next steps
- replace the random choices with a weighted choice.
- implement a morality scale.
- expand to n+ number of iterations with the same set of prisoners.
- define 'winning' in a zero sum game.

### errata
- i stole the gif without permission. sue me.
- i'm not spell checking, proof reading, or anything nice like that. It's type, ride or die, and I'm tired.
- this has reminded how slow python is. I'm trying to keep everything light and readable instead of chasing performance. I'll probably redo this in C / Rust / whatever the flavor of year is.
- i'll over-complicate everything and add a build chain as it gets more complex but see the next point
- i'll end up over complicating this
- I wanted to do this in LISP but emacs was annoying me and I didn't want to fall back on Scheme / LUA / Janet / whatever,  it's C/LISP or nothing ( in this case the tooling pissed me off and now its nothing.)
- i'm not aiming for perfection; just trying to make something that works.