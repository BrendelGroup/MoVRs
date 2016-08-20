#!/bin/sh

echo ""
echo "Perl binary:"
which perl
echo "Version:"
perl --version | egrep "This is"

echo "PERL5LIB:"
echo ""
echo $PERL5LIB
echo ""

perl -e 'print "Perl \@INC includes\n\n"; foreach (@INC) {print $_,"\n";};'

echo ""
echo "Checking for modules"
echo ""

echo "Required for MoVRs"
modules=(strict Getopt::Std Data::Dumper)
for i in ${!modules[*]}
do
    j=$[$i+1]
    module=${modules[$i]}
    printf "%4d) %s\t\t\t" $j ${module}
    perl -e "use ${module}; print \"Version installed:\t\", \$${module}::VERSION, \"\n\";"
done
