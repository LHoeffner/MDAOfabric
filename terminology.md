# Terminology MDAO - Lukas

## FSI / coupling in general

**subsolver**: solver of a single (physical) discipline

**framework**: code embedding other (possible black-box) components (on which it imposes a set of requirements). Sequence/control is determined by the framework, communication between the components is via the framework only. (opposite would be an API)

**data representation**: logic/discretisation on which some result/spatial-value is stored (grid vs. topology/mesh vs. particle)

**data format/structure**: type/container (str/dict/array etc.) with additionally defined substructure (e.g. "three arrays each containing an array with values for every grid-point" for storing 3D velocities in a numbered grid). A *data format* therefore contains/assumes a fixed *data representation* (s.o.) but (the other way round) a *representation* can be stored in various *formats*.

**interface**: "everything that makes two puzzle-pieces fit". For code-classes: A set of functions and properties for a certain purpose whose existence, behaviour and returns can be expected to be within a specification (of the *interface*) by other, interacting classes/scripts.


## MDAOfabric development

**component**: piece of code which can be put in a *stack* (see below) and run (in a loop or not) in sequence with other *components* - (currently) requires implementation of Initialize(), Run() and Finalize(). In the fabric, *components* are implemented as classes.

**stack**: number of *components* (which could themselves contain *stacks*) and their order in which they can be run "block-wise" (i.e. always from first to last, without running parts only - that would recommended by using a "sub-stack"). In contrast to *components*, stacks are members of such.