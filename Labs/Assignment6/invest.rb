
class Count
	attr_accessor :category
	attr_accessor :count

	def to_s
		"#{@category} & #{@count} \\\\ \\hline"
	end
end

content = File.open("invest.par.frames").read
lines = content.split("\n")

counts = {}
list = []

for line in lines do
	counts[line] ||= 0
	counts[line] += 1
end

for category, count in counts do
	c = Count.new
	c.category = category
	c.count = count
	list << c
end

list.sort! do |a, b|
	i = (a.count <=> b.count) * -1
	if i == 0 then
		i = (a.category <=> b.category)
	end
	i
end

for item in list do
	puts item
end

