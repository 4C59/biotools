#pbs_qsub.pl -j [job_list]-w [wall_time, default 4 hours] -m [memory,defaul 1G] -t [#_of_CPU]
'''
a script to submit job list,this script will creat pbs-script for jobs autoly
can help you use pbs qsub submit job quickly
'''
#!/usr/bin/perl
use strict;
my %args = @ARGV;
my $jobfile=$args{'-j'};
my $walltime=$args{'-w'}||"4:00:00";
my $mem=$args{'-m'}||"1G";
my $ncpu=$args{'-t'}||1;  # number of threads per processor
my $cnode=$args{'-n'}||41; #which node

unless (-f $jobfile){
  print "\'-j\' jobs list file must be specified ! Exit now!\n";
  exit;
}

open (my $fh,"<",$jobfile) or die "Can't open job list file $!";
my $count;

while(<$fh>){
	my $script = $jobfile.".pbs.scripts";
	open (my $pbs,">$script")||die "Can't open script file $script $!";
	print $pbs "\#\!\/bin\/bash\n\#PBS -l walltime=$walltime\n#PBS -l mem=$mem\n#PBS -l nodes=$cnode:ppn=$ncpu\n\#PBS -j oe\n";
	print $pbs "cd \$PBS_O_WORKDIR\n"; 
	print $pbs "$_\n";
	close $pbs;
	`qsub $script`;
	`rm $script`;
	$count++;
}

print "$count jobs have submitted to the PBS system.\n";
