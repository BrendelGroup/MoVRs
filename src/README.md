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

Unless otherwise indicated, it is assumed that you download the software from
the given URL into your ~/Downloads directory.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

BLAST
```
	mkdir BLAST; cd BLAST
	wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/LATEST/ncbi-blast-2.4.0+-x64-linux.tar.gz
	tar -xzf ncbi-blast-2.4.0+-x64-linux.tar.gz
	cd ncbi-blast-2.4.0+/bin
	cp * /usr/local/bin/
	cd ../..
```

BLAT
from http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/
```
	mkdir BLAT
	cd BLAT
	cp ~/Downloads/blat ./
	cp blat /usr/local/bin
	chmod a+x /usr/local/bin/blat
	cd ..
```

GHOSTSCRIPT
from http://www.ghostscript.com/download/gsdnld.html
```
	mkdir GHOSTSCRIPT
	cd GHOSTSCRIPT
	cp ~/Downloads/ghostscript-9.19-linux-x86_64.tgz ./
	tar -xzf ghostscript-9.19-linux-x86_64.tgz
	cd ghostscript-9.19-linux-x86_64
	cp gs-919-linux_x86_64 /usr/local/bin/gs
	cd ../..
```

MEME
from http://meme-suite.org/doc/download.html
```
	mkdir MEME
	cd MEME
	cp ~/Downloads/meme_4.11.2_1.tar.gz ./
	tar -xzf meme_4.11.2_1.tar.gz
	cd meme_4.11.2
	./configure --prefix=/usr/local/src/MEME/meme_4.11.2 --with-url="http://meme-suite.org"
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
	cp ~/Downloads/weblogo.2.8.2.tar.gz ./
	tar -xzf weblogo.2.8.2.tar.gz
	cd ..
```

HOMER
from http://homer.salk.edu/homer/
```
	cd HOMER
	perl configureHomer.pl -install homer >& err
	chmod -R a+w data
	cd ..
```

MoVRs
```
	git clone https://github.com/brendelgroup/MoVRs.git
```

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#### Setting up required R packages (execute the following within R):

```
	source("http://bioconductor.org/biocLite.R")
	biocLite("seqLogo")
```

#### Setting up your environment: bash

Add to ~/.bashrc the following lines (edit appropriately):

```
# needed for MoVRs:
#
export PATH="/usr/local/src/anaconda3/bin:$PATH"
export PATH="$PATH:/usr/local/src/WEBLOGO/weblogo"
export PATH="$PATH:/usr/local/src/MEME/meme_4.11.2/bin"
export PATH="$PATH:/usr/local/src/HOMER/bin"
export PATH="$PATH:/usr/local/src/MoVRs/scripts"
```

#### Setting up your environment: python

There are different ways to do this.  Here is one convenient and widely used
way using Anaconda:

from https://www.continuum.io/downloads#_unix
```
	cp ~/Downloads/Anaconda3-4.1.1-Linux-x86_64.sh ./
	bash Anaconda3-4.1.1-Linux-x86_64.sh
```

Then you can create a python environment for MoVRs as follows:

```
conda create --name movrs python=2.7 networkx matplotlib
source activate movrs
```
