extends KinematicBody2D

var pos: int = 0
var speed: int = 10

func _ready():
	position = Vector2(0, 0)

func _process(delta):
	pos += 1
	print(pos*speed, pos*speed)
	position += Vector2(pos, pos) * speed

	if(position.x >= 1006 && position.y >= 580):
		position = Vector2(0, 0)
		pos = 0
