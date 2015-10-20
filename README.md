# Tunes Project

This is a project exploring relationships between traditional Irish tunes using Python.

## User Stories

User stories divided into 'current sprint' and 'parking lot' categories can be found [here](https://docs.google.com/document/d/1NmkJvdyGIg_uRA1CXCmsfzD2kpdQg0QoPHq0OWZlYic/edit?usp=sharing).

## Sprint Log

### Current
Sprint A - Oct 20 2015 start. Target end date Oct 23 2015.

### Completed
<<Completed sprints with (start date, end date) go here. See [here](https://docs.google.com/document/d/1NmkJvdyGIg_uRA1CXCmsfzD2kpdQg0QoPHq0OWZlYic/edit?usp=sharing) for sprint contents.>>

## General Implementation Ideas
### Phase 1

In this current phase, I am trying to explore how to store information about tunes in a framework-agnostic sort of way and support a collection of features that I would find useful as a tunes player.

What should we implement?

* On the fly set creation, driven by start tune set length (and potentially transition rules)
* Ability to log at a session and create unions based on tunes played
* Ability to link a tune to media resources and access those resources
* --> bonus to above: ability to loop over a tune, at any tempo, using some quick buttons
mail
* Suggest sets based on key transitions and tune type, given that no current union exists between the tunes

### Phase 2

We're not here yet, but this phase probably involves plugging in the Phase 1 work to an online framework and giving it a more intuitive interface.
