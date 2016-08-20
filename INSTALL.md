# MoVRs Installation and Setup

## Obtaining MoVRs

Presumably you are reading this file on our github site and thus you are
likely to know that the following commands on your local machine should get
you going:

```bash
git clone https://github.com/BrendelGroup/MoVRs
cd MoVRs/
```

That said, an implicit assumption is that your local machine runs some version
of Linux.  For genome-wide DNA motif finding you will likely work with large
date sets.  The __open__ (source) MoVRs software will make the analysis of these
data sets __easy__, __accurate__, __meaningful__, __reproducible__, and
__scalable__ (our __RAMOSE__ philosophy and promise).  The output of MoVRs will
be nicely organized but intermediate output files will be kept initially, so you
will need sufficient disk space.  It will be up to you to specify the number of
processors to be used in various parallel steps during the workflow.  We like to
have 4-10 processors dedicated to the task (although most of the time, fewer
processors will be used).  Even then, be prepared to wait a few hours until all
is done.  Sounds bad?  Not really, because the whole analysis is quite a complex
process, but both the original setup of MoVRs and the setup of particular
analyses takes only a few minutes each.  Once launched, go on thinking about
your science, or start drafting the paper!

## Preliminary Steps

MoVRs is a workflow that invokes easily available third-party software as well
as scripts developed in our group.  As a first step, go to the [src](./src)
directory and install required programs as per instructions in the
[README](./src/README.md) file in that directory.  You will need to keep
track of the paths to the installed binaries.  Although quite a few external
programs are involved, typical installation can be scripted (as described) and
would not take more than a few minutes.

MoVRs relies on a number of bash, Perl, python, and R scripts that are placed in
the [scripts](./scripts) directory.  The Perl, python, and R scripts use various
packages that must be pre-installed on your system.  Run the
_xcheckprerequisites_ bash script in the [scripts](./scripts) directory to see
what is available.  If packages are missing, you need to install them prior to
running the MoVRs workflow (there are different ways to install these packages;
if in doubt, ask your systems administrator).

## Finally

proceed to the [HOWTO](./HOWTO.md) document, and we'll tell you how to execute
sample workflows (or, equally easy, your very own data analyses).
