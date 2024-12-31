extends Node

var x = 1
const pi = 1.14

export var y = 10
export(Texture) var image

var list1 = []
var list2 = Array()
var list3 = [1, 2, 3]
var list4 = [
	1,
	2,
	3
]

var dict1 = {}
var dict2 = Dictionary()
var dict3 = {"Name": "SALAH", "Age": 20}
var dict4 = {
	"Name": "SALAH",
	"Age": 20
}

func _ready():
	for i in [$Parent.get_child(0), $Parent.get_child(1)]:
		print(i.name)
	print(find_node("Child2", true, false))
	
	list1.append(1)
	dict1["Name"] = "SALAH"
	print(list1[0])
	print(dict1["Name"])
	
	print(Global.num)

	x = 1
	match x:
		1:
			print("x: 1")
		2:
			print("x: 2")
		_:
			print("!")

	pass

func _process(delta):
	pass
