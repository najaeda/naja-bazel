# SPDX-License-Identifier: MIT

# Load merged.lib and 1_synth.v, printa report, then
# write it out again.
from najaeda import netlist
from najaeda import naja
import sys

print("Args:", sys.argv)

liberty_files = sys.argv[1]
print("Loading liberty files:", liberty_files)
netlist.load_liberty(liberty_files)
print("Loading netlist from:", sys.argv[3:])
top = netlist.load_verilog(sys.argv[3:])
print("Dumping netlist to:", sys.argv[2])
        
# print the max logic level paths
print("Logic level count ", netlist.get_max_logic_level()[0])
        
# print the max logic level paths
max_level_paths = netlist.get_max_logic_level()[1]
for path in max_level_paths:
    for term in path:
        print(term, "of model", term.get_instance().get_model_name())
        for attr in term.get_instance().get_attributes():
            print("   ", attr)

print("Max Logic level count is: ", netlist.get_max_logic_level()[0])

max_fanout = netlist.get_max_fanout()
print("max_fanout",max_fanout)
print(max_fanout[0])
for terms in max_fanout[1]:
    print("Fanout for terminal", terms[0], "of model", terms[0].get_instance().get_model_name(),":")
    for attr in terms[0].get_instance().get_attributes():
            print("   ", attr)
    for t in terms[1]:
        print(t , "of model", t.get_instance().get_model_name())
        for attr in t.get_instance().get_attributes():
            print("   ", attr)
top.dump_verilog(sys.argv[2])
print("Done")





