# MoVRs HOWTO - examples for how to use the software

## Preparation

At this stage, you should have completed the __MoVRs__ installation steps
documented in the [INSTALL](./INSTALL.md) document.  Here we explain
basic use of __MoVRS__ with the test (toy) data provided in the [test](../test)
directory.  For research applications, please see our
[publication](http://brendelgroup.org/).

## Overview
Finding motifs in DNA sequences breaks down to a few fundamental
concepts:
* define __regions of interest__ (__roi__), i.e. genomic sequences that may contain specific DNA motifs to be discovered
* define __background__ sequences, i.e. genomic (or "random") sequences not expected to contain the specific DNA motifs
* identify over-represented patterns in __roi__ versus __background__ as candidate (biologically meaningful) motifs

There nice programs available to do just that.  __MoVRs__ is built
around the [HOMER](http://homer.salk.edu/homer/) software.  You can
easily adopt __MoVRs__ to work with other programs - after all,
__MoVRs__ is just a Linux _bash_ script wrapped around existing
motif-finding software, with a few useful additions.
The goal of __MoVRs__ is to reduce the set of candidate motifs
reported by a genome-wide application of a program like
[HOMER](http://homer.salk.edu/homer/) to a largely non-overlapping
and statistically cross-validated set of motifs.  Compared to a
one-pass genome-wide application of DNA motif-finding, __MoVRs__
implements a several step workflow.  Justification, details, and
research examples are provided in our
[publication](http://brendelgroup.org/).  This document reviews the mechanics of running __MoVRs__.

## Input
To get going, simply type MoVRs on your commandline, with result as follows:

```
MoVRs

    Usage: ./MoVRs <input with either -a, -f, or -i> <genome and background settings> [options]

    Examples:
      ./MoVRs -a testpeakfile --genome ./TestGenome -o TEST1 --size [-60,40] -p 10 >& errTEST1
      ./MoVRs -a testpeakfile --genome ./TestGenome -o TEST1 --size [-60,40] -p 10 --minpresence 7 --startfromstep step5 >& errTEST1AGAIN
      ./MoVRs -a testpeakfile -G hg19 -o TEST2 --size [-60,40] -k 5 -p 10 >& errTEST2
      ./MoVRs -f testfastafile -b Background/testbackground -S 10 -k 3 -p 9 --outputdir TEST3 >& errTEST3
      ./MoVRs -i testidfile -r human -G hg19 --size [-200,100] -S 15 -k 4 -p 8 --outputdir TEST4 >& errTEST4

    MoVRs will determine candidate motifs in a several-steps workflow.  You can specify
    partial workflow execution by specifying "stepX" [X = 1, 2, ..., 7] as argument to
    --startfromstep, --stopatstep, or --runonlystep.

    Step 1  Setting up training and validation sets
    Step 2  HOMER de novo motif finding in training sets
    Step 3  Motif extraction, filtering, and comparison
    Step 4  Generating motif clusters
    Step 5  Derivation of consensus motifs
    Step 6  MoVRs motif presentation and annotation
    Step 7  Find MoVRs consensus motifs in regions of interest

    To see more help, type "./MoVRs -h" or "./MoVRs --help".


MoVRs -h
MoVRs --help
```

Following the hint to see more help would produce the additional messages
```
      You must specify input in one of three forms:
        1a) -a/-g or -a/-G combination    (peak or BED file and genome file or identifier)
        1b) -f/-b combination             (FASTA target and background files)
        1c) -i/-r/-G combination          (GeneID file and preprocessed promoter set as well as genome identifier)

      Other options default to the specified values if not set.
      Details:

      1a) peak or BED file input to HOMER:
        -a|--annotation <peak|BED file>   Input file specifying genomic regions of interest
        -b|--background <peak|BED file>   (Non-mandatory) file specifying background regions
        -g|--genome <path>                Path to chromosome files
        -G|--Genome <identifier>          Identifier of HOMER-preprocessed genome
      1b) FASTA file input to HOMER:
        -f|--fasta <path>                 FASTA-formatted input file with regions of interest
        -b|--background <path>            (Mandatory) FASTA-formatted file with background regions
      1c) Gene identifier and promoter input to HOMER:
        -i|--geneID <file>                List file of gene identifiers
        -r|--promoter <file>              (Mandatory) Corresponding HOMER-supported promoter set identifier
                                            [Choice: human, mouse, rat, fly, worm, zebrafish, or yeast]
      2) Window and motif length and number input to HOMER
        -s|--size <string>                HOMER size argument (<#> or <[#,#]> or "given") [Default: 200]
        -l|--length <string>              HOMER motif length argument (<#> or <#>,<#>,...) [Default: 8,10,12]
        -S|--nummotifs <#>                HOMER argument for the number of motifs of each length to find) [Default: 25]
      3) MoVRs-specific options:
        -k <#>                            Conduct <#>-fold crossv-validation [Default: 10]
        -p|--numproc <#>                  Use <#> processors during execution [Default: 1]; ideally a multipe of the -k argument.
        -m|--mmquality <1e-#>             Minimum motif quality for motif to be considered [Default: 1e-3]
        -t|--ttthreshold <1e-#>           Threshold for tomtom motif similarity [Default: 1e-3]
        --minpresence <#>                 Minimal number of training sets in which a MoVRs motif must occur [Default: -k argument minus 1]
        -o|--outputdir <path>             Put output into directory <path> [Default: ./]
        -c|--configfile <path>            Configuration file [Default: /home/vbrendel/gitwd/MoVRs/scripts/MoVRs.conf]
      4) MoVRs workflow settings; <step> below must be one of (step1, step2, ..., step7)
         --startfromstep <string>	  Starting step; previous steps must have run successfully before.
         --stopatstep <string>            Last step to execute
         --runonlystep <string>           Workflow step to execute; previous steps must have run successfully before.
      5) Else:
        -h|--help                         Show this usage information

```
__MoVRs__ takes __roi__ and __background__ in the three flavors supported by
[HOMER](http://homer.salk.edu/homer/):

* Peak or BED file (specifying the __roi__ in terms of genomic ranges)
* FASTA file (directly supplying the sequences of the __roi__)
* geneID file (specifying the __roi__ with Gene Identifiers)

Please refer to the extensive and excellent [HOMER](http://homer.salk.edu/homer/)
documentation to review formats and specifics.

## Sample __MoVRs__ invocations
```
MoVRs -a testpeakfile --genome ./TestGenome -o TEST1 --size [-60,40] -p 10 >& errTEST1
```
takes the __testpeakfile__ and __TestGenome__ files as input and finds motifs in
the range -60 to +40 relative to the annotated peaks.  The program will use 10 processors.

```
MoVRs -a testpeakfile --genome ./TestGenome -o TEST1 --size [-60,40] -p 10 --minpresence 7 --startfromstep step5 >& errTEST1AGAIN
```
reruns the previous example, but with criterion that only 7 (instead of the default 9)
training sets generated in the 10-fold cross-validation must contain a motif to be
considered a validated candidate motif.  The first four steps of the workflow are not
rerun.

```
MoVRs -a testpeakfile -G hg19 -o TEST2 --size [-60,40] -k 5 -p 10 >& errTEST2
```
runs data corresponding to the preloaded human genome hg19.  The -k argument specifies
5-fold cross-validation.

```
MoVRs -f testfastafile -b Background/testbackground -S 10 -k 3 -p 9 --outputdir TEST3 >& errTEST3
```
takes the specified FASTA-formatted __roi__ and background sequences and restrictsyy
HOMER](http://homer.salk.edu/homer/) to report only the best 10 motifs in each run.

```
MoVRs -i testidfile -r human -G hg19 --size [-200,100] -S 15 -k 4 -p 8 --outputdir TEST4 >& errTEST4
```
looks for motifs in the -200 to 100 range in the promoters of the human genes specified in
the testidfile file.


## Steps in the workflow
A great way of learning what the __MoVRs__ workflow entails is to run an example in
stepwise fashion.  Just add the option __--runonlystep step1__ to your favorite
example.  That will stop the workflow after the first step (summarized below).
Look at the program logfiles and output, follow up on the program documentation,
and take a mental snapshot of what this step accomplished.  Then replace
__--runonlystep step1__ by __--runonlystep step2__ and continue in similar fashion
until the final step.

##### Step 1: Setting up training and validation sets
This step will create the training and validation sets in the specified
output directory, subdirectories _tmpTrainingDir_ and _tmpValidationDir_.

##### Step 2: [HOMER](http://homer.salk.edu/homer/) de novo motif finding in training sets
This step will run the appropriate [HOMER](http://homer.salk.edu/homer/) motif
finder on each of the training sets.  Records of this step are in _tmpTraingDir_, and
final 9utput is deposited in the output subdirectory _tmpMotifDir_.

##### Step 3:  Motif extraction, filtering, and comparison
Run in the _tmpMotifDir_, this step processes the motifs produced by the
[HOMER](http://homer.salk.edu/homer/) run.  Motifs exceeding a quality threshold
specified by option -m are pairwise compared using the MEME suite _tomtom_ tool,
and labeled similar if exceeding the threshold specified by option -t.
Results are deposited into output subdirectory _tmpMotifDir/TOMTOMresults_.

##### Step 4:  Generating motif clusters
This step invokes the _MoVRs\_GetCluster.py_ script that generates motif
clusters based on the tomtom similarity values obtained in the previous step.
Results are deposited into output subdirectory _tmpMotifDir/MCLUSTERresults_.

##### Step 5:  Derivation of consensus motifs
This step invokes the _MoVRs\_MotifSetReduce.pl_ script to generate consensus
motifs for each motif cluster obtained in the previous step.  The consensus
motifs are recorded in files _tmpMotifDir/MCLUSTERresults/mcluster*.cmotif_.

##### Step 6:  MoVRs motif presentation and annotation
In this step, the _mcluster*.cmotif_ files are further processed to show
seqLogos and similarity with known motifs.
Results are deposited into output subdirectory _MoVRs\_OutputDir_.

##### Step 7:  Find MoVRs consensus motifs in regions of interest
In the final step, the appropriate [HOMER](http://homer.salk.edu/homer/)
tools are used to tabulate occurrences of the __MoVRs__ consensus motifs
in the __roi__.
See files _MoVRs\_OutputDir/mcluster*.tab_.


## Output and examination of results
We are still working on nice summaries of results.
Until then, you are on your own ...
