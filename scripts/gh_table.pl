#!/usr/bin/perl

my $n=0;
my $len;
my $hlen;
while(<>) {
    chomp;
    if ($n==0 && m@^\#@) {
        s@^\#@@;
    }
    my (@vals) = split(/\t/,$_);
    @vals = map {s@\|@, @g; $_} @vals;
    if (!$hlen) {
        $hlen = scalar(@vals);
    }
    while (scalar(@vals) < $hlen) {
        push(@vals, '');
    }
    print '|'.join('|',@vals)."|\n";
    $nulen = scalar(@vals);
    if ($n > 0) {
        if ($len ne $nulen) {
            print STDERR "MISMATCH: $len != $nulen\n";
        }
    }
    $len = $nulen;
    if ($n ==0) {
        @vals = map {"---"} @vals;
        print '|'.join('|',@vals)."|\n";
    }
    $n++;
}