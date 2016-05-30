# enumerate adds counter to an iterator

l = ["foo", "bar", "baz"]

format = '%d %s'
for count, x in enumerate(l):
    print format % (count, x)

# we can start enumerate counter from any index

for count,x in enumerate(l,97):
    print format % (count,x)
