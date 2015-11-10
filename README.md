# Radio-Frequency-Assignment-using-constraint-Satisfaction
In an eort to improve public safety, the U.S. Federal Communications Commission (FCC) decides to open up
new wireless radio frequencies to be used by the government of each U.S. state for emergency communication
purposes. Ideally each state would receive its own unique frequency to avoid potential interference, but there
are two problems with this. First, there isn't enough free bandwidth for 50 new frequencies; in fact, there's
only room for 4. Second, some states (fortunately, relatively few) have legacy communication equipment
that only works on one particular frequency, and unfortunately some of these frequencies are the same across
states. Fortunately, as an enterprising young consultant, you realize that since radio waves have limited
range, it's sucient to ensure that nearby states do not share the same frequencies.
Write a Python program that assigns a frequency A, B, C, and D to each state, subject to the constraints
that (1) no two adjacent states share the same frequency, and (2) the states that have legacy equipment that
supports only one frequency are assigned to that frequency. Your program should be run like this:
python radio.py legacy constraints le
where legacy constraints le is an input to your program and has the legacy constraints listed in a format
like this:
Indiana A
New_York B
Washington A
The output from your program should be a le called results.txt which lists all fty states and a frequency and number of backtracks
