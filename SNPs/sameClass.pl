#/usr/bin/perl
use warnings;
use diagnostics;
use strict;
use Data::Dumper;
opendir(DH, "/mnt/project/tmhpred/willbebig/snap2/");
my @files = readdir(DH);
closedir(DH);

my @hydrophobic = ("C","G","A","V","T","I","L","M","F","Y","W","H","K");
my @polar = ("S","N","C","Q","T","D","E","K","Y","H","R","W");
my @small = ("P","C","A","G","S","N","V","T","D");

foreach my $file (@files)
{
    if ($file =~ /.*\.snap2/){
    
    # skip . and ..
    next if($file =~ /^\.$/);
    next if($file =~ /^\.\.$/);

	my $i = 0;
        $file = "/mnt/project/tmhpred/willbebig/snap2/".$file; 
        my @array = `cat $file | awk '{if(\$2 ~ /=>/) {printf (\"%s\\t%s\\n\",\$1,\$35)}}'`;
	foreach(@array){
		my $change = $_;
		#if($change =~ /[A-Z][0-9]+[A-Z]\s+([\-]*[0-9]+)/){print $1."\n";}
		if($change =~ /([A-Z])([0-9]+)([A-Z])\s+([\-]*[0-9]+)/){
		

		my @original;
                my @snp;
                my $first = $1;
                my $third = $3;
		my $score = $4;
                my $ref = $_;  

		foreach(@hydrophobic){
                        if ($first =~ $_){push(@original,"h");}
                        if ($third =~ $_){push(@snp,"h");}
                }
                foreach(@polar){
                        if ($first =~ $_){push(@original,"p");}
                        if ($third =~ $_){push(@snp,"p");}
                }
                foreach(@small){
                        if ($first =~ $_){push(@original,"s");}
                        if ($third =~ $_){push(@snp,"s");}
                }
		my %seen;
	        my @final;

        	@seen{@original} = ();

        	foreach my $new ( @snp ) {
        	push (@final, $new ) if exists $seen{$new};
        	}
        	foreach(@final){print $_."\t".$score."\n";}
		}
	}
	
     }#if snap2 ordner
}#for

