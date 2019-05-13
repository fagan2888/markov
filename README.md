The Gospel According to Markov
==============================

A project for fun that generates a sample from a Markov model of a text (e.g.,
the Bible).

## Usage 

    $ python markov.py text states outputwords [tokenizer]

 - *text*: path to a text file
 - *states*: number of states in the Markov model
 - *outputwords*: minimum number of words to sample from the model (sampling
   will end when the end of a sentence is reached).

## Examples

The Gospel:

    $ python markov.py text/gospel.txt 2 50

> I indeed have baptized you with water unto repentance. but he escaped out of
> the mammon of unrighteousness; that, when Elisabeth heard the king, behold,
> there came a leper to him, and said, Thou art his disciple; but we are many.
> 5:10 And he ran before, and climbed up into a pit on the unjust.

The Koran:

    $ python markov.py text/koran.txt 2 50

> We are firmly resolved: God said, Verily I am a public preacher. Is it not
> been upon thee, and who are respited until the rising of the good things
> which we have sent our spirit Gabriel also, in a sure receptacle: afterwards
> we blot out the unbelieving women: but demand back that which is in heaven
> and on earth; and those who fear God and his brother, and he is almighty.

Leaves of Grass:

    $ python markov.py text/leavesofgrass.txt 2 50

> Come Muse migrate from Greece and Rome, With the twirl of my spirit arouses
> me, Looking forth on pavement and land, Belonging to the head of the Nation
> of many a star at night, fancy figures and jets; Beef on the river of old,
> condemn'd for a moment, Then blank and suspicious, My great thoughts as these
> is just as surely nothing.
