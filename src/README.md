++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

## MoVRs - system wide installation of required software

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

##### README
Sources and installation notes (current as of August 19, 2016)

Our recommendation is to install the required programs system-wide.
Typical would be to run the installation steps as superuser after
_"cd /usr/local/src"_.  Even better might be to create a directory
_/usr/local/src/MoVRs_ and install the programs there; this might
avoid clashes with other programs you are running that possibly
depend on earlier versions of the same packages.

Sources of the programs are listed.  Please see the cited URLs for
details on the software and installation.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

BLAST
```
	mkdir BLAST; cd BLAST
	wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.9.0+-x64-linux.tar.gz
	tar -xzf ncbi-blast-2.9.0+-x64-linux.tar.gz
	cd ncbi-blast-2.9.0+/bin
	cp * /usr/local/bin/
	cd ../../..
```

BLAT
from http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/
```
	mkdir BLAT
	cd BLAT
	wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/blat
	cp blat /usr/local/bin
	chmod a+x /usr/local/bin/blat
	cd ..
```

GHOSTSCRIPT
from http://www.ghostscript.com/download/gsdnld.html
```
	mkdir GHOSTSCRIPT
	cd GHOSTSCRIPT
	wget https://github.com/ArtifexSoftware/ghostpdl-downloads/releases/download/gs927/ghostscript-9.27-linux-x86_64.tgz
	tar -xzf ghostscript-9.27-linux-x86_64.tgz
	cd ghostscript-9.27-linux-x86_64
	cp gs-927-linux_x86_64 /usr/local/bin/gs
	cd ../..
```

MEME
from http://meme-suite.org/doc/download.html
```
	mkdir MEME
	cd MEME
	wget http://meme-suite.org/meme-software/5.0.5/meme-5.0.5.tar.gz
	tar -xzf meme-5.0.5.tar.gz
	cd meme-5.0.5
	./configure --prefix=/usr/local/src/MEME/meme-5.0.5 --with-url="http://meme-suite.org"
	make
	make test
	make install
	cd ../..
```

SAMTOOLS
```
	mkdir SAMTOOLS
	cd SAMTOOLS
	git clone git://github.com/samtools/htslib.git htslib
	cd htslib
	make
	cd ..
	git clone git://github.com/samtools/samtools.git samtools
	cd samtools
	make
	cp samtools /usr/local/bin
	cd ../..
```

WEBLOGO
from http://weblogo.berkeley.edu/
```
	mkdir WEBLOGO
	cd WEBLOGO
	wget http://weblogo.berkeley.edu/release/weblogo.2.8.2.tar.gz
	tar -xzf weblogo.2.8.2.tar.gz
	cd ..
```

HOMER
from http://homer.salk.edu/homer/
```
	mkdir HOMER
	cd HOMER
	wget http://homer.ucsd.edu/homer/configureHomer.pl
	perl configureHomer.pl -install homer >& err
	chmod -R a+w data
	cd ..
```

MoVRs
```
	git clone https://github.com/BrendelGroup/MoVRs.git
```

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#### Setting up required R packages (execute the following within R):

```
	if (!requireNamespace("BiocManager", quietly=TRUE))
	   install.packages("BiocManager")
	BiocManager::install(c("seqLogo"))
```

#### Setting up your environment: bash

Add to ~/.bashrc the following lines (edit appropriately):

```
# needed for MoVRs:
#
export PATH="~/anaconda3/condabin:$PATH"
export PATH="$PATH:/usr/local/src/MoVRs/WEBLOGO/weblogo"
export PATH="$PATH:/usr/local/src/MoVRs/MEME/meme-5.0.5/bin"
export PATH="$PATH:/usr/local/src/MoVRs/HOMER/bin"
export PATH="$PATH:/usr/local/src/MoVRs/MoVRs/scripts"
```

#### Setting up your environment: python

There are different ways to do this.  Here is one convenient and widely used
way using Anaconda (as non-privileged user rather than root):

from https://www.continuum.io/downloads#_unix
```
	wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
	bash Anaconda3-2019.07-Linux-x86_64.sh 
```

Then you can create a python environment for MoVRs as follows:

```
conda create --name movrs python=3.6 networkx matplotlib
source activate movrs
```
