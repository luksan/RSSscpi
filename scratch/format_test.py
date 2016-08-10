from RSSscpi.gen.Instrument import SCPICmdFormatter

fmt = SCPICmdFormatter()

print fmt.format("{0:s}", "hej")
print fmt.format("{0:q}", "HEJsan")

print fmt.format("{0:d*}", [1,2,3])
print fmt.format("{:.2f*}", [1,2,3])
print fmt.format("{:e*}", [1,2,3])
print fmt.format("{} - {:q*}", "CMd", ["str", "list"])

print fmt.format("{:d**}", zip([1,2,3], [4,5,6]))
